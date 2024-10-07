
import speech_recognition as sr
import pyttsx3
from ..ai_utils import send_request

def voice_command_handler():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    try:
        with sr.Microphone() as source:
            engine.say("Listening for your command...")
            engine.runAndWait()
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            engine.say(f"You said: {command}")
            engine.runAndWait()

            # Send the command to AI for processing
            messages = [{"role": "user", "content": command}]
            response = send_request(model_key="general", messages=messages)
            engine.say("AI Response: " + response.get("choices", [{}])[0].get("message", {}).get("content", ""))
            engine.runAndWait()

    except Exception as e:
        engine.say("Sorry, I could not understand your command.")
        engine.runAndWait()

if __name__ == "__main__":
    voice_command_handler()
