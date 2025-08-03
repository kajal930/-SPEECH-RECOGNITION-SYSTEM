import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print("🎧 Listening to the audio...")
            audio = recognizer.record(source)

            print("🔍 Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print("\n📝 Transcription:")
            print(text)

    except FileNotFoundError:
        print(f"❌ File not found at: {file_path}")
    except sr.UnknownValueError:
        print("⚠️ Audio was unclear or unintelligible.")
    except sr.RequestError as e:
        print(f"🚫 Could not request results from Google API: {e}")

# ✅ Correct audio file path (double-check extension)
file_path =r"C:\Users\LENEVO\Desktop\test\VS CODE\PYTHON\tell.wav"
transcribe_audio(file_path)

