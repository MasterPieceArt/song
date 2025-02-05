import time
import sys

def print_lyrics():
    lyrics = [
        ["She", 0.1],
        ["said,", 0.1],
        ["Hola,", 0.3],
        ["¿cómo", 0.2],
        ["está'?", 0.7],
        ["", 0.0],  
        ["She", 0.1],
        ["said,", 0.1],
        ["こ", 0.2],
        ["ん", 0.2],
        ["に", 0.2],
        ["ち", 0.2],
        ["は", 0.5],
        ["", 0.0], 
        ["She", 0.3],
        ["said,", 0.2],
        ["Pardon", 0.2],
        ["my", 0.2],
        ["French", 0.2],
        ["", 0.2], 
        ["I", 0.2],
        ["said,", 0.4],
        ["Bonjour,", 0.4],
        ["madame", 0.4],
        ["", 0.0], 
        ["Then", 0.3],
        ["she", 0.2],
        ["said,", 0.3],
        ["Sak", 0.2],
        ["pasé?", 0.5],
        ["", 0.0],  
        ["And", 0.3],
        ["I", 0.3],
        ["said,", 0.2],
        ["N'ap", 0.2],
        ["boule", 0.5],
        ["", 0.0], 
        ["No", 0.2],
        ["matter", 0.2],
        ["where", 0.2],
        ["I", 0.2],
        ["go,", 0.5],
        ["you", 0.1],
        ["know", 0.2],
        ["I", 0.1],
        ["love", 0.2],
        ["'em", 0.2],
        ["all", 0.4],
        ["all", 0.3],
        ["all", 0.4],
    ]
    
    for word, delay in lyrics:
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(delay)
        if word == "":
            print("")  
    print("")  

if __name__ == "__main__":
    print_lyrics()