import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_precise(start_time, text, char_delay=0.075):
    """Ketikan effect pada waktu tepat"""
    chars = len(text)
    duration = chars * char_delay
    
    # Tunggu sampai start_time
    wait_time = start_time - time.time()
    if wait_time > 0:
        time.sleep(wait_time)
    
    # KETIKAN effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def main():
    clear_screen()
    global_start = time.time()
    
    print("BAHAGIA LAGI - PICHE KOTA")
    print("=" * 60)
    time.sleep(2.0)
    
    # TIMING LU + KETIKAN SUATU KALA NANTI!
    timings = [
        (5.79, "  Kupastikan kita bahagia lagi"),
        (11.10, "  Sampai kutemukan caraku untuk lupakanmu pergi dan hidup mati rasa"),
        (18.01, "  Pastikan aku untuk menunggumu sampai pada palung kecewa"),
        (22.73, "  Bila pada akhirnya kita menjadi asing pada kata bahagia"),
        (28.68, "  Sialnya, sayangnya, sialnya, aku akan tetap percaya"),
        (34.76, "  Suatu kala nanti")  
    ]
    
    for start_sec, line in timings:
        print_precise(global_start + start_sec, line, 0.075)
    
    print("\n" + "=" * 60)
    print("Piche Kota")

if __name__ == "__main__":
    main()