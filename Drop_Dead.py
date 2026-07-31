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

    print_slow("DROP DEAD - OLIVIA RODRIGO", 0.09)
    print_slow("=" * 50, 0.02)

    # (waktu dalam detik, lirik)
    lyrics = [
        (0.00, "Let's go steady"),
        (1.73, "Let's go out"),
        (3.04, "And tell the whole damn world how"),
        (4.30, "One night I was bored in bed"),
        (7.27, "And stalked you on the internet"),
        (10.89, "It's feminine intuition"),
        (14.20, "'Cuz I always had a vision of us standing like this"),
        (18.84, "All pressed up in the bathroom line"),
        (22.46, "You're looking like an angel on the walls of Versailles"),
        (26.45, "The most alive I've ever been"),
        (29.47, "But kiss me and I might")
    ]

    start = time.time()

    for timestamp, line in lyrics:
        while time.time() - start < timestamp:
            time.sleep(0.01)
        print_slow("  " + line, 0.07)

    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Olivia Rodrigo", 0.09)

if __name__ == "__main__":
    main()