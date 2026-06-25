import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("ABADI - PERUNGGU", 0.09)
    print_slow("=" * 50, 0.02)
    time.sleep(1.3)
    
    lyrics = [
        "Dinginnya hangatkanmu selalu",
        "Dilengkapi lapisan selimut",
        "Yang berupa dekapan nadi yang mengalir",
        "Menjadi seruan di hati",
        "Bermuarakan kabar baru",
        "",
        "Tentang mimpi berkecukupan",
        "Tanpa harus lembur lagi ke Gambir lagi",
        "Senin pagi dilanjut taksi tenangkanlah"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.1)
        else:
            print_slow("  " + line, 0.075)
            time.sleep(0.65)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Perunggu", 0.09)

if __name__ == "__main__":
    main()