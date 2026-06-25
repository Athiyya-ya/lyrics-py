import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.06):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("somebody's pleasure - Aziz Hedra", 0.04)
    print_slow("=" * 55, 0.04)
    time.sleep(1.5)
    
    lyrics = [
        "It was in a blink of an eye",
        "Find a way how to say goodbye",
        "I've got to take me away",
        "From all sadness",
        "Stitch all my wounds, confess all the sins (confess all the sins)",
        "",
        "And took all my insecure",
        "When will I got the love that is so pure?",
        "Gotta have to always make sure",
        "That I'm not just somebody's pleasure"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.070)
            time.sleep(0.5)
    
    print_slow("\n" + "=" * 55, 0.02)
   
if __name__ == "__main__":
    main()
