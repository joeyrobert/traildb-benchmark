FROM crystallang/crystal
ENV LD_LIBRARY_PATH /usr/local/lib

# TrailDB Steps
RUN apt-get update
RUN apt-get install -y libarchive-dev libjudy-dev pkg-config python
WORKDIR /opt/traildb
ADD https://github.com/traildb/traildb/archive/0.6.tar.gz .
RUN tar xfz 0.6.tar.gz
WORKDIR /opt/traildb/traildb-0.6
RUN ./waf configure
RUN ./waf install

# Crystal setup
WORKDIR /opt/benchmark
COPY crystal .
RUN shards install
RUN crystal build benchmark.cr --release --no-debug

# Copy Wikipedia
COPY ./wikipedia-history-small.tdb /mnt/data/wikipedia-history-small.tdb