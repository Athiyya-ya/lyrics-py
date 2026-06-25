import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_precise(start_time, text, char_delay=0.075):
    """Ketikan pada waktu EXACT"""
    chars = len(text)
    
    # Tunggu sampai start_time
    wait_time = start_time - time.time()
    if wait_time > 0:
        time.sleep(wait_time)
    
    # KETIKAN smooth
    for char in text:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def main():
    clear_screen()
    global_start = time.time()
    
    print("LANTAS - JUICY LUICY")
    print("=" * 60)
    time.sleep(0.5)
    
    # TIMING LU 100%!
    timings = [
        (0.85, "  Karena kau paling tahu"),
        (3.06, "  Cara lemahkan hatiku"),
        (5.99, "  Walau tak ada yang pasti"),
        (8.74, "  Yang kau beri hanya mimpi"),
        (12.44, "  Lantas mengapa ku masih menaruh hati"),
        (17.28, "  Padahal kutahu kau t'lah terikat janji"),
        (23.80, "  Keliru ataukah bukan tak tahu"),
        (29.91, "  Lupakanmu tapi aku tak mau")
    ]
    
    for start_sec, line in timings:
        print_precise(global_start + start_sec, line)
    
    print("\n" + "=" * 60)
    print("Juicy Luicy")
    time.sleep(1)

if __name__ == "__main__":
    main()