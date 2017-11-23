FROM ubuntu:16.04
# # Copy Wikipedia
RUN apt-get update && apt-get install -y curl
RUN mkdir -p /mnt/data
RUN curl http://traildb.io/data/wikipedia-history-small.tdb > /mnt/data/wikipedia-history-small.tdb

RUN apt-get install -y dirmngr
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 575159689BEFB442
RUN echo 'deb http://download.fpcomplete.com/ubuntu xenial main' >> /etc/apt/sources.list.d/fpco.list
RUN apt-get update && apt-get install -y ghc stack

ADD ./stack.yaml /opt/benchmark/stack.yaml
WORKDIR /opt/benchmark
RUN stack setup
ADD . /opt/benchmark
RUN stack build --copy-bins --local-bin-path /opt/benchmark

