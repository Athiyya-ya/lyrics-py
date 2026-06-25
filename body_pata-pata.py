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
    
    print_slow("BODY PATA-PATA - FARIS ADAM, DIVA AUREL", 0.04)
    print_slow("=" * 55, 0.04)
    time.sleep(1.5)
    
    lyrics = [
        "Oh, Ade Nona, kanapa bagitu",
        "Cantik, manis, lucu-lucu?",
        "Bikin sa jadi candu",
        "Nona, ko boleh bikin sa jadi rindu, Sayang",
        "Sumpah mati, sa pikir de hampir jatuh (br-rah!)",
        "",
        "Sio Nona, body pata-pata, cantik jelita",
        "Ko bikin sa ni salah tingkah melulu",
        "Oh, Nona, body pata-pata, cantik jelita",
        "Sampe sa coba kejar ko buru-buru"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.070)
            time.sleep(0.5)
    
    print_slow("\n" + "=" * 55, 0.02)
   
if __name__ == "__main__":
    main()