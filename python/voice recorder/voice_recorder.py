import tkinter as tk
import sounddevice as sd
import numpy as np
import threading
import wave

class VoiceRecorder:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Voice Recorder")
        self.recording = False

        self.record_button = tk.Button(self.app, text="Start Recording", font=("Arial", 16), command=self.toggle_recording)
        self.record_button.pack(pady=10)

    def toggle_recording(self):
        if not self.recording:
            self.record_button.config(text="Stop Recording")
            self.recording = True
            self.start_recording_thread()
        else:
            self.record_button.config(text="Start Recording")
            self.recording = False

    def start_recording_thread(self):
        t = threading.Thread(target=self.record_audio)
        t.start()

    def record_audio(self):
        fs = 44100  # Sample rate
        duration = 5  # Recording duration (in seconds)

        # Record audio
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        # Save audio to a wave file
        wav_file = "recording.wav"
        with wave.open(wav_file, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(audio.tobytes())

        print("Recording saved to recording.wav")

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    recorder = VoiceRecorder()
    recorder.run()
