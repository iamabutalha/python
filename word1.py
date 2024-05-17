import time
from word import words
import sys

for word in words:
    if word == "aback":
        print(f"Found word {word}")
        time.sleep(1)
        
    else:
        print("Not found")
        time.sleep(1)
        

