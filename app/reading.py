
import pyaudio
import wave
from django.core.files.storage import FileSystemStorage
from os import listdir
from os.path import isfile, join
import threading
import os


class VoiceT(threading.Thread):
    def __init__(self):
        self.flag=0
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.flag=1
            print("Reading Chunks")
            while(self.flag):
                self.readchunks()
        except Exception as e:
            print(e)

    def stopread(self):
        self.flag=0

    def readchunks(self):
        # Record in chunks of 1024 samples
        chunk = 1024

        # 16 bits per sample
        sample_format = pyaudio.paInt16
        chanels = 2

        # Record at 44400 samples per second
        smpl_rt = 44400
        seconds = 1


        i=len([f for f in listdir('./media/chunks/') if isfile(join('./media/chunks/', f))])
        # for j in range(i):
        #     rm=r"./media/chunks/"+str(j)+".wav"
        #     os.remove(rm)   
        filename = "./media/chunks/"+str(i+1)+".wav"

        # Create an interface to PortAudio
        pa = pyaudio.PyAudio()

        stream = pa.open(format=sample_format, channels=chanels,
                        rate=smpl_rt, input=True,
                        frames_per_buffer=chunk)

        # Initialize array that be used for storing frames
        frames = []

        # Store data in chunks for 8 seconds
        for i in range(0, int(smpl_rt / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Terminate - PortAudio interface
        pa.terminate()

        # Save the recorded data in a .wav format
        sf = wave.open(filename, 'wb')
        sf.setnchannels(chanels)
        sf.setsampwidth(pa.get_sample_size(sample_format))
        sf.setframerate(smpl_rt)
        sf.writeframes(b''.join(frames))
        sf.close()




# def readchunks():
#     # Record in chunks of 1024 samples
#     chunk = 1024

#     # 16 bits per sample
#     sample_format = pyaudio.paInt16
#     chanels = 2

#     # Record at 44400 samples per second
#     smpl_rt = 44400
#     seconds = 4

#     i=len([f for f in listdir('./media/chunks/') if isfile(join('./media/chunks/', f))])
#     filename = "./media/chunks/"+str(i+1)+".wav"
#     print(i)
#     # Create an interface to PortAudio
#     pa = pyaudio.PyAudio()

#     stream = pa.open(format=sample_format, channels=chanels,
#                     rate=smpl_rt, input=True,
#                     frames_per_buffer=chunk)

#     # Initialize array that be used for storing frames
#     frames = []

#     # Store data in chunks for 8 seconds
#     for i in range(0, int(smpl_rt / chunk * seconds)):
#         data = stream.read(chunk)
#         frames.append(data)

#     # Stop and close the stream
#     stream.stop_stream()
#     stream.close()

#     # Terminate - PortAudio interface
#     pa.terminate()

#     # Save the recorded data in a .wav format
#     sf = wave.open(filename, 'wb')
#     sf.setnchannels(chanels)
#     sf.setsampwidth(pa.get_sample_size(sample_format))
#     sf.setframerate(smpl_rt)
#     sf.writeframes(b''.join(frames))
#     sf.close()
# # readchunks()