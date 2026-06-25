import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.055):  # Perfect untuk HONNE vibe
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("Location Unknown - HONNE ft. beka", 0.08)
    print_slow("=" * 60, 0.02)
    time.sleep(0.5)
    
    # HONNE TIMING - MILES AWAY VIBES! 
    lyrics_timing = [
        (0.52,  "My location unknown"),
        (2.26,  "Tryna find a way back home"),
        (4.49,  "To you again"),
        (5.99,  "I gotta get back to you"),
        (7.93,  "Gotta, gotta get back to you"),
        (10.80, "My location unknown"),
        (12.52, "Tryna find a way back home"),
        (14.60, "To you again"),
        (15.99, "I gotta get back to you"),
        (18.11, "Gotta, gotta get back to you"),
        (21.06, "I just need to know that you're safe"),
        (23.77, "Given that I'm miles away"),
        (26.47, "On the first flight"),
        (28.93, "Back to your side"),
        (31.21, "I don't care how long it takes"),
        (33.66, "I know you'll be worth the wait"),
        (36.93, "On the first flight"),
        (39.41, "Back to your side"),
    ]
    
    start_time = time.time()
    
    for target_time, lyric in lyrics_timing:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.055)
    
    print_slow("\n" + "=" * 60, 0.02)
    print_slow("HONNE & beabadoobee - Worth the wait!", 0.07)

if __name__ == "__main__":
    main()