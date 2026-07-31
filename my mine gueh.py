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

    print_slow("MY MINE GUEH - NAYKILLA", 0.09)
    print_slow("=" * 50, 0.02)

    lyrics = [
        (0.00, "Kamu itu my mine gueh"),
        (4.68, "Kamu bukan main-mainan gueh"),
        (8.84, "Kamu buat aku jadi pusing meleleh"),
        (12.22, "Pilih aku, pilih satu"),
        (14.91, "Yang lain enggak boleh"),
        (16.76, "Jalan-jalan cuma kita berdua"),
        (20.58, "Mau apa? Aku kasih semua"),
        (24.26, "Kubuat kamu jadi lupa rumah"),
        (28.32, "Kamu bisa panggil aku mamah"),
        (32.68, "Ini statement, aku yang paling baddie (Ah)"),
        (37.34, "Ini statement, aku cewek yang paling centil (Ah)"),
        (41.31, "Pake baju pasar, aku masih sabi (Ah)"),
        (45.54, "Buat cewe yang disana, jangan gampang menyerah"),
        (49.11, "Kamu bisa juga jadi kaya gua"),
    ]

    start = time.time()

    for timestamp, line in lyrics:
        while time.time() - start < timestamp:
            time.sleep(0.01)

        print_slow("  " + line, 0.07)

    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Naykilla", 0.09)

if __name__ == "__main__":
    main()