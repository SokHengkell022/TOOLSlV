# Kramer/Specter Deobf by KhanhNguyen9872
# file name: [atlastools.py] (py - 3.12)
# dump -> code 2

pass
'\nAtlasTools V1.0\nDeveloper: XNoctra\nCommunity: t.me/Atlas4Sec\n'
import os
import sys
import time
import json
import hashlib
import base64
import socket
import random
import re
import subprocess
import urllib.parse
import zlib
from datetime import datetime
from pathlib import Path
REQUIRED_MODULES = ['requests', 'pyfiglet', 'colorama']

def install_modules():
    pass
    import importlib
    import subprocess
    print('[*] Checking required modules...')
    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module.replace('-', '_').lower())
            print(f'[✓] {module} already installed')
        except ImportError:
            print(f'[!] Installing {module}...')
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
                print(f'[✓] {module} installed successfully')
            except:
                print(f'[✗] Failed to install {module}')
                return False
    return True
try:
    import requests
    from pyfiglet import Figlet
    from colorama import Fore, Back, Style, init
    import html
except ImportError:
    if install_modules():
        import requests
        from pyfiglet import Figlet
        from colorama import Fore, Back, Style, init
        import html
    else:
        print('[✗] Failed to install required modules. Exiting...')
        sys.exit(1)
init(autoreset=True)

class Colors:
    RED = Fore.LIGHTRED_EX
    GREEN = Fore.LIGHTGREEN_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BLUE = Fore.LIGHTBLUE_EX
    MAGENTA = Fore.LIGHTMAGENTA_EX
    CYAN = Fore.LIGHTCYAN_EX
    WHITE = Fore.LIGHTWHITE_EX
    RESET = Style.RESET_ALL

def typing_effect(text, delay=0.03):
    pass
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(text='Loading', duration=2):
    pass
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.CYAN}[{symbols[i % len(symbols)]}] {text}...{Colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f"\r{Colors.GREEN}[✓] {text} complete!{' ' * 20}")

def clear_screen():
    pass
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    pass
    clear_screen()
    gradient_colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    try:
        f = Figlet(font='slant')
        banner = f.renderText('AtlasTools')
    except:
        banner = '\n     █████╗ ████████╗██╗      █████╗ ███████╗\n    ██╔══██╗╚══██╔══╝██║     ██╔══██╗██╔════╝\n    ███████║   ██║   ██║     ███████║███████╗\n    ██╔══██║   ██║   ██║     ██╔══██║╚════██║\n    ██║  ██║   ██║   ███████╗██║  ██║███████║\n    ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝\n        '
    lines = banner.split('\n')
    for i, line in enumerate(lines):
        color_idx = int(i / len(lines) * (len(gradient_colors) - 1))
        print(gradient_colors[color_idx] + line)
    print(f"\n{Colors.CYAN}{'=' * 60}")
    print(f"{Colors.YELLOW}║ {'Version:':<15} {Colors.GREEN}V1.0{' ' * 35} {Colors.YELLOW} ")
    print(f"{Colors.YELLOW}║ {'Developer:':<15} {Colors.MAGENTA}XNoctra{' ' * 32} {Colors.YELLOW} ")
    print(f"{Colors.YELLOW}║ {'Community:':<15} {Colors.CYAN}t.me/Atlas4Sec{' ' * 27} {Colors.YELLOW}")
    print(f"{Colors.CYAN}{'=' * 60}\n")

