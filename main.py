# main.py
from morse_encoder import text_to_morse
from morse_transmit import send_to_pico

PORT = "/dev/ttyACM0" # Update based on Pico's serial port

while True:
    msg = input("Type a message:")
    morse = text_to_morse(msg)
    print(f"Morse Code: {morse}")
    send_to_pico(PORT, morse)