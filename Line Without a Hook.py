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
    
    print_slow("Line Without a Hook - Ricky Montgomery", 0.08)
    print_slow("=" * 50, 0.02)
    
    LYRICS = [
        (0.72,  "dancer"),
        (1.89,  "Watching over me, he's singing"),
        (5.15,  "\"She's a, she's a lady, and I am just a boy\""),
        (11.89, "He's singing, \"She's a, she's a lady, and I am just a line without a hook\""),
        (20.59, "Oh, baby, I am a wreck when I'm without you"),
        (26.46, "I need you here to stay"),
    ]
    
    start_time = time.time()
    
    for target_time, lyric in LYRICS:
        while (time.time() - start_time) < target_time:
            time.sleep(0.01)
        print_slow(lyric, 0.06)

if __name__ == "__main__":
    main()
