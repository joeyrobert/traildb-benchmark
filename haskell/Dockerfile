FROM haskell:8.2.1

# TrailDB Steps
RUN apt-get update
RUN apt-get install -y libarchive-dev libjudy-dev pkg-config python build-essential
WORKDIR /opt/traildb
ADD https://github.com/traildb/traildb/archive/0.6.tar.gz .
RUN tar xfz 0.6.tar.gz
WORKDIR /opt/traildb/traildb-0.6
RUN ./waf configure
RUN ./waf install

# Haskell setup
ADD ./haskell/stack.yaml /opt/benchmark/stack.yaml
WORKDIR /opt/benchmark
RUN stack setup

COPY haskell /opt/benchmark
WORKDIR /opt/benchmark
RUN stack build --copy-bins --local-bin-path /opt/benchmark

ENV LD_LIBRARY_PATH /usr/local/lib
ENV LIBRARY_PATH /usr/local/lib

# Copy Wikipedia
COPY ./wikipedia-history-small.tdb /mnt/data/wikipedia-history-small.tdb