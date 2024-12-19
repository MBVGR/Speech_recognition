import speech_recognition as sr

recognizer = sr.Recognizer()

print("Available Microphones: ")
mic_names = sr.Microphone.list_microphone_names()
for index, name in enumerate(mic_names):
    print(f"{index}: {name}")

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 4 seconds...")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done recording.")

try:
    print("Recognizing the text...")
    text = recognizer.recognize_google(recorded_audio, language="en-US")
    print("Decoded Text: {}".format(text))
except Exception as ex:
    print("Error recognizing speech: ", ex)
