#!/bin/bash

# assumes docker is running on 8080

if [ "$1" == "" ]; then
  printf "takes one parameter: text to speak\n"
  exit 1
fi

rawurlencode() {
  local string="${1}"
  local strlen=${#string}
  local encoded=""
  local pos c o

  for (( pos=0 ; pos<strlen ; pos++ )); do
     c=${string:$pos:1}
     case "$c" in
        [-_.~a-zA-Z0-9] ) o="${c}" ;;
        * )               printf -v o '%%%02x' "'$c"
     esac
     encoded+="${o}"
  done
  echo "${encoded}"
}

rm -f test.wav
text=$(rawurlencode "$1")
curl http://localhost:8080?t=$text -o test.wav
aplay test.wav
