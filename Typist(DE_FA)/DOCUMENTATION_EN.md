Filename: Typist(DE_FA).py
General Overview:
This program combines speech recognition with keyboard control. Using Google’s speech recognition service and a microphone, it converts the user’s voice into text and types the text wherever the keyboard is focused. The program is controlled using specific keyboard keys (ESC, Ctrl_R, Alt_R).

Libraries Used:
speech_recognition: For capturing and recognizing the user's speech.
pynput: For listening to and controlling keyboard inputs.
threading: For handling concurrency and synchronizing resources between threads.
time: For small delays to reduce CPU usage.
Variables:
exit_program: A flag to stop the program entirely. When ESC is pressed, it is set to True.
stop_program: Controls the internal loop of the program. Pressing Ctrl_R sets this flag to stop the loop.
language_number: A variable to switch between Persian (fa-IR) and German (de-DE) for speech recognition.
lock: A threading lock to prevent race conditions when accessing shared variables.
Functions:
1. on_press(key)
This function is called by the keyboard listener (pynput.Listener) and handles specific key presses:

ESC: Exits the program.
Ctrl_R: Stops the internal loop.
Alt_R: Switches the speech recognition language between Persian and German.
2. listen_and_type()
This function listens to the user’s speech and converts it into text. The recognized text is then typed using the pynput.keyboard.Controller at the current keyboard focus. This process repeats in a loop until ESC is pressed.

Program Control:
ESC: Exits the program entirely.
Ctrl_R: Stops the internal loop and allows listening to speech again.
Alt_R: Switches the speech recognition language between Persian and German.
Exceptions:
sr.UnknownValueError: Triggered when speech is not understood, displaying the message "I didn't understand that, please say it again."
sr.RequestError: Displays a relevant error message if there is an issue connecting to the Google service.
Explanation of Limitations:
Infinite Loop with Control Exit:
The infinite loop prevents the program from continuously sending requests to Google when the user is not speaking. This saves resources and avoids unnecessary network requests. By pressing Ctrl_R, you can stop the loop and prevent constant speech recognition requests.
Language Switching with Alt_R:
The need for switching languages with Alt_R is because Google's speech recognition service works differently for each language. Proper language selection ensures better word recognition accuracy. Switching between Persian and German ensures the service correctly identifies the user's speech.
