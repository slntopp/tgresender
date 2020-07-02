FROM python:3.7.3

VOLUME [ "/app" ]
WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY conf.yml .
COPY main.py .

ENTRYPOINT ["python", "main.py"]