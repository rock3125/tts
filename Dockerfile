FROM ubuntu:focal

ENV TZ=Europe/London

# set timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN echo $TZ > /etc/timezone

RUN apt update -y
RUN apt upgrade -y

RUN apt install sox espeak-ng python3-pip -yqq
RUN pip3 install TTS==0.8.0

RUN mkdir -p /app
COPY server.py /app/server.py
WORKDIR /app

#COPY tts-model.tgz /app/tts-model.tgz
#RUN mkdir -p /root/.local/share/tts/tts_models--en--vctk--vits
#RUN tar xzf /app/tts-model.tgz -C /root/.local/share/tts/tts_models--en--vctk--vits

CMD /app/server.py
