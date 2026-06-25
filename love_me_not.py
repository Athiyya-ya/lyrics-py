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
    
    print_slow("LOVE ME NOT - RAVYN LENAE", 0.09)
    print_slow("=" * 50, 0.02)
    time.sleep(1.2)
    
    lyrics = [
        "I need you right now, once I leave you I'm strung out",
        "If I get you, I'm slowly breaking down",
        "And, oh, it's hard to see you, but I wish you were right here",
        "Oh, it's hard to leave you when I get you everywhere",
        "",
        "All this time I'm thinking we could never be a pair",
        "Oh, no, I don't need you, but I miss you, come here"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.6)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Ravyn Lenae", 0.09)

if __name__ == "__main__":
    main()