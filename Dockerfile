FROM ubuntu
# Disable warning about installing packages as root user
ENV PIP_ROOT_USER_ACTION=ignore
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
COPY ./Exporter/requirements.txt requirements.txt
# Caching disabled to reduce the size of the docker container
RUN pip3 install --no-cache-dir -r requirements.txt