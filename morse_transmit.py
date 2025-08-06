#morese_transamit.py
import serial
import time

def send_to_pico(port, morse_code):
    with serial.Serial(port, 9600, timeout=1) as ser:
        ser.write(morse_code.encode('utf-8'))
        ser.write(b'\n') #Terminate with new line
        print("[TX} Morse code sent to Pico.")