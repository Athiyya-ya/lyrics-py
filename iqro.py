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
        (1.00,  "Siapakah aku sebenarnya"),
        (7.88,  "Hanya atom yang kecil besar sombongnya"),
        (14.63, "Sampai di masa ini"),
        (17.78, "Ku masih mencari"),
        (21.77, "Tentang arti dunia"),
        (25.18, "Yang ramai nan sunyi"),
        (29.32, "Bantu aku berjalan menuju cahaya"),
        (37.01, "Lalu aku berjanji menjadi yang baik"),
    ]

    print_slow(" Iqro' - Raim Laode ", 0.08)
    print_slow("=" * 50, 0.02)

    start_time = time.time()

    for target_time, lyric in lyrics_timing:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.06)

    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Iqro' - Raim Laode", 0.06)

if __name__ == "__main__":
    main()