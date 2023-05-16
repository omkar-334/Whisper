# Whisper

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

## Approach

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.

## Setup

Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:

```
pip install openai-whisper
pip install git+https://github.com/openai/whisper.git 
pip install -r requirements.txt

```

To update the package to the latest version of this repository, please run:

```
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```

It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

**Requirements**

* for Whisper GUI - tk, customtkinter
* for OpenAI API - openai
* for Whisper_Gradio - transformers, gradio
* for Transciption accuracy - simphile, spacy, https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
