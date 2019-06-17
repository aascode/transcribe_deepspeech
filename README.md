# transcribe

How to use deepspeech:

```
mkdir venv
cd venv
virtualenv deepspeech-venv
source deepspeech-venv/bin/activate
pip install -r path/to/requirements.txt
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.5.0/deepspeech-0.5.0-models.tar.gz #1.9 GB
tar xvfz deepspeech-0.5.0-models.tar.gz # Unzips
```
This will unzip ./models/ directory (or rename to "models"). You can put this within any other directory, including within the directory it was installed (for me: /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/deepspeech/) but I put it in ./data/ and you later need to reference the full path in the code (see audio_transcribe.py).

When you run deep speech you need to run something like audio_transcribe.py



