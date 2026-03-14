import pyperclip as pycp

pycp.copy('The text to be copied to the clipboard.')
spam = pycp.paste()
if not pycp.is_available():

  print("Copy functionality unavailable!")

print(spam)
