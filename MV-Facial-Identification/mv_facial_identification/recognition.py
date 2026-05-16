from __future__ import annotations
from typing import Any

from deepface import DeepFace

class FaceRecognizer:
    def __init__(self) -> None:
        self.model_name = "VGG-Face"

    def analyze_frame(self, frame: Any) -> dict[str, Any] | None:
        analysis = DeepFace.analyze(frame, enforce_detection=False, detector_backend="opencv", model_name=self.model_name)
        if analysis and analysis.get("dominant_emotion"):
            return analysis
        return None
