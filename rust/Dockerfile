FROM rust:1.21.0
ENV LD_LIBRARY_PATH /usr/local/lib
ENV LLVM_CONFIG_PATH /usr/bin/llvm-config-3.8
ENV LIBCLANG_PATH /usr/lib/llvm-3.8/lib/

# TrailDB Steps
RUN apt-get update
RUN apt-get install -y libarchive-dev libjudy-dev pkg-config python llvm clang
WORKDIR /opt/traildb
ADD https://github.com/traildb/traildb/archive/0.6.tar.gz .
RUN tar xfz 0.6.tar.gz
WORKDIR /opt/traildb/traildb-0.6
RUN ./waf configure
RUN ./waf install
RUN ln -s /usr/lib/llvm-3.8/lib/libclang.so.1 /usr/lib/llvm-3.8/lib/libclang.so

# Rust steps
WORKDIR /opt/benchmark
COPY . .
# RUN cargo install

# # Copy Wikipedia
# # ADD http://traildb.io/data/wikipedia-history-small.tdb /mnt/data/wikipedia-history-small.tdb
# ADD http://192.168.1.102:8000/wikipedia-history-small.tdb /mnt/data/wikipedia-history-small.tdb