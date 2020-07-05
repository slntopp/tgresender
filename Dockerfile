FROM python:3.7.3

VOLUME [ "/app" ]
WORKDIR /app

COPY wsgi.py /app
ADD bot /app/bot

RUN pip install -r bot/requirements.txt

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8080", "wsgi:app" ]