import os
import json
import logging
import sys
import subprocess
import uuid

from flask import Flask, request
from flask_cors import CORS

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.dirname(__file__)
app = Flask(__name__)
CORS(app)


@app.errorhandler(Exception)
def _(error):
    import traceback
    logging.error(traceback.format_exc())
    return json.dumps({'error': error.__str__()}), 510, {'ContentType': 'application/javascript'}


@app.route('/', methods=['GET'])
def index():
    return '<html><body>TTS</body></html>', 200, {'ContentType': 'text/html'}


# curl http://localhost:8080/api/v1/tts/Test%20Peter --output - > test.mp3
@app.route('/api/v1/tts/<text>', methods=['GET'])
def text_to_speech(text):

    # copy incoming text to say.txt
    job_id = uuid.uuid4().__str__()
    text_file = os.path.join('/tmp/', job_id + '.txt')
    with open(text_file, 'wt') as writer:
        writer.write(text)

    # excute tts
    in_file = os.path.join('/tmp/', job_id + '.wav')
    subprocess.run([os.path.join(base_dir, 'run.sh'), text_file, in_file])

    # convert to mp3
    out_file = os.path.join('/tmp/', job_id + '.mp3')
    with open(os.devnull, 'w') as f_null:
        subprocess.call(["/usr/bin/ffmpeg", "-i", in_file, out_file], stdout=f_null, stderr=f_null)

    # write output to stdout
    if os.path.isfile(out_file):
        print('writing ' + out_file)
        with open(out_file, 'rb') as reader:
            return reader.read(), 200, {'ContentType': 'audio/mpeg'}
    else:
        return json.dumps({'error': 'file not produced'}), 510, {'ContentType': 'application/javascript'}


# curl -X POST -H "Content-Type: plain/text" --data "Say something" http://localhost:8081/api/v1/tts --output - > test.mp3
@app.route('/api/v1/tts', methods=['POST'])
def text_to_speech_2():

    text = request.data.decode('UTF-8')  # get raw request data

    # copy incoming text to say.txt
    job_id = uuid.uuid4().__str__()
    text_file = os.path.join('/tmp/', job_id + '.txt')
    with open(text_file, 'wt') as writer:
        writer.write(text)

    # excute tts
    in_file = os.path.join('/tmp/', job_id + '.wav')
    subprocess.run([os.path.join(base_dir, 'run.sh'), text_file, in_file])

    # convert to mp3
    out_file = os.path.join('/tmp/', job_id + '.mp3')
    with open(os.devnull, 'w') as f_null:
        subprocess.call(["/usr/bin/ffmpeg", "-i", in_file, out_file], stdout=f_null, stderr=f_null)

    # write output to stdout
    if os.path.isfile(out_file):
        print('writing ' + out_file)
        with open(out_file, 'rb') as reader:
            return reader.read(), 200, {'ContentType': 'audio/mpeg'}
    else:
        return json.dumps({'error': 'file not produced'}), 510, {'ContentType': 'application/javascript'}


if __name__ == '__main__':
    logging.info("!!! RUNNING in TEST/DEBUG mode, not PRODUCTION !!!")
    app.run(port=8081)
