FROM ubuntu
COPY requirements.txt ./
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install -r requirements.txt
ADD src $HOME/src
WORKDIR $HOME/src
RUN pwd
RUN ls
ENV FLASK_APP=server
RUN flask init-db
RUN flask run --cert=adhoc --host=0.0.0.0
EXPOSE 8000
