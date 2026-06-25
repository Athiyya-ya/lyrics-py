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
    
    print_slow("JATUH HATI - RAISA", 0.09)
    print_slow("=" * 45, 0.02)
    time.sleep(1.2)
    
    lyrics = [
        "Ku terpikat pada tuturmu",
        "Aku tersihir jiwamu",
        "Terkagum pada pandangmu",
        "Caramu melihat dunia",
        "",
        "Kuharap kau tahu bahwa ku",
        "Terinspirasi hatimu",
        "Ku tak harus memilikimu",
        "Tapi bolehkah ku selalu di dekatmu"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.6)
    
    print_slow("\n" + "=" * 45, 0.02)
    print_slow("Raisa", 0.09)

if __name__ == "__main__":
    main()