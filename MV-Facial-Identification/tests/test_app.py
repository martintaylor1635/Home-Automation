from mv_facial_identification.config import AppConfig
from mv_facial_identification.rtsp import RTSPReader
from mv_facial_identification.recognition import FaceRecognizer
from mv_facial_identification.mqtt_client import MQTTClient


def test_app_config_defaults() -> None:
    config = AppConfig.load()
    assert config.rtsp_url
    assert config.mqtt_broker
    assert config.mqtt_topic


def test_rtsp_reader_initializes(monkeypatch) -> None:
    class FakeCapture:
        def isOpened(self):
            return False
        def read(self):
            return False, None
    monkeypatch.setattr("cv2.VideoCapture", lambda url: FakeCapture())
    reader = RTSPReader("rtsp://test")
    try:
        assert iter(reader) is reader
    finally:
        reader.release()
