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
    
    lyrics_timing = [
        (2.70,  "I'm lookin' back on things I've done"),
        (7.05,  "I never wanna play the same old part"),
        (11.98, "I'll keep you in the dark"),
        (16.38, "Now let me show you the shape of my heart"),
        (21.46, "Looking back on the things I've done"),
        (25.69, "I was trying to be someone"),
        (29.72, "I played my part, kept you in the dark"),
        (34.94, "Now let me show you the shape of my heart"),
        (42.41, "Looking back on the things I've done"),
        (45.56, "I was trying to be someone"),
        (49.86, "I played my part, kept you in the dark"),
        (54.76, "Now let me show you the shape of my heart"),
    ]
    
    print_slow(" Shape of My Heart - Backstreet Boys ", 0.08)
    print_slow("=" * 50, 0.02)
    
    start_time = time.time()
    
    for target_time, lyric in lyrics_timing:
        # Tunggu sampai waktu yang pas
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        
        print_slow(lyric, 0.08)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Backstreet Boys Forever!", 0.06)

if __name__ == "__main__":
    main()