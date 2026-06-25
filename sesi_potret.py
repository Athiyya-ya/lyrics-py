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
        (1.15,  "Sesi potret yang selalu ku benci"),
        (7.52,  "Aneh rasanya kau tak di sini"),
        (13.27, "Susunan barisannya tak sama lagi"),
        (17.40, "Oh ho ho satu dua tiga"),
        (22.90, "Ini nyata kau telah pergi"),
        (30.07, ""),
        (31.15, "Ku bertamu kerumah barumu"),
        (36.15, "Tak ada kamu"),
        (39.26, "Hanya papan dan namamu"),
        (42.83, "Mana ocehan wewangian khasmu"),
        (47.01, ""),
        (48.40, "Jarak ini terlalu jauh"),
        (51.54, "Kalau rindu aku tak mampu"),
        (55.10, "Sesal hatiku tak sempat temani kamu"),
        (60.16, "Harusnya kubisikan kata ajaib ke telingamu"),
        (66.81, "Soal ikhlas ternyata aku masih amatir"),
        (72.23, "Masih sangat amatir"),
    ]

    print_slow(" Sesi Potret - Ari Lesmana ", 0.08)
    print_slow("=" * 50, 0.02)

    start_time = time.time()

    for target_time, lyric in lyrics_timing:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.06)

    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Sesi Potret - Ari Lesmana", 0.06)

if __name__ == "__main__":
    main()