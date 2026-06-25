import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.06):  # Lembut buat lagu Ghea
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("Manusia Paling Bahagia - Ghea Indah", 0.08)
    print_slow("=" * 55, 0.02)
    time.sleep(1)
    
    # GHEA TIMING - LANGIT JINGGA VIBES! 
    lyrics_timing = [
        (2.32,  "Kaubawakan bulan tepat di pangkuanku"),
        (6.64,  "Tawarkan rindu yang menjadi candu"),
        (11.68, "Canduku"),
        (16.30, "Tapi denganmu, langitku jingga"),
        (19.50, "Senyumku semekar bunga-bunga"),
        (23.90, "Apakah aku sedang di surga?"),
        (27.01, "Di surga, di surga"),
        (31.12, "Tapi denganmu, langitku jingga"),
        (35.53, "Senyumku semekar bunga-bunga"),
        (38.90, "Jadi manusia paling bahagia"),
        (43.74, "Bahagia, bahagia"),
    ]
    
    start_time = time.time()
    
    for target_time, lyric in lyrics_timing:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.06)
    
    print_slow("\n" + "=" * 55, 0.02)
    print_slow("Ghea Indah - Manusia Paling Bahagia!", 0.07)

if __name__ == "__main__":
    main()