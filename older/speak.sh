#!/bin/bash

if [ "$1" == "" ]; then
  printf "takes one parameter: text to speak\n"
  exit 1
fi

# pip3 install TTS
# sudo apt install sox espeak-ng

rm -f test.wav
tts --text "$1" --model_name tts_models/en/vctk/vits --out_path test.wav --speaker_idx p343 > /dev/null
aplay test.wav
