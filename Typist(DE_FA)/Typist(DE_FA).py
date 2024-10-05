import speech_recognition as sr
from pynput.keyboard import Controller, Listener, Key
import time

exit_program = False  # Flag to indicate whether to exit the program
stop_program = True  # Flag to control the loop
language_number = 0
def on_press(key):
    global exit_program, stop_program ,language_number  # Declare global variables to modify them
    if key == Key.esc:  # Check if the ESC key is pressed
        exit_program = True
    if key == Key.ctrl_r:  # Check if the Right Ctrl key is pressed
        print("\nYou can speak now.")
        stop_program = False  # Exit the inner loop
    if key == Key.shift_r:  # Correct comparison
        language_number = 1 if language_number == 0 else 0
        if language_number == 0:
            print("\nchange Language to Persian")
        else:
            print("\nChange language to Deutsch")

def listen_and_type():
    recognizer = sr.Recognizer()  # Create a speech recognizer
    microphone = sr.Microphone()  # Create a microphone for audio input
    keyboard = Controller()        # Create a keyboard controller

    with microphone as source:
        print("\nListening... (Press ESC to quit)")
        while not exit_program:
            audio = recognizer.listen(source)  # Record audio from the microphone
            try:
                # Convert the received audio to text
                if language_number == 0 :
                    text = recognizer.recognize_google(audio, language='fa-IR')
                else:
                    text = recognizer.recognize_google(audio, language='de-DE')
                print("\nYou said:", text)

                # Type the text wherever the focus is
                for char in text:
                    keyboard.press(char)     # Press the key
                    keyboard.release(char)   # Release the key
                    time.sleep(0.05)         # Shorter delay between key presses

                global stop_program
                stop_program = True  # Reset stop_program to True after each recognition
                print("\nPress the Ctrl key to exit waiting mode.")
                while stop_program:  # Loop until Ctrl is pressed
                    time.sleep(2)  # Small delay to avoid high CPU usage
                    # Here you can add more functionality if needed
                    
            except sr.UnknownValueError:
                print("\nI didn't understand that, please say it again.")
            except sr.RequestError:
                print("\nError connecting to the Google service.")

# Start the keyboard listener in a separate thread
listener = Listener(on_press=on_press)
listener.start()

# Adding time for preparation
time.sleep(3)
listen_and_type()

# Stop the listener when the program exits
listener.stop()

