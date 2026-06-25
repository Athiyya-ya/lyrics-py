import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_precise(start_time, text, char_delay=0.075):
    """Ketikan EXACT waktu lagu"""
    chars = len(text)
    
    # Wait sampai start_time
    wait_time = start_time - time.time()
    if wait_time > 0:
        time.sleep(wait_time)
    
    # Smooth ketikan
    for char in text:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def main():
    clear_screen()
    global_start = time.time()
    
    print("GHOST - JUSTIN BIEBER")
    print("=" * 60)
    time.sleep(0.3)
    
    # TIMING LU PERFECT!
    timings = [
        (0.57, "  Since the love that you left is all that I get, I want you to know"),
        (5.99, "  That if I can't be close to you"),
        (10.18, "  I'll settle for the ghost of you"),
        (13.93, "  I miss you more than life"),
        (18.33, "  And if you can't be next to me"),
        (22.35, "  Your memory is ecstasy"),
        (26.09, "  I miss you more than life"),
        (29.56, "  I miss you more than life")
    ]
    
    for start_sec, line in timings:
        print_precise(global_start + start_sec, line)
    
    print("\n" + "=" * 60)
    print("Justin Bieber")
    time.sleep(1)

if __name__ == "__main__":
    main()