from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from .mqtt_client import MQTTClient

@dataclass
class FaceEvent:
    identity: str
    score: float
    emotion: str
    camera_name: str
    timestamp: str

    @classmethod
    def from_analysis(cls, analysis: dict, camera_name: str) -> "FaceEvent":
        return cls(
            identity=analysis.get("identity", "unknown"),
            score=float(analysis.get("score", 0.0)),
            emotion=analysis.get("dominant_emotion", "unknown"),
            camera_name=camera_name,
            timestamp=datetime.utcnow().isoformat() + "Z",
        )

class EventPublisher:
    def __init__(self, mqtt_client: MQTTClient) -> None:
        self.mqtt_client = mqtt_client

    def publish_face_event(self, analysis: dict, camera_name: str) -> None:
        event = FaceEvent.from_analysis(analysis, camera_name)
        payload = {
            "type": "face_recognition",
            "identity": event.identity,
            "confidence": event.score,
            "emotion": event.emotion,
            "camera": event.camera_name,
            "timestamp": event.timestamp,
        }
        self.mqtt_client.publish(payload)
