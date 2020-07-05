FROM node as build-stage
WORKDIR /ui/
ADD bot/ui .

RUN npm install
RUN npm run buld

FROM python:3.7.3 as deploy-stage

VOLUME [ "/app" ]
WORKDIR /app

COPY wsgi.py /app
ADD bot /app/bot

RUN pip install -r bot/requirements.txt

COPY --from=build-stage /ui public

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8080", "wsgi:app" ]