class AtlasTools:

    def __init__(self):
        self.wordlist_dir = 'wordlists'
        Path(self.wordlist_dir).mkdir(exist_ok=True)

    def recon_basic(self):
        print(f'\n{Colors.CYAN}[1] BASIC RECONNAISSANCE')
        print(f"{Colors.YELLOW}{'-' * 40}")
        target = input(f'{Colors.GREEN}[?] Enter target (URL/IP): ').strip()
        if not target:
            print(f'{Colors.RED}[!] Target required')
            return
        loading_animation('Starting recon')
        try:
            if not target.startswith(('http://', 'https://')):
                target = 'http://' + target
            response = requests.get(target, timeout=10, headers={'User-Agent': 'AtlasTools/1.0'})
            print(f'\n{Colors.GREEN}[+] Headers:')
            for header, value in response.headers.items():
                print(f'    {Colors.CYAN}{header}: {Colors.WHITE}{value}')
        except Exception as e:
            print(f'{Colors.RED}[!] Header check failed: {e}')
        try:
            domain = target.split('//')[-1].split('/')[0]
            print(f'\n{Colors.GREEN}[+] Ping test for {domain}:')
            result = subprocess.run(['ping', '-c', '4', domain], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f'{Colors.RED}[!] Ping failed or timed out')
        except subprocess.TimeoutExpired:
            print(f'{Colors.RED}[!] Ping timeout')
        except:
            print(f'{Colors.RED}[!] Ping failed')
        try:
            print(f'\n{Colors.GREEN}[+] DNS Info:')
            ip = socket.gethostbyname(domain)
            print(f'    {Colors.CYAN}IP Address: {Colors.WHITE}{ip}')
        except:
            pass
        print(f'\n{Colors.GREEN}[+] Checking common admin panels...')
        admin_paths = ['/admin', '/wp-admin', '/admin/login', '/administrator', '/login', '/dashboard']
        for path in admin_paths:
            try:
                url = f"{target.rstrip('/')}{path}"
                resp = requests.head(url, timeout=5)
                if resp.status_code < 400:
                    print(f'    {Colors.YELLOW}[!] Found: {url} ({resp.status_code})')
            except:
                pass
        try:
            url = f"{target.rstrip('/')}/robots.txt"
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                print(f'\n{Colors.GREEN}[+] robots.txt found:')
                print(f'{Colors.CYAN}{resp.text[:500]}...')
        except:
            pass
        print(f'\n{Colors.GREEN}[+] Basic recon complete!')

    def hash_hunter(self):
        print(f'\n{Colors.CYAN}[2] HASH HUNTER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Hash Checker')
        print(f'{Colors.GREEN}[2] Wordlist Generator')
        print(f'{Colors.GREEN}[3] Indonesian Wordlist')
        print(f'{Colors.GREEN}[4] Hash Identifier')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            hash_input = input(f'{Colors.YELLOW}[?] Enter hash: ').strip()
            hash_type = input(f'{Colors.YELLOW}[?] Hash type (md5/sha1/sha256/sha512): ').strip().lower()
            wordlist = input(f'{Colors.YELLOW}[?] Wordlist path (enter for default): ').strip()
            if not wordlist:
                wordlist = f'{self.wordlist_dir}/indonesia.txt'
            if not os.path.exists(wordlist):
                print(f'{Colors.RED}[!] Wordlist not found, using built-in wordlist')
                words = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', 'admin']
            else:
                with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                    words = [line.strip() for line in f.readlines()]
            loading_animation('Cracking hash')
            for word in words:
                if hash_type == 'md5':
                    h = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    h = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    h = hashlib.sha256(word.encode()).hexdigest()
                elif hash_type == 'sha512':
                    h = hashlib.sha512(word.encode()).hexdigest()
                else:
                    print(f'{Colors.RED}[!] Invalid hash type')
                    return
                if h == hash_input:
                    print(f'\n{Colors.GREEN}[✓] Hash cracked!')
                    print(f'{Colors.CYAN}Hash: {Colors.WHITE}{hash_input}')
                    print(f'{Colors.CYAN}Value: {Colors.WHITE}{word}')
                    return
            print(f'\n{Colors.RED}[✗] Hash not found in wordlist')
        elif choice == '2':
            print(f'\n{Colors.GREEN}[+] Wordlist Generator')
            base_word = input(f'{Colors.YELLOW}[?] Base word: ').strip()
            output = input(f'{Colors.YELLOW}[?] Output file: ').strip()
            variants = []
            variants.append(base_word)
            variants.append(base_word.upper())
            variants.append(base_word.lower())
            variants.append(base_word.capitalize())
            variants.append(base_word + '123')
            variants.append(base_word + '123456')
            variants.append(base_word + '@123')
            variants.append('123' + base_word)
            variants.append(base_word + '!')
            variants.append(base_word + '2024')
            with open(output, 'w') as f:
                for var in variants:
                    f.write(var + '\n')
            print(f'{Colors.GREEN}[✓] Generated {len(variants)} variants to {output}')
        elif choice == '3':
            print(f'\n{Colors.GREEN}[+] Indonesian Wordlist')
            common_id = ['indonesia', 'jakarta', 'surabaya', 'bandung', 'bali', '123456', 'password', 'qwerty', 'admin', '12345', 'bismillah', 'allah', 'muhammad', 'sayang', 'cinta', 'ganteng', 'cantik', 'anjing', 'rahasia', 'indonesia123', 'jakarta123', 'surabaya123', 'bandung123', 'bali123', 'indonesia2024', 'password123', 'admin123', '123456789']
            output = f'{self.wordlist_dir}/indonesia.txt'
            with open(output, 'w', encoding='utf-8') as f:
                for word in common_id:
                    f.write(word + '\n')
            print(f'{Colors.GREEN}[✓] Indonesian wordlist created: {output}')
        elif choice == '4':
            print(f'\n{Colors.GREEN}[+] Hash Identifier')
            hash_input = input(f'{Colors.YELLOW}[?] Enter hash: ').strip()
            print(f'\n{Colors.CYAN}[+] Identifying hash type...')
            hash_len = len(hash_input)
            if hash_len == 32:
                print(f'{Colors.YELLOW}[!] Possible MD5 (32 chars)')
            elif hash_len == 40:
                print(f'{Colors.YELLOW}[!] Possible SHA1 (40 chars)')
            elif hash_len == 64:
                print(f'{Colors.YELLOW}[!] Possible SHA256 (64 chars)')
            elif hash_len == 128:
                print(f'{Colors.YELLOW}[!] Possible SHA512 (128 chars)')
            else:
                print(f'{Colors.RED}[!] Unknown hash type ({hash_len} chars)')

    def banner_scan(self):
        print(f'\n{Colors.CYAN}[3] BANNER SCANNER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        target = input(f'{Colors.GREEN}[?] Enter target (URL/IP): ').strip()
        if not target:
            print(f'{Colors.RED}[!] Target required')
            return
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        loading_animation('Scanning banners')
        try:
            response = requests.get(target, timeout=10)
            print(f'\n{Colors.GREEN}[+] Server Headers:')
            server = response.headers.get('Server', 'Not found')
            print(f'    {Colors.CYAN}Server: {Colors.WHITE}{server}')
            server_lower = server.lower()
            if 'apache' in server_lower:
                print(f'    {Colors.YELLOW}[!] Detected: Apache')
                if '2.2' in server_lower:
                    print(f'    {Colors.RED}[!] Warning: Old Apache version 2.2')
                elif '2.4' in server_lower:
                    print(f'    {Colors.GREEN}[✓] Apache 2.4 detected')
            elif 'nginx' in server_lower:
                print(f'    {Colors.YELLOW}[!] Detected: Nginx')
            elif 'iis' in server_lower:
                print(f'    {Colors.YELLOW}[!] Detected: Microsoft IIS')
            elif 'cloudflare' in server_lower:
                print(f'    {Colors.YELLOW}[!] Detected: Cloudflare')
            elif 'cloudfront' in server_lower:
                print(f'    {Colors.YELLOW}[!] Detected: AWS CloudFront')
            php_version = response.headers.get('X-Powered-By', 'Not found')
            print(f'    {Colors.CYAN}PHP: {Colors.WHITE}{php_version}')
            if 'x-aspnet-version' in response.headers:
                print(f"    {Colors.CYAN}ASP.NET: {Colors.WHITE}{response.headers['x-aspnet-version']}")
            if 'windows' in server_lower:
                print(f'    {Colors.CYAN}OS Guess: {Colors.WHITE}Windows Server')
            elif 'ubuntu' in server_lower:
                print(f'    {Colors.CYAN}OS Guess: {Colors.WHITE}Linux/Ubuntu')
            elif 'debian' in server_lower:
                print(f'    {Colors.CYAN}OS Guess: {Colors.WHITE}Linux/Debian')
            elif 'centos' in server_lower:
                print(f'    {Colors.CYAN}OS Guess: {Colors.WHITE}Linux/CentOS')
            elif 'redhat' in server_lower:
                print(f'    {Colors.CYAN}OS Guess: {Colors.WHITE}Linux/RedHat')
            print(f'\n{Colors.GREEN}[+] Security Headers:')
            security_headers = {'X-Frame-Options': 'Prevents clickjacking', 'X-Content-Type-Options': 'Prevents MIME sniffing', 'X-XSS-Protection': 'XSS protection', 'Content-Security-Policy': 'Content security policy', 'Strict-Transport-Security': 'HTTPS enforcement'}
            for header, description in security_headers.items():
                if header in response.headers:
                    print(f'    {Colors.GREEN}[✓] {header}: {response.headers[header]}')
                else:
                    print(f'    {Colors.RED}[✗] {header}: Missing')
        except Exception as e:
            print(f'{Colors.RED}[!] Error: {e}')

    def check_password_api(self, password: str):
        pass
        try:
            url = 'https://leakedpassword.com/api/'
            params = {'p': password}
            r = requests.get(url, params=params, timeout=10)
            if r.status_code != 200:
                return (None, 'API_ERROR')
            data = r.json().get('password', {})
            return (data, None)
        except Exception as e:
            return (None, str(e))

    def leak_checker(self):
        print(f'\n{Colors.CYAN}[4] LEAK CHECKER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Check single password')
        print(f'{Colors.GREEN}[2] Check multiple passwords from file')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            password = input(f'{Colors.YELLOW}[?] Enter password to check: ').strip()
            loading_animation('Checking password')
            result, error = self.check_password_api(password)
            if error:
                print(f'{Colors.RED}[!] Error checking password: {error}')
                return
            if result and result.get('leak'):
                print(f'\n{Colors.RED}[!] PASSWORD LEAKED!')
                print(f"{Colors.YELLOW}[!] Seen count : {result.get('seen')}")
                print(f"{Colors.CYAN}[+] Hash       : {result.get('hash')}")
                print(f'{Colors.GREEN}[+] Recommendation:')
                print(f'    - Change password immediately')
                print(f'    - Use strong & unique password')
                print(f'    - Enable 2FA')
            else:
                print(f'\n{Colors.GREEN}[✓] Password NOT found in leak database')
                if result:
                    print(f"{Colors.CYAN}[+] Hash: {result.get('hash')}")
        elif choice == '2':
            file_path = input(f'{Colors.YELLOW}[?] Enter file path with passwords: ').strip()
            if not os.path.exists(file_path):
                print(f'{Colors.RED}[!] File not found')
                return
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
            loading_animation(f'Checking {len(passwords)} passwords')
            leaked = []
            for pwd in passwords:
                result, error = self.check_password_api(pwd)
                if error:
                    continue
                if result and result.get('leak'):
                    leaked.append({'password': pwd, 'seen': result.get('seen'), 'hash': result.get('hash')})
            if leaked:
                print(f'\n{Colors.RED}[!] Found {len(leaked)} leaked passwords:')
                for item in leaked[:20]:
                    print(f"{Colors.RED}- {item['password']} | seen: {item['seen']}")
                if len(leaked) > 20:
                    print(f'{Colors.YELLOW}... and {len(leaked) - 20} more')
            else:
                print(f'\n{Colors.GREEN}[✓] No leaked passwords found')
        else:
            print(f'{Colors.RED}[!] Invalid choice')

    def encode_master(self):
        print(f'\n{Colors.CYAN}[5] ENCODE MASTER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Encode')
        print(f'{Colors.GREEN}[2] Decode')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice not in ['1', '2']:
            print(f'{Colors.RED}[!] Invalid choice')
            return
        print(f'\n{Colors.GREEN}[1] Base64')
        print(f'{Colors.GREEN}[2] Base32')
        print(f'{Colors.GREEN}[3] Hex')
        print(f'{Colors.GREEN}[4] URL Encoding')
        print(f'{Colors.GREEN}[5] ROT13')
        print(f'{Colors.GREEN}[6] Caesar Cipher')
        print(f'{Colors.GREEN}[7] Binary')
        print(f'{Colors.GREEN}[8] ASCII Code')
        method = input(f'\n{Colors.YELLOW}[?] Select method: ').strip()
        text = input(f'{Colors.YELLOW}[?] Enter text: ').strip()
        if choice == '1':
            if method == '1':
                result = base64.b64encode(text.encode()).decode()
            elif method == '2':
                result = base64.b32encode(text.encode()).decode()
            elif method == '3':
                result = text.encode().hex()
            elif method == '4':
                result = urllib.parse.quote(text)
            elif method == '5':
                result = self.rot13(text)
            elif method == '6':
                shift = input(f'{Colors.YELLOW}[?] Shift amount (1-25): ').strip()
                try:
                    result = self.caesar_cipher(text, int(shift))
                except ValueError:
                    print(f'{Colors.RED}[!] Invalid shift amount')
                    return
            elif method == '7':
                result = ' '.join((format(ord(c), '08b') for c in text))
            elif method == '8':
                result = ' '.join((str(ord(c)) for c in text))
            else:
                print(f'{Colors.RED}[!] Invalid method')
                return
            print(f'\n{Colors.GREEN}[✓] Encoded:')
            print(f'{Colors.CYAN}Result: {Colors.WHITE}{result}')
        else:
            if method == '1':
                try:
                    result = base64.b64decode(text.encode()).decode()
                except:
                    print(f'{Colors.RED}[!] Invalid Base64')
                    return
            elif method == '2':
                try:
                    result = base64.b32decode(text.encode()).decode()
                except:
                    print(f'{Colors.RED}[!] Invalid Base32')
                    return
            elif method == '3':
                try:
                    result = bytes.fromhex(text).decode()
                except:
                    print(f'{Colors.RED}[!] Invalid hex')
                    return
            elif method == '4':
                result = urllib.parse.unquote(text)
            elif method == '5':
                result = self.rot13(text)
            elif method == '6':
                shift = input(f'{Colors.YELLOW}[?] Shift amount (1-25): ').strip()
                try:
                    result = self.caesar_cipher(text, -int(shift))
                except ValueError:
                    print(f'{Colors.RED}[!] Invalid shift amount')
                    return
            elif method == '7':
                try:
                    result = ''.join((chr(int(b, 2)) for b in text.split()))
                except:
                    print(f'{Colors.RED}[!] Invalid binary')
                    return
            elif method == '8':
                try:
                    result = ''.join((chr(int(c)) for c in text.split()))
                except:
                    print(f'{Colors.RED}[!] Invalid ASCII codes')
                    return
            else:
                print(f'{Colors.RED}[!] Invalid method')
                return
            print(f'\n{Colors.GREEN}[✓] Decoded:')
            print(f'{Colors.CYAN}Result: {Colors.WHITE}{result}')

    def rot13(self, text):
        pass
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    def caesar_cipher(self, text, shift):
        pass
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    def port_scan_lite(self):
        print(f'\n{Colors.CYAN}[6] PORT SCAN LITE')
        print(f"{Colors.YELLOW}{'-' * 40}")
        target = input(f'{Colors.GREEN}[?] Enter target IP/hostname: ').strip()
        if not target:
            print(f'{Colors.RED}[!] Target required')
            return
        try:
            ip = socket.gethostbyname(target)
            print(f'{Colors.CYAN}[+] Target IP: {Colors.WHITE}{ip}')
        except:
            ip = target
            print(f'{Colors.YELLOW}[!] Using {ip} as target')
        print(f'\n{Colors.GREEN}[1] Quick scan (common ports)')
        print(f'{Colors.GREEN}[2] Custom range')
        print(f'{Colors.GREEN}[3] Single port')
        print(f'{Colors.GREEN}[4] Top 100 ports')
        choice = input(f'\n{Colors.YELLOW}[?] Select scan type: ').strip()
        ports = []
        if choice == '1':
            ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080, 8443]
        elif choice == '2':
            try:
                start = int(input(f'{Colors.YELLOW}[?] Start port: ').strip())
                end = int(input(f'{Colors.YELLOW}[?] End port: ').strip())
                ports = range(start, end + 1)
            except ValueError:
                print(f'{Colors.RED}[!] Invalid port numbers')
                return
        elif choice == '3':
            try:
                port = int(input(f'{Colors.YELLOW}[?] Port: ').strip())
                ports = [port]
            except ValueError:
                print(f'{Colors.RED}[!] Invalid port number')
                return
        elif choice == '4':
            ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
        else:
            print(f'{Colors.RED}[!] Invalid choice')
            return
        results = []
        open_ports = []
        print(f'\n{Colors.CYAN}[+] Scanning {len(ports)} ports on {ip}...\n')
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0:
                status = f'{Colors.GREEN}OPEN'
                open_ports.append(port)
                results.append({'port': port, 'status': 'open'})
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((ip, port))
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')[:100]
                    sock.close()
                    if banner.strip():
                        print(f'{status} Port {port:5d} - {banner.split(chr(10))[0]}')
                    else:
                        print(f'{status} Port {port:5d}')
                except:
                    print(f'{status} Port {port:5d}')
            else:
                print(f'{Colors.RED}[✗] Port {port:5d} - CLOSED')
                results.append({'port': port, 'status': 'closed'})
        print(f'\n{Colors.GREEN}[+] Scan complete!')
        print(f'{Colors.CYAN}Open ports: {Colors.WHITE}{len(open_ports)}')
        if open_ports:
            print(f'{Colors.CYAN}List: {Colors.WHITE}{sorted(open_ports)}')
        export = input(f'\n{Colors.YELLOW}[?] Export to JSON? (y/n): ').strip().lower()
        if export == 'y':
            filename = f"scan_{ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump({'target': target, 'ip': ip, 'timestamp': datetime.now().isoformat(), 'open_ports': open_ports, 'results': results}, f, indent=2)
            print(f'{Colors.GREEN}[✓] Results exported to {filename}')

    def link_inspector(self):
        print(f'\n{Colors.CYAN}[7] LINK INSPECTOR')
        print(f"{Colors.YELLOW}{'-' * 40}")
        url = input(f'{Colors.GREEN}[?] Enter URL to analyze: ').strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        loading_animation('Analyzing URL')
        try:
            response = requests.get(url, timeout=10, allow_redirects=False)
            print(f'\n{Colors.GREEN}[+] Basic Information:')
            print(f'    {Colors.CYAN}URL: {Colors.WHITE}{url}')
            print(f'    {Colors.CYAN}Status Code: {Colors.WHITE}{response.status_code}')
            print(f'    {Colors.CYAN}Content Length: {Colors.WHITE}{len(response.content)} bytes')
            print(f"    {Colors.CYAN}Content Type: {Colors.WHITE}{response.headers.get('Content-Type', 'Unknown')}")
            if 300 <= response.status_code < 400:
                location = response.headers.get('Location', '')
                print(f'    {Colors.YELLOW}[!] Redirects to: {location}')
                try:
                    redirect_resp = requests.get(url, timeout=10, allow_redirects=True)
                    print(f'    {Colors.CYAN}Final URL: {Colors.WHITE}{redirect_resp.url}')
                except:
                    pass
            tracking_params = ['utm_', 'fbclid', 'gclid', 'ref=', 'source=', 'campaign=', 'medium=', 'term=']
            parsed = urllib.parse.urlparse(url)
            query = urllib.parse.parse_qs(parsed.query)
            tracking_found = []
            for param in query.keys():
                for track in tracking_params:
                    if track in param.lower():
                        tracking_found.append(param)
            if tracking_found:
                print(f'\n{Colors.YELLOW}[!] Tracking parameters detected:')
                for param in tracking_found:
                    print(f'    {Colors.RED}- {param}')
            phishing_score = 0
            warnings = []
            if re.match('https?://\\d+\\.\\d+\\.\\d+\\.\\d+', url):
                phishing_score += 30
                warnings.append('IP address in URL')
            if '@' in url:
                phishing_score += 20
                warnings.append('@ symbol in URL (possible credential phishing)')
            if '--' in parsed.netloc:
                phishing_score += 10
                warnings.append('Multiple hyphens in domain')
            suspicious_tlds = ['.xyz', '.top', '.club', '.info', '.biz', '.tk', '.ml', '.ga', '.cf']
            for tld in suspicious_tlds:
                if parsed.netloc.endswith(tld):
                    phishing_score += 5
                    warnings.append(f'Suspicious TLD: {tld}')
            if not url.startswith('https://'):
                phishing_score += 15
                warnings.append('No HTTPS (insecure connection)')
            if len(parsed.netloc) > 50:
                phishing_score += 10
                warnings.append('Very long domain name')
            if warnings:
                print(f'\n{Colors.RED}[!] Security Warnings:')
                for warning in warnings:
                    print(f'    {Colors.RED}- {warning}')
            print(f'\n{Colors.GREEN}[+] Security Assessment:')
            if phishing_score > 50:
                print(f'    {Colors.RED}[!] HIGH RISK: Potential phishing site (Score: {phishing_score}/100)')
                print(f'    {Colors.YELLOW}[!] Recommendation: Do not enter any personal information!')
            elif phishing_score > 30:
                print(f'    {Colors.YELLOW}[!] MEDIUM RISK: Be cautious (Score: {phishing_score}/100)')
                print(f'    {Colors.CYAN}[!] Verify the website before entering sensitive data')
            elif phishing_score > 10:
                print(f'    {Colors.BLUE}[!] LOW RISK: Some issues found (Score: {phishing_score}/100)')
            else:
                print(f'    {Colors.GREEN}[✓] LOW RISK: Appears safe (Score: {phishing_score}/100)')
        except Exception as e:
            print(f'{Colors.RED}[!] Error: {e}')

    def txt_tools(self):
        print(f'\n{Colors.CYAN}[8] TEXT TOOLS')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] JSON Beautify')
        print(f'{Colors.GREEN}[2] JSON Minify')
        print(f'{Colors.GREEN}[3] HTML Escape/Unescape')
        print(f'{Colors.GREEN}[4] Remove Duplicates')
        print(f'{Colors.GREEN}[5] Sort Lines')
        print(f'{Colors.GREEN}[6] Merge Wordlists')
        print(f'{Colors.GREEN}[7] Text Statistics')
        print(f'{Colors.GREEN}[8] Find and Replace')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            json_input = input(f'{Colors.YELLOW}[?] Enter JSON string or file path: ').strip()
            if os.path.exists(json_input):
                try:
                    with open(json_input, 'r') as f:
                        json_input = f.read()
                except:
                    print(f'{Colors.RED}[!] Error reading file')
                    return
            try:
                parsed = json.loads(json_input)
                print(f'\n{Colors.GREEN}[✓] Formatted JSON:')
                print(json.dumps(parsed, indent=2))
                save = input(f'\n{Colors.YELLOW}[?] Save to file? (y/n): ').strip().lower()
                if save == 'y':
                    filename = input(f'{Colors.YELLOW}[?] Filename: ').strip()
                    with open(filename, 'w') as f:
                        json.dump(parsed, f, indent=2)
                    print(f'{Colors.GREEN}[✓] Saved to {filename}')
            except json.JSONDecodeError as e:
                print(f'{Colors.RED}[!] Invalid JSON: {e}')
            except:
                print(f'{Colors.RED}[!] Invalid JSON')
        elif choice == '2':
            json_input = input(f'{Colors.YELLOW}[?] Enter JSON string or file path: ').strip()
            if os.path.exists(json_input):
                try:
                    with open(json_input, 'r') as f:
                        json_input = f.read()
                except:
                    print(f'{Colors.RED}[!] Error reading file')
                    return
            try:
                parsed = json.loads(json_input)
                print(f'\n{Colors.GREEN}[✓] Minified JSON:')
                minified = json.dumps(parsed, separators=(',', ':'))
                print(minified)
                print(f'\n{Colors.CYAN}Size reduction: {len(json_input)} -> {len(minified)} chars')
            except:
                print(f'{Colors.RED}[!] Invalid JSON')
        elif choice == '3':
            text = input(f'{Colors.YELLOW}[?] Enter text: ').strip()
            action = input(f'{Colors.YELLOW}[?] (E)scape or (U)nescape? ').strip().lower()
            if action == 'e':
                result = html.escape(text)
                print(f'\n{Colors.GREEN}[✓] Escaped HTML:')
                print(result)
            elif action == 'u':
                result = html.unescape(text)
                print(f'\n{Colors.GREEN}[✓] Unescaped HTML:')
                print(result)
            else:
                print(f'{Colors.RED}[!] Invalid choice')
        elif choice == '4':
            file_path = input(f'{Colors.YELLOW}[?] Enter file path: ').strip()
            if not os.path.exists(file_path):
                print(f'{Colors.RED}[!] File not found')
                return
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            unique_lines = list(set(lines))
            output = input(f'{Colors.YELLOW}[?] Output file (enter for same file): ').strip()
            if not output:
                output = file_path
            with open(output, 'w', encoding='utf-8') as f:
                f.writelines(unique_lines)
            removed = len(lines) - len(unique_lines)
            print(f'{Colors.GREEN}[✓] Removed {removed} duplicates. {len(unique_lines)} unique lines saved.')
        elif choice == '5':
            file_path = input(f'{Colors.YELLOW}[?] Enter file path: ').strip()
            if not os.path.exists(file_path):
                print(f'{Colors.RED}[!] File not found')
                return
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            lines.sort()
            output = input(f'{Colors.YELLOW}[?] Output file (enter for same file): ').strip()
            if not output:
                output = file_path
            with open(output, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f'{Colors.GREEN}[✓] Sorted {len(lines)} lines.')
        elif choice == '6':
            files = input(f'{Colors.YELLOW}[?] Enter file paths (comma separated): ').strip().split(',')
            files = [f.strip() for f in files]
            all_lines = []
            for file in files:
                if os.path.exists(file):
                    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                        all_lines.extend(f.readlines())
                else:
                    print(f'{Colors.YELLOW}[!] File not found: {file}')
            unique_lines = list(set(all_lines))
            output = input(f'{Colors.YELLOW}[?] Output file: ').strip()
            with open(output, 'w', encoding='utf-8') as f:
                f.writelines(unique_lines)
            print(f'{Colors.GREEN}[✓] Merged {len(all_lines)} lines, {len(unique_lines)} unique saved to {output}')
        elif choice == '7':
            text = input(f'{Colors.YELLOW}[?] Enter text or file path: ').strip()
            if os.path.exists(text):
                try:
                    with open(text, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()
                except:
                    print(f'{Colors.RED}[!] Error reading file')
                    return
            print(f'\n{Colors.GREEN}[+] Text Statistics:')
            print(f'    {Colors.CYAN}Characters: {Colors.WHITE}{len(text)}')
            print(f'    {Colors.CYAN}Words: {Colors.WHITE}{len(text.split())}')
            print(f'    {Colors.CYAN}Lines: {Colors.WHITE}{text.count(chr(10)) + 1}')
            print(f'    {Colors.CYAN}Unique characters: {Colors.WHITE}{len(set(text))}')
            print(f'    {Colors.CYAN}Whitespace characters: {Colors.WHITE}{sum((1 for c in text if c.isspace()))}')
            freq = {}
            for char in text:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            print(f'\n{Colors.CYAN}Top 5 most common characters:')
            sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
            for char, count in sorted_freq:
                char_display = repr(char)[1:-1]
                print(f"    {Colors.WHITE}'{char_display}': {count} times")
        elif choice == '8':
            file_path = input(f'{Colors.YELLOW}[?] Enter file path: ').strip()
            if not os.path.exists(file_path):
                print(f'{Colors.RED}[!] File not found')
                return
            find_text = input(f'{Colors.YELLOW}[?] Text to find: ').strip()
            replace_text = input(f'{Colors.YELLOW}[?] Text to replace with: ').strip()
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            new_content = content.replace(find_text, replace_text)
            replacements = content.count(find_text)
            output = input(f'{Colors.YELLOW}[?] Output file (enter for same file): ').strip()
            if not output:
                output = file_path
            with open(output, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'{Colors.GREEN}[✓] Made {replacements} replacements in {output}')
        else:
            print(f'{Colors.RED}[!] Invalid choice')

    def wordlist_forge(self):
        print(f'\n{Colors.CYAN}[9] WORDLIST FORGE')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Name-based generator')
        print(f'{Colors.GREEN}[2] Date-based generator')
        print(f'{Colors.GREEN}[3] Hobby-based generator')
        print(f'{Colors.GREEN}[4] Phone number generator')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            first_name = input(f'{Colors.YELLOW}[?] First name: ').strip()
            last_name = input(f'{Colors.YELLOW}[?] Last name: ').strip()
            nickname = input(f'{Colors.YELLOW}[?] Nickname: ').strip()
            words = []
            if first_name:
                words.extend([first_name, first_name.lower(), first_name.upper()])
            if last_name:
                words.extend([last_name, last_name.lower(), last_name.upper()])
            if nickname:
                words.extend([nickname, nickname.lower(), nickname.upper()])
            if first_name and last_name:
                words.append(first_name + last_name)
                words.append(first_name.lower() + last_name.lower())
                words.append(first_name[0] + last_name)
                words.append(first_name + last_name[0])
                words.append(first_name + '.' + last_name)
                words.append(first_name + '_' + last_name)
            base_words = words.copy()
            for word in base_words:
                for year in range(1970, 2024):
                    words.append(word + str(year))
                    words.append(word + str(year)[2:])
                for i in range(100):
                    words.append(word + str(i).zfill(2))
                    words.append(word + str(i))
            output = f'{self.wordlist_dir}/name_{first_name}_{last_name}.txt'
        elif choice == '2':
            day = input(f'{Colors.YELLOW}[?] Day (DD): ').strip()
            month = input(f'{Colors.YELLOW}[?] Month (MM): ').strip()
            year = input(f'{Colors.YELLOW}[?] Year (YYYY): ').strip()
            words = []
            if day and month and year:
                words.append(f'{day}{month}{year}')
                words.append(f'{day}{month}{year[2:]}')
                words.append(f'{year}{month}{day}')
                words.append(f'{year[2:]}{month}{day}')
                words.append(f'{day}/{month}/{year}')
                words.append(f'{day}-{month}-{year}')
                words.append(f'{month}{day}{year}')
                words.append(f'{month}{day}{year[2:]}')
                words.append(f'{year}-{month}-{day}')
            output = f'{self.wordlist_dir}/date_{day}_{month}_{year}.txt'
        elif choice == '3':
            hobbies = input(f'{Colors.YELLOW}[?] Hobbies (comma separated): ').strip().split(',')
            hobbies = [h.strip() for h in hobbies]
            words = []
            for hobby in hobbies:
                words.append(hobby)
                words.append(hobby.lower())
                words.append(hobby.upper())
                words.append(hobby.capitalize())
                for i in range(100):
                    words.append(hobby + str(i))
                    words.append(hobby + str(i).zfill(2))
                    words.append(hobby + '_' + str(i))
            output = f'{self.wordlist_dir}/hobbies.txt'
        elif choice == '4':
            prefix = input(f'{Colors.YELLOW}[?] Phone prefix (e.g., 0812, 0857): ').strip()
            if not prefix:
                prefix = '08'
            words = []
            for i in range(10000):
                number = f'{prefix}{str(i).zfill(8 - len(prefix))}'
                words.append(number)
            output = f'{self.wordlist_dir}/phone_{prefix}.txt'
        else:
            print(f'{Colors.RED}[!] Invalid choice')
            return
        with open(output, 'w', encoding='utf-8') as f:
            for word in set(words):
                f.write(word + '\n')
        print(f'{Colors.GREEN}[✓] Generated {len(set(words))} words to {output}')

    def ascii_art_tools(self):
        print(f'\n{Colors.CYAN}[10] ASCII ART TOOLS')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Text to ASCII Art')
        print(f'{Colors.GREEN}[2] Generate Pattern')
        print(f'{Colors.GREEN}[3] Banner Creator')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            text = input(f'{Colors.YELLOW}[?] Enter text: ').strip()
            try:
                f = Figlet(font='standard')
                ascii_art = f.renderText(text)
                print(f'\n{Colors.GREEN}[✓] ASCII Art:\n')
                print(ascii_art)
                save = input(f'\n{Colors.YELLOW}[?] Save to file? (y/n): ').strip().lower()
                if save == 'y':
                    filename = input(f'{Colors.YELLOW}[?] Filename: ').strip()
                    with open(filename, 'w') as f:
                        f.write(ascii_art)
                    print(f'{Colors.GREEN}[✓] Saved to {filename}')
            except:
                print(f'\n{Colors.GREEN}[✓] Simple ASCII Art:\n')
                border = '=' * (len(text) + 4)
                print(border)
                print(f'| {text} |')
                print(border)
        elif choice == '2':
            print(f'\n{Colors.GREEN}[+] ASCII Patterns')
            patterns = [('Checkerboard', '##  ##  \n  ##  ##\n##  ##  \n  ##  ##'), ('Diagonal', '#     \n  #   \n    # \n      #'), ('Border', '┌────┐\n│    │\n│    │\n└────┘'), ('Heart', ' ♥ ♥ \n♥   ♥\n ♥ ♥ \n  ♥  '), ('Smiley', '  🙂  \n /|\\ \n / \\ ')]
            for i, (name, pattern) in enumerate(patterns, 1):
                print(f'\n{Colors.CYAN}[{i}] {name}:')
                print(pattern)
        elif choice == '3':
            print(f'\n{Colors.GREEN}[+] Banner Creator')
            text = input(f'{Colors.YELLOW}[?] Banner text: ').strip()
            width = int(input(f'{Colors.YELLOW}[?] Width (default 40): ').strip() or '40')
            border = '=' * width
            padding = (width - len(text) - 4) // 2
            if padding < 0:
                padding = 0
            banner = f"\n{border}\n|{' ' * (width - 2)}|\n|{' ' * padding} {text} {' ' * (width - padding - len(text) - 3)}|\n|{' ' * (width - 2)}|\n{border}\n            "
            print(f'\n{Colors.GREEN}[✓] Created banner:')
            print(banner)
        else:
            print(f'{Colors.RED}[!] Invalid choice')

    def osint_lite(self):
        print(f'\n{Colors.CYAN}[11] OSINT LITE')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] Username pattern generator')
        print(f'{Colors.GREEN}[2] Email pattern generator')
        print(f'{Colors.GREEN}[3] Social media formats')
        print(f'{Colors.GREEN}[4] Profile URL checker')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            username = input(f'{Colors.YELLOW}[?] Base username: ').strip()
            patterns = [username, username.lower(), username.upper(), username + '123', username + '123456', 'real' + username, 'the' + username, username + 'official', username + '_', '_' + username, username + '.', '.' + username, username + str(random.randint(100, 999)), username[0] * 3 + username, username + username, username + 'x', 'x' + username]
            print(f'\n{Colors.GREEN}[✓] Generated username patterns:')
            for i, pattern in enumerate(patterns, 1):
                print(f'    {Colors.CYAN}{i:2d}. {pattern}')
        elif choice == '2':
            first_name = input(f'{Colors.YELLOW}[?] First name: ').strip()
            last_name = input(f'{Colors.YELLOW}[?] Last name: ').strip()
            domain = input(f'{Colors.YELLOW}[?] Domain (e.g., gmail.com): ').strip()
            patterns = [f'{first_name}.{last_name}@{domain}', f'{first_name}{last_name}@{domain}', f'{first_name}_{last_name}@{domain}', f'{first_name[0]}{last_name}@{domain}', f'{first_name}{last_name[0]}@{domain}', f'{first_name}.{last_name[0]}@{domain}', f'{first_name[0]}.{last_name}@{domain}', f'{first_name}@{domain}', f'{last_name}.{first_name}@{domain}', f'{first_name}{random.randint(10, 99)}@{domain}', f'{last_name}{random.randint(10, 99)}@{domain}']
            print(f'\n{Colors.GREEN}[✓] Generated email patterns:')
            for i, pattern in enumerate(patterns, 1):
                print(f'    {Colors.CYAN}{i:2d}. {pattern}')
        elif choice == '3':
            print(f'\n{Colors.GREEN}[+] Social Media URL Formats:')
            platforms = {'Instagram': 'https://instagram.com/{username}', 'Twitter/X': 'https://twitter.com/{username}', 'Facebook': 'https://facebook.com/{username}', 'LinkedIn': 'https://linkedin.com/in/{username}', 'GitHub': 'https://github.com/{username}', 'YouTube': 'https://youtube.com/@{username}', 'TikTok': 'https://tiktok.com/@{username}', 'Reddit': 'https://reddit.com/user/{username}', 'Telegram': 'https://t.me/{username}', 'Pinterest': 'https://pinterest.com/{username}'}
            for platform, pattern in platforms.items():
                print(f'\n{Colors.CYAN}{platform}:')
                print(f'    {Colors.WHITE}{pattern}')
            print(f'\n{Colors.YELLOW}[!] Note: Replace {{username}} with actual username')
        elif choice == '4':
            username = input(f'{Colors.YELLOW}[?] Username to check: ').strip()
            platforms = {'Instagram': f'https://instagram.com/{username}', 'Twitter': f'https://twitter.com/{username}', 'GitHub': f'https://github.com/{username}', 'Reddit': f'https://reddit.com/user/{username}'}
            print(f'\n{Colors.GREEN}[+] Checking profile URLs...')
            for platform, url in platforms.items():
                try:
                    response = requests.head(url, timeout=5, allow_redirects=True)
                    if response.status_code == 200:
                        print(f'{Colors.GREEN}[✓] {platform}: {url}')
                    elif response.status_code == 404:
                        print(f'{Colors.RED}[✗] {platform}: Not found')
                    else:
                        print(f'{Colors.YELLOW}[?] {platform}: Status {response.status_code}')
                except:
                    print(f'{Colors.RED}[!] {platform}: Connection failed')
        else:
            print(f'{Colors.RED}[!] Invalid choice')

    def env_scanner(self):
        print(f'\n{Colors.CYAN}[12] ENVIRONMENT SCANNER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        directory = input(f'{Colors.GREEN}[?] Directory to scan (enter for current): ').strip()
        if not directory:
            directory = '.'
        if not os.path.exists(directory):
            print(f'{Colors.RED}[!] Directory not found')
            return
        loading_animation(f'Scanning {directory}')
        sensitive_patterns = {'API_KEY': '(?i)(api[_-]?key|apikey)[=:]\\s*["\\\']?([a-zA-Z0-9_-]{20,})["\\\']?', 'SECRET_KEY': '(?i)(secret[_-]?key|secretkey)[=:]\\s*["\\\']?([a-zA-Z0-9_-]{20,})["\\\']?', 'PASSWORD': '(?i)(password|passwd|pwd)[=:]\\s*["\\\']?([^\\s"\\\']{6,})["\\\']?', 'TOKEN': '(?i)(token|access[_-]?token)[=:]\\s*["\\\']?([a-zA-Z0-9_-]{20,})["\\\']?', 'DATABASE_URL': '(?i)(database[_-]?url|db[_-]?url)[=:]\\s*["\\\']?(mongodb|mysql|postgresql|redis)://[^\\s"\\\']+["\\\']?', 'AWS_KEY': '(?i)(aws[_-]?(access[_-]?key|secret[_-]?key))[=:]\\s*["\\\']?([A-Z0-9]{20,})["\\\']?', 'PRIVATE_KEY': '-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----', 'CREDIT_CARD': '\\b(?:\\d[ -]*?){13,16}\\b', 'EMAIL': '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'}
        findings = []
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv']]
            for file in files:
                if file == '.env' or file.endswith('.env.example'):
                    filepath = os.path.join(root, file)
                    findings.append(f'{Colors.YELLOW}[!] Found env file: {filepath}')
                if file.endswith(('.py', '.js', '.json', '.yml', '.yaml', '.config', '.conf', '.ini', '.txt', '.env', '.php')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            for pattern_name, pattern in sensitive_patterns.items():
                                matches = re.findall(pattern, content)
                                if matches:
                                    for match in matches:
                                        if isinstance(match, tuple):
                                            value = match[1]
                                        else:
                                            value = match
                                        hidden_value = value[:10] + '...' + value[-5:] if len(value) > 20 else value
                                        findings.append(f'{Colors.RED}[!] {pattern_name} found in {filepath}: {hidden_value}')
                    except:
                        continue
        if findings:
            print(f'\n{Colors.RED}[!] SECURITY FINDINGS ({len(findings)}):')
            for finding in findings[:20]:
                print(f'    {finding}')
            if len(findings) > 20:
                print(f'    {Colors.YELLOW}... and {len(findings) - 20} more findings')
            save = input(f'\n{Colors.YELLOW}[?] Save findings to file? (y/n): ').strip().lower()
            if save == 'y':
                filename = f"env_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    f.write(f'Environment Scan Results - {directory}\n')
                    f.write(f'Scan date: {datetime.now()}\n')
                    f.write('=' * 50 + '\n\n')
                    for finding in findings:
                        f.write(finding + '\n')
                print(f'{Colors.GREEN}[✓] Findings saved to {filename}')
        else:
            print(f'\n{Colors.GREEN}[✓] No sensitive data found in {directory}')

    def simple_crypt(self):
        print(f'\n{Colors.CYAN}[13] SIMPLE CRYPTOGRAPHY')
        print(f"{Colors.YELLOW}{'-' * 40}")
        print(f'{Colors.GREEN}[1] XOR Encrypt/Decrypt')
        print(f'{Colors.GREEN}[2] Hash Generator')
        print(f'{Colors.GREEN}[3] Text Obfuscator')
        print(f'{Colors.GREEN}[4] Simple Caesar Cipher')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        if choice == '1':
            text = input(f'{Colors.YELLOW}[?] Enter text: ').strip()
            key = input(f'{Colors.YELLOW}[?] Encryption key: ').strip()
            if not key:
                print(f'{Colors.RED}[!] Key required')
                return
            result = []
            key_bytes = key.encode()
            for i, char in enumerate(text):
                result.append(chr(ord(char) ^ key_bytes[i % len(key_bytes)]))
            encrypted = ''.join(result)
            print(f'\n{Colors.GREEN}[✓] XOR Result:')
            print(f'{Colors.CYAN}Original: {Colors.WHITE}{text}')
            print(f'{Colors.CYAN}Key: {Colors.WHITE}{key}')
            print(f'{Colors.CYAN}Result: {Colors.WHITE}{encrypted}')
            print(f'{Colors.CYAN}Hex: {Colors.WHITE}{encrypted.encode().hex()}')
            print(f'{Colors.CYAN}Base64: {Colors.WHITE}{base64.b64encode(encrypted.encode()).decode()}')
        elif choice == '2':
            text = input(f'{Colors.YELLOW}[?] Enter text to hash: ').strip()
            print(f'\n{Colors.GREEN}[+] Hash Results:')
            hashes = {'MD5': hashlib.md5(text.encode()).hexdigest(), 'SHA1': hashlib.sha1(text.encode()).hexdigest(), 'SHA256': hashlib.sha256(text.encode()).hexdigest(), 'SHA512': hashlib.sha512(text.encode()).hexdigest(), 'SHA3-256': hashlib.sha3_256(text.encode()).hexdigest() if hasattr(hashlib, 'sha3_256') else 'N/A', 'BLAKE2b': hashlib.blake2b(text.encode()).hexdigest() if hasattr(hashlib, 'blake2b') else 'N/A'}
            for name, value in hashes.items():
                print(f'{Colors.CYAN}{name}: {Colors.WHITE}{value}')
        elif choice == '3':
            text = input(f'{Colors.YELLOW}[?] Enter text to obfuscate: ').strip()
            print(f'\n{Colors.GREEN}[+] Obfuscation Options:')
            print(f'{Colors.CYAN}1. HTML Entities')
            print(f'{Colors.CYAN}2. Unicode Escape')
            print(f'{Colors.CYAN}3. Base64 Encoding')
            print(f'{Colors.CYAN}4. Reverse Text')
            opt = input(f'{Colors.YELLOW}[?] Select method: ').strip()
            if opt == '1':
                result = ''.join((f'&#{ord(c)};' for c in text))
                print(f'{Colors.CYAN}HTML Entities: {Colors.WHITE}{result}')
            elif opt == '2':
                result = ''.join((f'\\u{ord(c):04x}' for c in text))
                print(f'{Colors.CYAN}Unicode Escape: {Colors.WHITE}{result}')
            elif opt == '3':
                result = base64.b64encode(text.encode()).decode()
                print(f'{Colors.CYAN}Base64: {Colors.WHITE}{result}')
            elif opt == '4':
                result = text[::-1]
                print(f'{Colors.CYAN}Reversed: {Colors.WHITE}{result}')
            else:
                print(f'{Colors.RED}[!] Invalid option')
        elif choice == '4':
            text = input(f'{Colors.YELLOW}[?] Enter text: ').strip()
            action = input(f'{Colors.YELLOW}[?] (E)ncrypt or (D)ecrypt? ').strip().lower()
            shift = int(input(f'{Colors.YELLOW}[?] Shift amount (1-25): ').strip())
            result = []
            for char in text:
                if 'a' <= char <= 'z':
                    base = ord('a')
                    if action == 'e':
                        result.append(chr((ord(char) - base + shift) % 26 + base))
                    else:
                        result.append(chr((ord(char) - base - shift) % 26 + base))
                elif 'A' <= char <= 'Z':
                    base = ord('A')
                    if action == 'e':
                        result.append(chr((ord(char) - base + shift) % 26 + base))
                    else:
                        result.append(chr((ord(char) - base - shift) % 26 + base))
                else:
                    result.append(char)
            print(f'\n{Colors.GREEN}[✓] Result:')
            print(f'{Colors.CYAN}Original: {Colors.WHITE}{text}')
            print(f'{Colors.CYAN}Shift: {Colors.WHITE}{shift}')
            print(f"{Colors.CYAN}Result: {Colors.WHITE}{''.join(result)}")
        else:
            print(f'{Colors.RED}[!] Invalid choice')

    def log_reader(self):
        print(f'\n{Colors.CYAN}[14] LOG READER')
        print(f"{Colors.YELLOW}{'-' * 40}")
        log_file = input(f'{Colors.GREEN}[?] Log file path: ').strip()
        if not os.path.exists(log_file):
            print(f'{Colors.RED}[!] File not found')
            return
        print(f'\n{Colors.GREEN}[1] View with error highlighting')
        print(f'{Colors.GREEN}[2] Filter by keyword')
        print(f'{Colors.GREEN}[3] Extract errors only')
        print(f'{Colors.GREEN}[4] Search for IP addresses')
        print(f'{Colors.GREEN}[5] Count lines by severity')
        choice = input(f'\n{Colors.YELLOW}[?] Select option: ').strip()
        try:
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            if choice == '1':
                print(f'\n{Colors.CYAN}[+] Log file: {log_file}')
                print(f"{Colors.YELLOW}{'=' * 80}")
                for i, line in enumerate(lines, 1):
                    line = line.rstrip()
                    line_lower = line.lower()
                    if any((error in line_lower for error in ['error', 'exception', 'critical', 'fatal', 'panic'])):
                        color = Colors.RED
                    elif any((warn in line_lower for warn in ['warn', 'alert', 'notice'])):
                        color = Colors.YELLOW
                    elif 'debug' in line_lower:
                        color = Colors.CYAN
                    elif 'info' in line_lower:
                        color = Colors.BLUE
                    elif 'success' in line_lower or 'completed' in line_lower:
                        color = Colors.GREEN
                    else:
                        color = Colors.WHITE
                    print(f'{color}[{i:4d}] {line}')
            elif choice == '2':
                keyword = input(f'{Colors.YELLOW}[?] Filter keyword: ').strip().lower()
                print(f"\n{Colors.CYAN}[+] Lines containing '{keyword}':")
                print(f"{Colors.YELLOW}{'=' * 80}")
                count = 0
                for i, line in enumerate(lines, 1):
                    if keyword in line.lower():
                        print(f'{Colors.CYAN}[{i:4d}] {line.strip()}')
                        count += 1
                print(f'\n{Colors.GREEN}[✓] Found {count} matches')
            elif choice == '3':
                error_lines = []
                for i, line in enumerate(lines, 1):
                    line_lower = line.lower()
                    if any((error in line_lower for error in ['error', 'exception', 'critical', 'fatal', 'panic'])):
                        error_lines.append((i, line.strip()))
                if error_lines:
                    print(f'\n{Colors.RED}[+] ERROR LOGS ({len(error_lines)}):')
                    print(f"{Colors.YELLOW}{'=' * 80}")
                    for i, line in error_lines[:50]:
                        print(f'[{i:4d}] {line}')
                    if len(error_lines) > 50:
                        print(f'\n{Colors.YELLOW}[!] Showing first 50 of {len(error_lines)} errors')
                else:
                    print(f'{Colors.GREEN}[✓] No errors found in log file')
            elif choice == '4':
                print(f'\n{Colors.CYAN}[+] Searching for IP addresses...')
                ip_pattern = '\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b'
                ip_count = {}
                for i, line in enumerate(lines, 1):
                    ips = re.findall(ip_pattern, line)
                    for ip in ips:
                        if ip in ip_count:
                            ip_count[ip] += 1
                        else:
                            ip_count[ip] = 1
                if ip_count:
                    print(f'\n{Colors.GREEN}[+] Found {len(ip_count)} unique IP addresses:')
                    sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
                    for ip, count in sorted_ips[:20]:
                        print(f'    {Colors.CYAN}{ip:<15} - {Colors.WHITE}{count} occurrences')
                    if len(ip_count) > 20:
                        print(f'    {Colors.YELLOW}... and {len(ip_count) - 20} more IPs')
                else:
                    print(f'{Colors.YELLOW}[!] No IP addresses found')
            elif choice == '5':
                print(f'\n{Colors.CYAN}[+] Counting lines by severity...')
                counts = {'error': 0, 'warning': 0, 'info': 0, 'debug': 0, 'other': 0}
                for line in lines:
                    line_lower = line.lower()
                    if any((error in line_lower for error in ['error', 'exception', 'critical', 'fatal', 'panic'])):
                        counts['error'] += 1
                    elif any((warn in line_lower for warn in ['warn', 'alert', 'notice'])):
                        counts['warning'] += 1
                    elif 'info' in line_lower:
                        counts['info'] += 1
                    elif 'debug' in line_lower:
                        counts['debug'] += 1
                    else:
                        counts['other'] += 1
                total = sum(counts.values())
                print(f'\n{Colors.GREEN}[+] Log Statistics:')
                print(f'    {Colors.CYAN}Total lines: {Colors.WHITE}{total}')
                print(f"    {Colors.RED}Errors: {counts['error']} ({counts['error'] / total * 100:.1f}%)")
                print(f"    {Colors.YELLOW}Warnings: {counts['warning']} ({counts['warning'] / total * 100:.1f}%)")
                print(f"    {Colors.BLUE}Info: {counts['info']} ({counts['info'] / total * 100:.1f}%)")
                print(f"    {Colors.CYAN}Debug: {counts['debug']} ({counts['debug'] / total * 100:.1f}%)")
                print(f"    {Colors.WHITE}Other: {counts['other']} ({counts['other'] / total * 100:.1f}%)")
            else:
                print(f'{Colors.RED}[!] Invalid choice')
        except Exception as e:
            print(f'{Colors.RED}[!] Error reading log: {e}')

def main():
    tools = AtlasTools()
    while True:
        display_banner()
        print(f'{Colors.MAGENTA}MAIN MENU:')
        print(f"{Colors.CYAN}{'=' * 60}")
        menu_items = ['Recon Basic', 'Hash Hunter', 'Banner Scan', 'Leak Checker', 'Encode Master', 'Port Scan Lite', 'Link Inspector', 'Text Tools', 'Wordlist Forge', 'ASCII Art Tools', 'OSINT Lite', 'Environment Scanner', 'Simple Cryptography', 'Log Reader', 'Exit']
        for i, item in enumerate(menu_items, 1):
            color = Colors.GREEN if i <= 14 else Colors.RED
            print(f'{color}[{i:2d}] {item}')
        print(f"{Colors.CYAN}{'=' * 60}")
        try:
            choice = input(f'\n{Colors.YELLOW}[?] Select option (1-15): ').strip()
            if choice == '1':
                tools.recon_basic()
            elif choice == '2':
                tools.hash_hunter()
            elif choice == '3':
                tools.banner_scan()
            elif choice == '4':
                tools.leak_checker()
            elif choice == '5':
                tools.encode_master()
            elif choice == '6':
                tools.port_scan_lite()
            elif choice == '7':
                tools.link_inspector()
            elif choice == '8':
                tools.txt_tools()
            elif choice == '9':
                tools.wordlist_forge()
            elif choice == '10':
                tools.ascii_art_tools()
            elif choice == '11':
                tools.osint_lite()
            elif choice == '12':
                tools.env_scanner()
            elif choice == '13':
                tools.simple_crypt()
            elif choice == '14':
                tools.log_reader()
            elif choice == '15':
                print(f'\n{Colors.GREEN}[✓] Thank you for using AtlasTools!')
                print(f'{Colors.CYAN}[+] Join our community: t.me/Atlas4Sec')
                print(f'{Colors.MAGENTA}[+] Developer: XNoctra')
                print(f'{Colors.YELLOW}[+] Goodbye! 👋')
                time.sleep(2)
                break
            else:
                print(f'{Colors.RED}[!] Invalid choice. Please select 1-15.')
            input(f'\n{Colors.YELLOW}[Press Enter to continue...]')
        except KeyboardInterrupt:
            print(f'\n\n{Colors.RED}[!] Program interrupted by user')
            print(f'{Colors.YELLOW}[+] Returning to main menu...')
            time.sleep(1)
            continue
        except Exception as e:
            print(f'{Colors.RED}[!] Error: {e}')
            input(f'\n{Colors.YELLOW}[Press Enter to continue...]')
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n\n{Colors.RED}[!] Program terminated by user')
        print(f'{Colors.YELLOW}[+] Thank you for using AtlasTools!')
    except Exception as e:
        print(f'{Colors.RED}[!] Fatal error: {e}')