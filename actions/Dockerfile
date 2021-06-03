FROM rasa/rasa-sdk:2.0.0

 # The Rasa SDK image runs as non-root user by default. Hence, you have to switch
 # back to the `root` user if you want to install additional dependencies
USER root

RUN apt-get update
RUN apt update

RUN pip3 install typing_extensions
RUN pip3 install pandas
RUN pip3 install spacy
RUN python -m spacy download en_core_web_md

RUN apt-get update

# Switch back to a non-root user
USER 1001
