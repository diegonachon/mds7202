FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY gradio_app.py ./
COPY pipeline.pkl ./
COPY transformations.py ./

CMD ["python", "gradio_app.py"]
