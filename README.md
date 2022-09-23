## TTS - text to speech in docker
from `https://github.com/coqui-ai/TTS`
```
docker build -t tts:1.0.0 .
```

## run
```
docker run --rm --name tts -p 8080:8080 tts:1.0.0
```

## test
```
curl http://localhost:8080?t=This%20is%20a%20larger%20test%20of%20Speech%20to%20text -o test.wav
aplay test.wav
```

or test using `docker-speak.sh`

```
./docker-speak.sh "Testing the docker build for speech output."
```

