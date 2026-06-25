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
    
    print_slow("Esa X Perih - 510 (Vierratale)", 0.08)
    print_slow("=" * 50, 0.02)
    
    LYRICS = [
        (1.34,  "Kau buang aku tinggalkan diriku"),
        (8.39,  "Kau hancurkan aku seakan ku tak pernah ada"),
        (15.76, "Aku kan bertahan"),
        (19.15, "Mungkin takkan mungkin"),
        (24.13, "Menerjang kisahnya"),
        (27.40, "Walau perihwalau perih"),
        (32.61, "Aku kan bertahan"),
        (35.24, "Mungkin takkan mungkin"),
        (40.12, "Menerjang kisahnya"),
        (44.77, "Walau perihwalau perih"),
    ]
    
    start_time = time.time()
    
    for target_time, lyric in LYRICS:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.06)

if __name__ == "__main__":
    main()