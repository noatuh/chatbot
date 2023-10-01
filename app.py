import speech_recognition as sr
import pyttsx3

class VerbalChatbot:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Predefined responses
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm just a program, but I'm running smoothly!",
            "tell me something": "Did you know the moon is about 1/6th the size of Earth?",
            "bye": "Goodbye! It was nice chatting!"
        }

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = r.listen(source)
                return r.recognize_google(audio).lower().strip()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
                return None
            except sr.RequestError:
                print("API unavailable. Please check your internet connection.")
                return None
            except Exception as e:
                print("An error occurred:", str(e))
                return None

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print("An error occurred while trying to speak:", str(e))

    def chat(self):
        self.speak("Hello! Speak 'goodbye' to exit.")
        while True:
            user_input = self.listen()
            if user_input:
                print("You:", user_input)
                if user_input == "goodbye":
                    self.speak(self.responses.get("bye"))
                    break
                response = self.responses.get(user_input, "Sorry, I don't know that.")
                print("SimpleChatbot:", response)
                self.speak(response)
            else:
                self.speak("Sorry, I didn't catch that.")

# To start chatting
chatbot = VerbalChatbot()
chatbot.chat()
