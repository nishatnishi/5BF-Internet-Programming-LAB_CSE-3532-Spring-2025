import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq
from dotenv import load_dotenv

# Step 1: Load environment variables from a .env file
load_dotenv()

# Step 2: Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 3: Record Audio
def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Save as MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred during audio recording: {e}")

# Step 4: Transcribe using GROQ
def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    try:
        if not GROQ_API_KEY:
            raise ValueError("Missing GROQ_API_KEY. Please set it in your environment.")

        client = Groq(api_key=GROQ_API_KEY)

        with open(audio_filepath, "rb") as audio_file:
            logging.info("Sending audio to GROQ for transcription...")
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )
            logging.info("Transcription received.")

            # Desired Output Format
            print(f"Transcription(text='{transcription.text}', x_groq={{'id': '{transcription.x_groq['id']}'}})")
            return transcription.text

    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        return None

# File path for audio
audio_filepath = "patient_voice_test_for_patient.mp3"

# Record audio (uncomment to use)
record_audio(audio_filepath)

# Transcribe
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Using os.getenv for environment variable access
stt_model = "whisper-large-v3"

# Call transcription
if GROQ_API_KEY:
    transcription = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
    if transcription:
        logging.info(f"Transcription: {transcription}")
    else:
        logging.error("Transcription failed.")
else:
    logging.error("GROQ_API_KEY not set. Please add it to your .env file.")
