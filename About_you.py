import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.065):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("ABOUT YOU - THE 1975", 0.09)
    print_slow("=" * 40, 0.02)
    time.sleep(1.2)
    
    lyrics = [
        "I know a place",
        "It's somewhere I go when I need to remember your face",
        "We get married in our heads",
        "Something to do whilst we try to recall how we met",
        "",
        "Do you think I have forgotten?",
        "Do you think I have forgotten?",
        "Do you think I have forgotten about you?"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.6)
    
    print_slow("\n" + "=" * 40, 0.02)
    print_slow("The 1975", 0.09)

if __name__ == "__main__":
    main()