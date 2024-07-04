import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

class SpeechRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motivational Speech Recognizer")
        
        self.label = tk.Label(root, text="Press the button and say something motivational!", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.recognize_button = tk.Button(root, text="Recognize Speech", command=self.recognize_speech, font=("Arial", 14))
        self.recognize_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
        self.result_label.pack(pady=20)
    
    def recognize_speech(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        self.result_label.config(text="Listening...")
        self.root.update()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["success"] = False
            response["error"] = "Unable to recognize speech"
        
        if response["success"]:
            if response["transcription"]:
                self.result_label.config(text=f"You said: {response['transcription']}")
            else:
                self.result_label.config(text="I didn't catch that. Could you please repeat?")
        else:
            messagebox.showerror("Error", response["error"])

def main():
    root = tk.Tk()
    app = SpeechRecognizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
