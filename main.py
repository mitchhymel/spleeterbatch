from spleeter import *
from spleeter.separator import Separator
from spleeter.utils import *
from spleeter.audio.adapter import get_default_audio_adapter

import json
with open('./input.json') as f:
    data = json.load(f)
    outputDir = data['outputDir']
    inputFiles = data['inputFiles']

def doSeparate(separator, files, output):
    for file in files:
        separator.separate_to_file(audio_descriptor=file, destination=output, bitrate='320k')

separator = Separator('spleeter:2stems-16kHz', stft_backend='librosa', multiprocess=False)
doSeparate(separator, inputFiles, outputDir)

