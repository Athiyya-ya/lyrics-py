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

    print_slow("ASTAGA BERCANDA - AKBAR CHALAY & MINGSE", 0.09)
    print_slow("=" * 50, 0.02)

    lyrics = [
        (0.00, "Semua mua yang aku mau"),
        (3.11, "Ada padamu kok bisa gitu"),
        (7.10, "A a aduh pusing kepala"),
        (9.48, "CI cinta segitiga"),
        (11.05, "Ku mau mau aja"),
        (12.99, "Jadi Yang kedua"),
        (14.90, "Eh astaga bercanda"),
        (18.28, "Aku tunggu aja jadi yang pertama"),
        (22.28, "Astaga bercanda"),
        (25.90, "Kalau kau serius coba sekarang putus, eh"),
    ]

    start = time.time()

    for timestamp, line in lyrics:
        while time.time() - start < timestamp:
            time.sleep(0.01)

        print_slow("  " + line, 0.07)

    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Akbar Chalay & Mingse", 0.09)

if __name__ == "__main__":
    main()