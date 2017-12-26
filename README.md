# Simple text to speech docker container using EnglishHTSVoices

## build
```
docker build -t tts .
```

## run service on port 81
```
docker run -d --rm -p 81:80 --name tts -i tts
```

and then hit the service

```
curl http://localhost:8080/api/v1/tts/Test --output - > test.mp3
```

## sample
listen to a [sample](sample/test.wav) produced by this system
