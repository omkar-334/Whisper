import os
import io
from openai import OpenAI
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from openai import OpenAI
import keyboard
from pathlib import Path
from playsound import playsound

# Set your OpenAI API key here
api_key = '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'
global client
client = OpenAI(api_key)

# Function to convert WAV to MP3
def convert_to_mp3(wav_file, mp3_file):
    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format="mp3")

# Function to transcribe audio
def transcribe_audio(mp3_file):
    global client
    with open(mp3_file, 'rb') as audio_file:
        audio = audio_file.read()
    audio_file = io.BytesIO(audio)
    with open(mp3_file, 'rb') as audio_file:
        transcript_response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcript_response

def record_audio(duration, fs):
    print("Recording... Press any key to stop")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    if keyboard.is_pressed():
        sd.stop()
    print("Recording ended")

    # Save recording to WAV file
    intermediate_file = 'output.wav'
    write(intermediate_file, fs, myrecording)

    # Convert WAV to MP3
    mp3_output_file = 'output.mp3'
    convert_to_mp3(intermediate_file, mp3_output_file)

    # Delete WAV file
    os.remove(intermediate_file)

    # Transcribe audio
    transcript_text = transcribe_audio(mp3_output_file)

    # Write transcription to a text file
    with open('transcription.txt', 'w') as text_file:
        text_file.write(transcript_text)

        

def send_gpt(transcription_file='transcription.txt', default_text="Hello!"):
    global client

    # Read the transcribed text from the file
    if os.path.exists(transcription_file):
        with open(transcription_file, 'r') as file:
            transcribed_text = file.read()
    else:
        print("Transcription file not found.")
        transcribed_text = default_text  # Default text if transcription is not available

    # Use the transcribed text as input for the chat model
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcribed_text}
        ]
    )

    # Return the chat model's response
    return completion.choices[0].message.content

def text_to_speech(text_input):
    speech_file_path = Path(__file__).parent / "speech.mp3"
        # Use OpenAI's API to convert text to speech and stream to file
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text_input
    )
    response.stream_to_file(str(speech_file_path))

    # Check if the file was created successfully
    if speech_file_path.exists():
        # Play the MP3 file
        playsound(str(speech_file_path))
    else:
        print("Error: File does not exist.")
        

duration = 100000
fs = 44100

record_audio(duration, fs)
response = send_gpt()
text_to_speech(response)
print(response)