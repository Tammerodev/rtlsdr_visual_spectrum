import tkinter as tk

import displaySpectrum

window = tk.Tk()
window.config(background="lightblue")
window.title("RTL-SDR Visual spectrum")
window.geometry("900x400")

input_lo_label = tk.Label(window, text="Start (MHz)", font=("Roboto", 18), background="lightblue")
input_lo_label.pack(anchor="w", padx=10)

input_lo = tk.Spinbox(window, from_= 1, to = 1700, width=4, increment=1,
    font=("Roboto", 18))
input_lo.pack(anchor="w", padx=10)

input_hi_label = tk.Label(window, text="Stop (MHz)", font=("Roboto", 18), background="lightblue")
input_hi_label.pack(anchor="w", padx=10)

input_hi = tk.Spinbox(window, from_= 1, to = 1700, width=4, increment=1,
    font=("Roboto", 18))
input_hi.pack(anchor="w", padx=10)

input_gain_label = tk.Label(window, text="Gain (dB)", font=("Roboto", 18), background="lightblue")
input_gain_label.pack(anchor="w", padx=10)

input_gain = tk.Spinbox(window, from_= 0, to = 49, width=4, increment=1,
    font=("Roboto", 18))
input_gain.pack(anchor="w", padx=10)

display_btn = tk.Button(
    window, text="Display spectrum", font=("Roboto", 18),
    command=lambda:displaySpectrum.displaySpectrum(input_lo.get(), input_hi.get(), input_gain.get()))
display_btn.pack()

while True:
    window.update()