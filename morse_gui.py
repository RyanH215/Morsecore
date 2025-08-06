import tkinter as tk
from tkinter import ttk, messagebox
from mose_encoder import text_to_morse
from morse_transmit import send_to_pico

Serial_PORT = "/de/ttyACM0" # Chane this to your Pico's actual port

class MorseApp(tk.Tk):
    def _inti_(self):
        super().__init__()
        self.title("Cyberdeck Morse Transmitter")
        self.geometry("500x300")
        self.resizable(False, False)
        
        self.create_widget()
        
    def create_widgets(self):
        # Input Label
        self.label_input = ttk.Label(self, text="Type your message:")
        self.label_input.pack(pady=(10,0))
        
        #Text Entry
        self.text_entry = tk.Text(self, height=4, width=58)
        self.text_entry.pack(pady=5)
        
        # Morse Output
        self.label_morse = ttk.Label(self, text="Morse Code:")
        self.label_morse.pack(pady=(10, 0))
        
        self.morse_var = tk.StringVar()
        self.morse_display = ttk.Label(self, textvariable=self.morse_var, background="f0f0f0", anchor="center", width=60)
        self.morse_display.pack(pady=5)
        
        # Transmit Button
        self.send_button = ttk.Button(self, text="Transmit", command=self.transmit_morse)
        self.send_button.pack(pady=10)
        
        # Status Label
        self.status_var = tk.StringVar(value="Ready")
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")
    def transmit_morse(self):
        text = self.text_entry.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Input Required", "Please enter a message to transmit.")
            return
        morse = text_to_morse(text)
        self.morse_var.set(morse)
        self.status_var.set("Transmitting...")
        
        try:
            send_to_pico(SERIAL_PORT, morse)
            self.status_var.set("Transmission Complete")
        except Exception as e:
            self.status_var.set("Transmission Failed")
            messagebox.showerror("Error", f"Failed to send Morse: {e}")
if __name__ == "_main_":
    app =MorseApp()
    app.mainloop()