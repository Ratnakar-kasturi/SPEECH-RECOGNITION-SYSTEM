import speech_recognition as sr
import time # Import time for small delays if needed

def transcribe_audio_from_mic_continuous():
    """
    Continuously captures audio from the microphone and transcribes it into text
    using Google's Web Speech API until a stop command is spoken.
    """
    r = sr.Recognizer()
    listening = True

    print("--- Speech-to-Text System Started ---")
    print("Say 'stop listening' to exit.")
    print("-----------------------------------")

    with sr.Microphone() as source:
        while listening:
            try:
                print("\nAdjusting for ambient noise... Please wait.")
                r.adjust_for_ambient_noise(source, duration=1)
                print("Say something now:")
                
                # Listen to the audio input from the microphone
                audio = r.listen(source, timeout=5, phrase_time_limit=8) # Added timeout and phrase_time_limit
                
                print("Transcribing...")
                text = r.recognize_google(audio, language="en-US")
                print(f"You said: \"{text}\"")

                # Check for a stop command
                if "stop listening" in text.lower() or "quit" in text.lower():
                    print("Stop command detected. Exiting...")
                    listening = False

            except sr.WaitTimeoutError:
                print("No speech detected for a while. Retrying...")
            except sr.UnknownValueError:
                print("Sorry, I could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                # If there's a persistent request error, it might be better to stop
                listening = False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                # For unexpected errors, consider stopping or logging
                listening = False
            
            time.sleep(0.5) # Short delay to prevent rapid re-prompting

    print("--- Transcription Session Ended ---")
    return "Session complete." # Return a status message

if __name__ == "__main__":
    transcribe_audio_from_mic_continuous()
