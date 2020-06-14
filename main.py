from spleeter import *
from spleeter.separator import Separator


bitrate='320k'
outputDir = "./output"
inputFiles = []
backend='librosa'
config='spleeter:2stems-16kHz'
with open('./input.txt') as f:
    for line in f:
        inputFiles.append(line)

def doSeparate(separator, files, output):
    for file in files:
        separator.separate_to_file(audio_descriptor=file, destination=output, bitrate=bitrate)

separator = Separator(config, stft_backend=backend, multiprocess=False)
doSeparate(separator, inputFiles, outputDir)

