import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_precise(start_time, text, char_delay=0.075):
    """Ketikan presisi sesuai video"""
    chars = len(text)
    
    # Wait exact waktu
    wait_time = start_time - time.time()
    if wait_time > 0:
        time.sleep(wait_time)
    
    # Ketik natural
    for char in text:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def main():
    clear_screen()
    global_start = time.time()
    
    print("ORA URUS - TOTON CARIBO")
    print("=" * 70)
    time.sleep(0.2)
    
    # TIMING LU 100% AKRAT!
    timings = [
        (0.44, "  Sa bisa bikin rumah tangga stabil"),
        (3.87, "  Tinggal ko pilih mana baik, mana ganjil"),
        (7.55, "  Sa janji minggu depan lunasi angsuran"),
        (11.66, "  Kamis, Jumat, Sabtu, tapi sepi panggungan"),
        (16.20, "  Adoh, Sayang, yang penting bisa makan"),
        (18.69, "  Tetap bersyukur tong pu kekurangan"),
        (22.16, "  Ko tinggal tuduh, tuduh, tuduh, tuduh sa terus"),
        (26.93, "  Tuduh sa terus, tuduh sa terus"),
        (29.74, "  Kalau begitu, sekarang hidup ni ko yang urus"),
        (34.13, "  Hidup ni ko yang urus, sa cape, ora urus")
    ]
    
    for start_sec, line in timings:
        print_precise(global_start + start_sec, line)
    
    print("\n" + "=" * 70)
    print("Toton Caribo")

if __name__ == "__main__":
    main()