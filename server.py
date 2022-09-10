#!/usr/bin/python3

import http.server
import socketserver
from urllib.parse import urlparse, unquote
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import uuid
import os

# usage: GET http://localhost:8080/?t=test%20me

# tts --text "$1" --model_name tts_models/en/vctk/vits --out_path test.wav --speaker_idx p343 > /dev/null
PORT = 8080

# load model manager
manager = ModelManager()

speakers_file_path = ""
language_ids_file_path = ""
vocoder_path = ""
vocoder_config_path = ""
encoder_path = ""
encoder_config_path = ""
use_cuda = False

model_path, config_path, model_item = manager.download_model("tts_models/en/vctk/vits")

# load models
synthesizer = Synthesizer(
    model_path,
    config_path,
    speakers_file_path,
    language_ids_file_path,
    vocoder_path,
    vocoder_config_path,
    encoder_path,
    encoder_config_path,
    use_cuda,
)

speaker_idx = "p343"
language_idx = ""
speaker_wav = None
reference_wav = None
capacitron_style_wav = None
capacitron_style_text = None
reference_speaker_idx = None


class TTSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # usage: GET http://localhost:8080/?t=test%20me
    def do_GET(self):
        query = urlparse(self.path).query
        if query is not None and (len(query) > 0 and "=" in query):
            parts = query.split("=")
            query_components = dict()
            query_components[parts[0]] = unquote(parts[1])
            if "t" not in query_components:
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"parameter t missing")
            else:
                # kick it
                wav = synthesizer.tts(
                    query_components["t"],
                    speaker_idx,
                    language_idx,
                    speaker_wav,
                    reference_wav=reference_wav,
                    style_wav=capacitron_style_wav,
                    style_text=capacitron_style_text,
                    reference_speaker_name=reference_speaker_idx,
                )
                out_filename = "/tmp/" + str(uuid.uuid4()) + ".wav"
                synthesizer.save_wav(wav, out_filename)
                with open(out_filename, 'rb') as reader:
                    self.send_response(200)
                    self.send_header('Content-type', 'audio/x-wav')
                    self.end_headers()
                    self.wfile.write(reader.read())
                os.remove(out_filename)
        else:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"parameter t=<text to speak> missing")


with socketserver.TCPServer(("", PORT), TTSHTTPRequestHandler) as httpd:
    print("TTS server on port", PORT)
    httpd.serve_forever()
