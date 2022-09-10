#!/bin/bash

# https://github.com/coqui-ai/TTS

U=$USER
D="/home/$U/.local/share/tts/tts_models--en--vctk--vits"
mkdir -p "$D"
if [ ! -f "$D/model_file.pth" ]; then
  tar xzf tts-model.tgz -C "$D"
fi

apt install sox espeak-ng
pip3 install TTS==0.8.0
