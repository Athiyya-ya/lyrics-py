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
    
    print_slow("LAMPU KUNING - JUICY LUICY", 0.09)
    print_slow("=" * 45, 0.02)
    time.sleep(1.2)
    
    lyrics = [
        "Mengapa ku tancap gas dan melaju",
        "Padahal lampu kuning telah peringatkanku",
        "Bahaya di depanku",
        "Hati-hati kecewa kan menunggu",
        "Lagu lama yang aku tahu"
    ]
    
    for line in lyrics:
        print_slow("  " + line, 0.07)
        time.sleep(0.6)
    
    print_slow("\n" + "=" * 45, 0.02)
    print_slow("Juicy Luicy", 0.09)

if __name__ == "__main__":
    main()