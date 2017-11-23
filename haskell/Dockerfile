FROM ubuntu:16.04
# # Copy Wikipedia
RUN apt-get update && apt-get install -y curl
RUN mkdir -p /mnt/data
RUN curl -L http://192.168.1.102:8000/wikipedia-history-small.tdb > /mnt/data/wikipedia-history-small.tdb

RUN apt-get install -y dirmngr
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 575159689BEFB442
RUN echo 'deb http://download.fpcomplete.com/ubuntu xenial main' >> /etc/apt/sources.list.d/fpco.list
RUN apt-get update && apt-get install -y ghc stack

ADD ./stack.yaml /opt/benchmark/stack.yaml
WORKDIR /opt/benchmark
RUN stack setup

RUN apt-get install -y libarchive-dev libjudy-dev pkg-config python
RUN curl -L https://github.com/traildb/traildb/archive/0.6.tar.gz > 0.6.tar.gz
RUN tar xfz 0.6.tar.gz
WORKDIR /opt/benchmark/traildb-0.6
RUN ./waf configure
RUN ./waf install

COPY . /opt/benchmark
WORKDIR /opt/benchmark
RUN stack build --copy-bins --local-bin-path /opt/benchmark

ENV LD_LIBRARY_PATH /usr/local/lib
ENV LIBRARY_PATH /usr/local/lib

