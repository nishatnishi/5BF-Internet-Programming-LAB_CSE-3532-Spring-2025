# voice_of_the_doctor.py

# Step 0: Load Environment Variables
from dotenv import load_dotenv
load_dotenv()  # Make sure .env file is in the same directory

# Step 1: Imports
import os
import subprocess
import platform
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

# Get ElevenLabs API Key from environment
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in environment variables. Check your .env file.")

# Step 2a: Text to Speech with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audio_obj = gTTS(text=input_text, lang=language, slow=False)
    audio_obj.save(output_filepath)
    play_audio(output_filepath)

# Step 2b: Text to Speech with ElevenLabs
def text_to_speech_with_elevenlabs(input_text, output_filepath, voice="Aria"):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    try:
        audio = client.generate(
            text=input_text,
            voice=voice,
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_filepath)
        play_audio(output_filepath)
    except Exception as e:
        print(f"[ERROR] ElevenLabs TTS failed: {e}")

# Step 3: Autoplay Audio
def play_audio(filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', filepath])  # You can replace with 'ffplay' or 'mpg123' if needed
        else:
            raise OSError("Unsupported operating system for audio playback.")
    except Exception as e:
        print(f"[ERROR] Unable to play audio: {e}")

# Step 4: Testing Both Methods
input_text = "Hi this is Ai with Nazrana!"

# Uncomment one to test:
# text_to_speech_with_gtts(input_text, "gtts_testing.mp3")
text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing.mp3", voice="Sarah")
