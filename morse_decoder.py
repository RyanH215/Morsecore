# morse_decoder.py
import pyaudio
import numpy as np
import time

THRESHOLD = 500  # Volume threshold
SAMPLE_RATE = 44100
CHUNK = 1024

DOT_DASH_TIME = 0.2
GAP_TIME = 0.7
WORD_TIME = 1.5

MORSE_REVERSE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

def decode_morse_sequence(sequence):
    return ''.join(MORSE_REVERSE.get(code, '?') for code in sequence.strip().split(' '))

def listen_and_decode():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=SAMPLE_RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("Listening for Morse audio...")
    buffer = []
    symbol = ''
    last_sound_time = time.time()

    try:
        while True:
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            amplitude = np.max(np.abs(data))
            now = time.time()

            if amplitude > THRESHOLD:
                buffer.append(1)
                last_sound_time = now
            else:
                buffer.append(0)

            if now - last_sound_time > GAP_TIME:
                if buffer:
                    duration = len(buffer) / SAMPLE_RATE
                    if duration < DOT_DASH_TIME:
                        symbol += '.'
                    else:
                        symbol += '-'
                    buffer.clear()
                    print(f"Morse: {symbol}")
                    # Implement inter-letter and inter-word parsing as needed

    except KeyboardInterrupt:
        stream.stop_stream()
        stream.close()
        p.terminate()