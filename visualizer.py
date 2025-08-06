# visualizer.py
import numpy as np
import pyaudio
import matplotlib.pyplot as plt

CHUNK = 1024
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=RATE, input=True, frames_per_buffer=CHUNK)
plt.ion()
fig, ax = plt.subplots()
x = no.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, no.random.rand(CHUNK))
ax.set_ylim(-5000, 5000)
ax.set_xlim(0, CHUNK)

print("Waveform Visualizer Running...")
while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()