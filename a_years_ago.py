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
    
    print_slow("A YEAR AGO - JAMES ARTHUR", 0.09)
    print_slow("=" * 50, 0.02)
    time.sleep(1.3)
    
    lyrics = [
        "And now I'm just somebody you forgot",
        "I hope you're well",
        "Oh, and I can't help myself, oh, oh",
        "I wish it was a year ago",
        "I wish that I could hold you close",
        "",
        "Now I'm driving past your house",
        "I know the lights are on, you're not alone",
        "I wonder if you're making lies",
        "I wonder if he loves you like",
        "The way you said that only I could do",
        "",
        "I wish that I could tell you that I miss you",
        "I wish that I could tell you that I miss you"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.1)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.6)
    
    print_slow("\n" + "=" * 50, 0.02)
    print_slow("James Arthur", 0.09)

if __name__ == "__main__":
    main()