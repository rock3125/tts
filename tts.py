#!/usr/bin/python3

import os
import sys
import logging
import subprocess

# add this path to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__' :

    # copy incoming text to say.txt
    with open('./say.txt', 'wb') as writer:
        writer.write(sys.stdin.buffer.read())

    # excute tts
    subprocess.run(['./run-uk.sh'])

    # write output to stdout
    with open('./output-uk.wav', 'rb') as reader:
        sys.stdout = os.fdopen(1, "wb")
        sys.stdout.write(reader.read())


