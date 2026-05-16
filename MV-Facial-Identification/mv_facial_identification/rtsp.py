from __future__ import annotations
import cv2

class RTSPReader:
    def __init__(self, rtsp_url: str) -> None:
        self.rtsp_url = rtsp_url
        self.capture = cv2.VideoCapture(self.rtsp_url)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.capture.isOpened():
            raise StopIteration

        success, frame = self.capture.read()
        if not success:
            raise StopIteration
        return frame

    def release(self) -> None:
        self.capture.release()
