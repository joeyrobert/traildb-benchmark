FROM ubuntu:16.04
ENV LD_LIBRARY_PATH /usr/local/lib

# TrailDB Steps
RUN apt-get update
RUN apt-get install -y libarchive-dev libjudy-dev pkg-config python python-ply libjson-c-dev libcmph-dev libc6-dev libjemalloc-dev libcurl4-openssl-dev libmsgpack-dev jq git
WORKDIR /opt/traildb
ADD https://github.com/traildb/traildb/archive/0.6.tar.gz .
RUN tar xfz 0.6.tar.gz
WORKDIR /opt/traildb/traildb-0.6
RUN ./waf configure
RUN ./waf install

# Trck steps
WORKDIR /opt/benchmark
COPY trck .
RUN git clone https://github.com/traildb/trck.git
WORKDIR /opt/benchmark/trck
RUN git submodule update --init --remote --recursive
RUN make
RUN ./bin/trck -c /opt/benchmark/benchmark.tr -o /opt/benchmark/benchmark
WORKDIR /opt/benchmark

# Copy Wikipedia
COPY ./wikipedia-history-small.tdb /mnt/data/wikipedia-history-small.tdb