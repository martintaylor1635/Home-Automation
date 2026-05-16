from __future__ import annotations
import json
import logging
import urllib.parse

import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)

class MQTTClient:
    def __init__(self, broker_url: str, topic: str) -> None:
        self.broker_url = broker_url
        self.topic = topic
        self.client = mqtt.Client()
        self.is_connected = False
        self._configure_broker()

    def _configure_broker(self) -> None:
        parsed = urllib.parse.urlparse(self.broker_url)
        host = parsed.hostname or "localhost"
        port = parsed.port or 1883
        try:
            self.client.connect(host, port)
            self.is_connected = True
            logger.info("Connected to MQTT broker at %s:%s", host, port)
        except Exception as e:
            logger.warning("Failed to connect to MQTT broker at %s:%s: %s. Events will not be published.", host, port, e)
            self.is_connected = False

    def publish(self, payload: dict[str, object]) -> None:
        if not self.is_connected:
            logger.debug("MQTT broker not connected. Skipping event publication: %s", payload)
            return
        try:
            message = json.dumps(payload)
            result = self.client.publish(self.topic, message)
            result.wait_for_publish()
            logger.debug("Published MQTT message to %s: %s", self.topic, message)
        except Exception as e:
            logger.warning("Failed to publish MQTT message: %s", e)
            self.is_connected = False
