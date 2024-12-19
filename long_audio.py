import os
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence

recognizer = sr.Recognizer()

def load_chunks(filename):
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1800,
        silence_thresh=-17
    )
    return audio_chunks

# Ensure the temporary directory exists or create it
temp_dir = './temp_audio_chunks/'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

for idx, audio_chunk in enumerate(load_chunks('./sample_audio/long_audio.mp3')):
    temp_file = os.path.join(temp_dir, f"chunk_{idx}.wav")
    audio_chunk.export(temp_file, format="wav")
    
    with sr.AudioFile(temp_file) as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Chunk {idx}: {text}")
        except Exception as ex:
            print(f"Error occurred with chunk {idx}: {ex}")

# Optionally, clean up temporary files
for temp_file in os.listdir(temp_dir):
    os.remove(os.path.join(temp_dir, temp_file))

print("++++++")