import tkinter as tk
from googletrans import Translator

def translate_word(event=None):  # Event parameter is added with a default value None
    word = entry_word.get().strip()
    if word:
        translator = Translator()
        try:
            translated_text = translator.translate(word, dest='fa').text
            label_result.config(text=f"{translated_text}")
        except Exception as e:
            label_result.config(text=f"Translation failed: {e}")
    else:
        label_result.config(text="Please enter a word to translate.")

# Create the main window
root = tk.Tk()
root.title("Word Translator")

# Create and place widgets
label_word = tk.Label(root, text="Enter a word to translate:")
label_word.pack(pady=5)

entry_word = tk.Entry(root, width=30)
entry_word.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Bind the <Return> event to the translate_word function
entry_word.bind("<Return>", translate_word)

# Start the main event loop
root.mainloop()
