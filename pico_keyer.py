#Load this with Thonny on your Pico
from machine import Pin
import time
import sys

tx = Pin(15, Pin.OUT)
DOT = 0.2
DASH = DOT * 3
INTRA = DOT
INTER = DOT * 3
WORD = DOT * 7

def key_down():
    tx.high()

def key_up():
    tx.low()

def play_morse(morse_code):
    for char in morse_code:
        if char == '.':
            key_down(); time.sleep(DOT); key_up()
        elif char == '-':
            key_down(); time.sleep(DASH); key_up()
        elif char == ' ':
            time.sleep(INTER)
        elif char == '/':
            time.sleep(WORD)
        time.sleep(INTRA)
print("Pico CW Keyer Ready")
while True:
    line = sys.stdin.readline()
    play_morse(line.strip())