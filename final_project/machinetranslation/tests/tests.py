import sys
sys.path.append("..")
from translator import *

print("** Translate from English to French **: ")

print("Translate 'How are you' to french:")
print(english_to_french("How are you"))

print("Translate 'Car' to french:")
print(english_to_french("Car"))

print("Translate 'Hello' to french:")
print(english_to_french("Hello"))

print("-----------------------------------")

print("** Translate from French to English **: ")

print("Translate 'Comment allez-vous' to english:")
print(french_to_english("Comment allez-vous"))

print("Translate 'Voiture' to english:")
print(french_to_english("Voiture"))

print("Translate 'Bonjour' to english:")
print(french_to_english("Bonjour"))