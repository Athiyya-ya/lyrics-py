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
    
    print_slow("STRONG - ONE DIRECTION", 0.04)
    print_slow("=" * 55, 0.04)
    time.sleep(1.5)
    
    lyrics = [
        "  You make me strong",
        "",
        "  I'm sorry if I say, (I need you)",
        "  But I don't care, I'm not scared of love",
        "  'Cause when I'm not with you I'm weaker",
        "  Is that so wrong?",
        "  Is it so wrong?",
        "  That you make me strong?"
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