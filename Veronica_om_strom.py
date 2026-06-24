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
    
    print_slow("VERONICA OM STROM - VERRY KLAU", 0.08)
    print_slow("=" * 50, 0.02)
    time.sleep(1)
    
    lyrics = [
        "Lu kenal Veronica ko?",
        "Veronica yang om Strom Pu Anak Nona Ni Ko",
        "Om Strom yang biasa, Tambal jalan lobang tu ko?",
        "",
        "Bukan yang itu, Tapi Mama Maria pu suami",
        "Na kasi kenal saya deng Veronica dulu",
        "Dia pu Mama suka laki-laki",
        "Bisa bahasa Inggris",
        "Bahasa Inggris kecil",
        "",
        "Coba satu kalimat",
        "Bluetooth device has connected successfully",
        "Pi ko Mama Maria kasi",
        "Kursus lu pake strom"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(0.8)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.5)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("Verry Klau", 0.09)

if __name__ == "__main__":
    main()