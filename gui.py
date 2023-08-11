import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence


# Function to start the voice assistant
def start_voice_assistant():
    global voice_assistant_process
    if voice_assistant_process and voice_assistant_process.poll() is None:
        messagebox.showinfo("Voice Assistant",
                            "Voice assistant is already running!")
    else:
        print("Starting voice assistant...")
        voice_assistant_process = subprocess.Popen(["python", "avneet.py"])


# Function to quit the application
def quit_app():
    print("Quitting...")
    if voice_assistant_process:
        voice_assistant_process.terminate()
    window.destroy()


# Function to update the animation frame
def update_animation():
    global current_frame_index
    frame = animation_frames[current_frame_index]
    gif_label.config(image=frame)
    current_frame_index = (current_frame_index + 1) % len(animation_frames)
    window.after(100, update_animation)


# Create the GUI window
window = tk.Tk()
window.title("Personal Voice Assistant")
window.geometry("800x600")

# Load the GIF frames
animation_frames = []
gif_image = Image.open("voice.gif")
for frame in ImageSequence.Iterator(gif_image):
    # Use Image.LANCZOS for anti-aliasing
    frame = frame.resize((800, 600), Image.LANCZOS)
    frame = ImageTk.PhotoImage(frame)
    animation_frames.append(frame)

# Create a label to display the GIF frames
current_frame_index = 0
gif_label = tk.Label(window, width=800, height=600)
gif_label.pack()

# Start the animation
update_animation()

# Create a start button
start_button = tk.Button(
    window, text="Start Voice Assistant", command=start_voice_assistant, font=("Arial", 14)
)
start_button.place(x=20, y=20)

# Create a quit button
quit_button = tk.Button(
    window, text="Quit", command=quit_app, font=("Arial", 14)
)
quit_button.place(x=720, y=20)

# Initialize the voice assistant process variable
voice_assistant_process = None

# Run the GUI event loop
window.mainloop()
