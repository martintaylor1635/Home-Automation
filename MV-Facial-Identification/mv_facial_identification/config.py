from __future__ import annotations
from dataclasses import dataclass
import os

@dataclass
class AppConfig:
    rtsp_url: str = os.getenv("RTSP_URL", "rtsp://example.local/stream")
    mqtt_broker: str = os.getenv("MQTT_BROKER", "mqtt://localhost:1883")
    mqtt_topic: str = os.getenv("MQTT_TOPIC", "home/facial-identification/events")
    camera_name: str = os.getenv("CAMERA_NAME", "front-door")
    confidence_threshold: float = float(os.getenv("CONFIDENCE_THRESHOLD", "0.8"))

    @classmethod
    def load(cls) -> "AppConfig":
        return cls()
