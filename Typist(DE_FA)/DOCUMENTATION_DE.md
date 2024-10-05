Filename: Typist(DE_FA).py
Allgemeine Beschreibung:
Dieses Programm kombiniert Spracherkennung und Tastatursteuerung. Es verwendet den Google-Spracherkennungsdienst und ein Mikrofon, um die Sprache des Benutzers in Text umzuwandeln. Der erkannte Text wird dann an der Position der Tastaturfokussierung eingegeben. Über bestimmte Tastenkombinationen (ESC, Ctrl_R, Alt_R) kann das Programm gesteuert werden.

Verwendete Bibliotheken:
speech_recognition: Zum Erfassen und Erkennen der Sprache des Benutzers.
pynput: Zum Überwachen und Steuern der Tastatureingaben.
threading: Für die Verwaltung von Nebenläufigkeit (Concurrency) und die Synchronisierung zwischen Threads.
time: Für kleine Verzögerungen, um die CPU-Belastung zu reduzieren.
Variablen:
exit_program: Flag zur Beendigung des Programms. Wenn ESC gedrückt wird, wird dieser Wert auf True gesetzt.
stop_program: Steuert die interne Schleife des Programms. Wenn der Benutzer Ctrl_R drückt, wird diese Schleife gestoppt.
language_number: Variable zum Wechseln der Spracherkennung zwischen Persisch (fa-IR) und Deutsch (de-DE).
lock: Ein Lock zur Synchronisation von Threads, um Rennbedingungen zu vermeiden.
Funktionen:
1. on_press(key)
Diese Funktion wird vom Tastatur-Listener (pynput.Listener) aufgerufen und reagiert auf bestimmte Tastendrücke:

ESC: Beendet das Programm.
Ctrl_R: Stoppt die interne Schleife.
Alt_R: Wechselt die Sprache der Spracherkennung zwischen Persisch und Deutsch.
2. listen_and_type()
Diese Funktion hört auf die Sprache des Benutzers und wandelt sie in Text um. Der erkannte Text wird dann mit Hilfe des pynput.keyboard.Controller an der aktuellen Fokussierungsposition der Tastatur eingegeben. Dieser Prozess wird in einer Schleife fortgesetzt, bis ESC gedrückt wird.

Steuerung des Programms:
ESC: Beendet das Programm vollständig.
Ctrl_R: Beendet die innere Schleife und ermöglicht eine neue Spracherkennung.
Alt_R: Wechselt die Sprache der Spracherkennung zwischen Persisch und Deutsch.
Ausnahmen:
sr.UnknownValueError: Wird ausgegeben, wenn die Sprache nicht erkannt wird. Es erscheint die Nachricht: "Ich habe das nicht verstanden, bitte wiederholen."
sr.RequestError: Wenn die Verbindung zum Google-Dienst fehlschlägt, wird eine Fehlermeldung angezeigt.
Erklärung der Einschränkungen:
Endlose Schleife und Beenden mit Strg:
Die Endlosschleife wird verwendet, um zu verhindern, dass das Programm bei Pausen ständig Anfragen an den Google-Dienst sendet. Dies spart Ressourcen und vermeidet unnötige Netzwerkanfragen. Der Benutzer kann durch Drücken von Ctrl_R die Schleife anhalten und die Anfragepausen steuern.
Sprachwechsel mit Alt_R:
Der Grund für den Wechsel der Sprache mit Alt_R liegt darin, dass die Google-Spracherkennung für jede Sprache unterschiedlich funktioniert. Durch die Auswahl der richtigen Sprache kann die Genauigkeit der Erkennung erheblich verbessert werden. Zwischen Persisch und Deutsch wechselnd, sorgt der Dienst für präzisere Ergebnisse.
