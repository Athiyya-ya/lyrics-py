import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # Judul lagu
    print_slow("🎵 Shape of My Heart - Backstreet Boys 🎵", 0.08)
    print_slow("=" * 50, 0.02)
    time.sleep(1)
    
    # Lirik
    lyrics = [
        "I'm lookin' back on things I've done",
        "I never wanna play the same old part",
        "I'll keep you in the dark",
        "Now let me show you the shape of my heart",
        "",
        "Looking back on the things I've done",
        "I was trying to be someone",
        "I played my part, kept you in the dark",
        "Now let me show you the shape of my heart",
        "",
        "Looking back on the things I've done",
        "I was trying to be someone",
        "I played my part, kept you in the dark",
        "Now let me show you the shape of my heart"
    ]
    
    for line in lyrics:
        print_slow(line, 0.08)
        time.sleep(0.3)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Backstreet Boys Forever! 💙", 0.06)

if __name__ == "__main__":
    main()