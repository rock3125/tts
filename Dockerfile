FROM ubuntu:16.04

ENV LANG="C.UTF-8"

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        python3 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app
RUN ./do_build


WORKDIR /app

CMD ["./tts.py"]
# CMD ["./run-uk.sh"]

