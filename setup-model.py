#!/usr/bin/python3

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

# load model manager
manager = ModelManager()
manager.download_model("tts_models/en/vctk/vits")
