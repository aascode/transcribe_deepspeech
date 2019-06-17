#!/usr/bin/env python3

'''
Author: Daniel M. Low
'''

import os
# file = './data/audio_examples/2830-3980-0043.wav'
# file = './data/audio_examples/hc_13802_p4_freeresp_trimmed_segmented_1_2.wav'
file = './data/audio_examples/se_10502_p1_sentences_trimmed.wav'
output_file=file[0:-4]+'.txt'
model_dir = './data/models/'
command = 'deepspeech --model {0}output_graph.pb --alphabet {0}alphabet.txt --lm {0}lm.binary --trie {0}trie --audio {1} >> {2}'.format(model_dir, file, output_file)
os.system(command)
transcript=open(output_file).read()
print('deepspeech transcript: '+transcript)

## Alternatively
import transcribe
# transcription_sphinx = transcribe.transcribe_sphinx(AUDIO_FILE)
# transcription_deepspeech = transcribe.transcribe_deepspeech(file)

