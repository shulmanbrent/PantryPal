FROM ubuntu:14.04
MAINTAINER Brent Shulman <shulmanbrent@yahoo.com>

RUN apt-get update

# Install development environment
RUN apt-get install --assume-yes python-dev
RUN apt-get install --assume-yes libhdf5-dev
RUN apt-get install --assume-yes python-pip
RUN apt-get install --assume-yes libpq-dev
RUN apt-get install --assume-yes wget

# Download and install heroku toolbelt
RUN wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# Stage files in current folder in /data
ADD . /data

RUN pip install -r /data/requirements.txt

# setup data volume
VOLUME ["/data"]

# default to shell
CMD ["/bin/bash"]
