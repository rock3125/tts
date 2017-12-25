# Simple text to speech docker container using EnglishHTSVoices

## build
```
docker build -t tts .
```

## run
```
echo "Hello there Peter." | docker run --rm -i tts > test.mp3
```

## sample
try a ![sample](sample/test.wav)

