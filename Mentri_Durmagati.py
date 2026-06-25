import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# SPEED CONTROL - Ganti ini!
BASE_SPEED = 0.045  # 0.03=super cepat, 0.06=lambat

def print_tune(line, multiplier=1.0):
    """Tuning fleksibel"""
    chars = len(line)
    speed = BASE_SPEED * multiplier
    for char in line:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()
    time.sleep(0.15 * multiplier)

def main():
    clear_screen()
    
    print_tune("MENTRI DURMAGATI - KAJAWI", 1.1)
    print("=" * 40)
    time.sleep(1.0)
    
    verse1 = [
        "  Kabeh nggawe ragad",
        "  Sangkuni paring warta", 
        "  Dana buta proyek negara",
        "  Kabeh kudu isa nanging aja sembrana",
        "  Ala saithik penting ra ketara"
    ]
    
    verse2 = [
        "  Iki proyek gedhe nanging aja nganti lali",
        "  Turahane dikanthongi Paman dibagehi",
        "  Sangkuni nagih janji yen gagal dikeplaki",
        "  Meeting bengi-bengi para-para mabuk whisky",
        "  Bancakan ingkunge gedhi semuanya happy",
        "  Karo gadis seksi si Limbuk Angelasari"
    ]
    
    verse3 = [
        "  Durmagati dadi menteri nata proyek nggo pribadi",
        "  Penting dadi kudu bathi tuku Ferrari",
        "  LSM-e disangoni anggaran kudu setiti",
        "  Mlebu kanthong metu mburi iki sing digoleki"
    ]
    
    # Verse 1
    for line in verse1:
        print_tune(line, 1.0)
    time.sleep(0.8)
    
    # Verse 2  
    for line in verse2:
        print_tune(line, 0.95)
    time.sleep(1.0)
    
    # Verse 3
    for line in verse3:
        print_tune(line, 0.92)
    
    print("=" * 40)
    print_tune("Kajawi", 1.1)

if __name__ == "__main__":
    main()