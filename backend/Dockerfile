#FROM rasa/rasa:latest-full 
FROM rasa/rasa:2.6.0-full

USER root

WORKDIR /app
COPY . /app
COPY ./data /app/data

RUN pip3 install --upgrade pip --user
RUN  python3 -m rasa train

# Switch back to a non-root user
USER 1001

VOLUME /app
VOLUME /app/data
VOLUME /app/models


CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug","--ssl-keyfile","/app/data/external_data/privkey.pem","--ssl-certificate","/app/data/external_data/fullchain.pem", "--credentials", "credentials.yml", "--endpoints", "endpoints.yml"]