FROM python:3.7-slim-buster

WORKDIR /usr/app
CMD ["python", "-m", "src.main"]

COPY requirements.txt .
COPY setup.py .
COPY src/. src/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

ENV LOG_LEVEL INFO

EXPOSE 8080