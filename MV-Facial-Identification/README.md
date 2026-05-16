# MV Facial Identification

A Python application that reads RTSP camera streams, performs face recognition with DeepFace, and publishes custom events to an MQTT broker for a control center.

## Project structure

- `main.py` — simple entrypoint for the application
- `mv_facial_identification/` — main package
  - `app.py` — orchestration and runtime loop
  - `config.py` — runtime settings and environment loading
  - `rtsp.py` — RTSP stream reader
  - `recognition.py` — DeepFace inference wrapper
  - `mqtt_client.py` — MQTT publish helper
  - `events.py` — face event serialization and publishing
- `tests/` — starter tests for core components

## Getting started

### Local development

1. Install a compatible Python version: `3.10`, `3.11`, `3.12`, or `3.13`
2. Pin the interpreter using `uv`:
   ```powershell
   uv python pin 3.13
   ```
3. Install dependencies:
   ```powershell
   uv sync
   ```
4. Run the app:
   ```powershell
   python main.py
   ```

### Docker Compose (testing with local Mosquitto)

1. Ensure Docker and Docker Compose are installed
2. Copy `.env.example` to `.env` and configure your settings:
   ```powershell
   cp .env.example .env
   ```
3. Start the services:
   ```bash
   docker-compose up -d
   ```
   This will start:
   - **Mosquitto MQTT broker** on `localhost:1883`
   - **Facial identification app** connected to Mosquitto

4. View logs:
   ```bash
   docker-compose logs -f facial-identification
   ```

5. Stop the services:
   ```bash
   docker-compose down
   ```

## Configuration

The app reads configuration from environment variables:

- `RTSP_URL`
- `MQTT_BROKER`
- `MQTT_TOPIC`
- `CAMERA_NAME`
- `CONFIDENCE_THRESHOLD`

## Notes

- `deepface` is used for face recognition
- `opencv-python` is used for RTSP capture
- `paho-mqtt` publishes custom events to the MQTT broker
- **MQTT connection is optional** — the app will continue running and performing face recognition even if the MQTT broker is unavailable
- Docker Compose configuration includes a local Mosquitto broker for easy testing
