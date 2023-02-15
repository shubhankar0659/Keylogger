#libraries
import socket
import platform
import time 
import os
from scipy.io.wavfile import write
import sounddevice as sd


audio_information="audio.wav"
michrophone_time=10

def microphone():
    fs=44100
    seconds=michrophone_time

    myrecording = sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    write(audio_information, fs, myrecording)
 
microphone()
