from __future__ import annotations
import logging

from .config import AppConfig
from .events import EventPublisher
from .mqtt_client import MQTTClient
from .recognition import FaceRecognizer
from .rtsp import RTSPReader

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def run(config: AppConfig | None = None) -> None:
    config = config or AppConfig.load()

    try:
        mqtt_client = MQTTClient(config.mqtt_broker, config.mqtt_topic)
        publisher = EventPublisher(mqtt_client)
    except Exception as e:
        logger.error("Failed to initialize MQTT client: %s. Continuing without event publishing.", e)
        mqtt_client = MQTTClient(config.mqtt_broker, config.mqtt_topic)
        publisher = EventPublisher(mqtt_client)

    recognizer = FaceRecognizer()

    reader = RTSPReader(config.rtsp_url)
    try:
        for frame in reader:
            analysis = recognizer.analyze_frame(frame)
            if analysis is not None:
                publisher.publish_face_event(analysis, config.camera_name)
    finally:
        reader.release()


def main() -> None:
    run()
