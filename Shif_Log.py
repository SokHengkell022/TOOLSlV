import sys
import os
import time
import re
import requests
import threading
from datetime import datetime
from typing import List, Dict
from colorama import init, Fore, Back, Style
import json
import random
init(autoreset=True)
class Colors:
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    BLACK = Fore.BLACK
    BRIGHT_CYAN = Fore.CYAN + Style.BRIGHT
    BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
    BRIGHT_RED = Fore.RED + Style.BRIGHT
    BRIGHT_YELLOW = Fore.YELLOW + Style.BRIGHT
    BRIGHT_BLUE = Fore.BLUE + Style.BRIGHT
    BRIGHT_MAGENTA = Fore.MAGENTA + Style.BRIGHT
    BRIGHT_WHITE = Fore.WHITE + Style.BRIGHT
    BG_BLUE = Back.BLUE
    BG_RED = Back.RED
    BG_GREEN = Back.GREEN
    BG_YELLOW = Back.YELLOW
    BG_MAGENTA = Back.MAGENTA
    BG_CYAN = Back.CYAN
    BG_WHITE = Back.WHITE
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
    RESET_ALL = Style.RESET_ALL
class Animations:
    @staticmethod
    def loading_spinner(text='Loading', color=Colors.BRIGHT_CYAN):
        spinner = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        for i in range(len(spinner)):
            sys.stdout.write(f'\r{color}{text} {spinner[i]}')
            sys.stdout.flush()
            time.sleep(0.1)
    @staticmethod
    def progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█', color=Colors.BRIGHT_GREEN):
        percent = '{0:.1f}'.format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '░' * (length - filled_length)
        sys.stdout.write(f'\r{color}{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()
        if iteration == total:
            print()
    @staticmethod
    def typewriter(text, delay=0.03, color=Colors.BRIGHT_WHITE):
        for char in text:
            sys.stdout.write(f'{color}{char}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    @staticmethod
    def fade_in(text, steps=5, delay=0.05, color=Colors.BRIGHT_CYAN):
        for i in range(steps + 1):
            alpha = i / steps
            sys.stdout.write(f'\r{color}{text[:int(len(text) * alpha)]}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
class UI:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    @staticmethod
    def print_banner():
        banner = f"\n{Colors.BRIGHT_CYAN}{'══════════════════════════════════════════════════'}\n{Colors.BRIGHT_MAGENTA}{Style.BRIGHT}\n    _________ ________________________   ____\n    \\_   ___ \\_   ___ \\__    ___/\\   \\ /   /\n    /    \\  \\//    \\  \\/ |    |    \\   Y   / \n    \\     \\___\\     \\____|    |     \\     /  \n     \\______  /\\______  /|____|      \\___/   \n        \\/        \\/                     \n{Colors.BRIGHT_YELLOW}{'      '}══════════════════════════════════════\n{Colors.BRIGHT_CYAN}{'      '}       CCTV Hack\n{Colors.BRIGHT_YELLOW}{'      '}══════════════════════════════════════\n{Colors.BRIGHT_GREEN}{'        '}Developer: @XNoctra\n{Colors.BRIGHT_CYAN}{'        '}Community: t.me/Atlas4Sec\n{Colors.BRIGHT_YELLOW}{'        '}Version: 1.0\n{Colors.BRIGHT_CYAN}{'══════════════════════════════════════════════════'}\n{Colors.RESET_ALL}"
        print(banner)
    @staticmethod
    def print_header(text):
        print(f"\n{Colors.BG_BLUE}{Colors.BRIGHT_WHITE}{'     '} {text} {'     '}{Colors.RESET_ALL}")
        print(f"{Colors.CYAN}{'────────────────────────────────────────────────────────────'}{Colors.RESET_ALL}")
    @staticmethod
    def print_success(text):
        print(f'{Colors.BRIGHT_GREEN}[✓] {text}{Colors.RESET_ALL}')
    @staticmethod
    def print_error(text):
        print(f'{Colors.BRIGHT_RED}[✗] {text}{Colors.RESET_ALL}')
    @staticmethod
    def print_warning(text):
        print(f'{Colors.BRIGHT_YELLOW}[!] {text}{Colors.RESET_ALL}')
    @staticmethod
    def print_info(text):
        print(f'{Colors.BRIGHT_CYAN}[i] {text}{Colors.RESET_ALL}')
    @staticmethod
    def print_menu():
        menu = f'\n{Colors.BRIGHT_CYAN}╔══════════════════════════════════════╗\n{Colors.BRIGHT_CYAN}║{Colors.BRIGHT_MAGENTA}               MAIN MENU              {Colors.BRIGHT_CYAN}║\n╠══════════════════════════════════════╣\n║  {Colors.BRIGHT_GREEN}[1]{Colors.BRIGHT_WHITE}  Country List                   {Colors.BRIGHT_CYAN}║\n║  {Colors.BRIGHT_GREEN}[2]{Colors.BRIGHT_WHITE}  Random Scan                    {Colors.BRIGHT_CYAN}║\n║  {Colors.BRIGHT_GREEN}[0]{Colors.BRIGHT_WHITE}  Exit CCTCHack                  {Colors.BRIGHT_CYAN}║\n{Colors.BRIGHT_CYAN}╚══════════════════════════════════════╝\n{Colors.RESET_ALL}'
        print(menu)
PL = ['US', 'JP', 'IT', 'KR', 'FR', 'DE', 'TW', 'RU', 'GB', 'NL', 'CZ', 'TR', 'AT', 'CH', 'ES', 'CA', 'SE', 'IL', 'PL', 'IR', 'NO', 'RO', 'IN', 'VN', 'BE', 'BR', 'BG', 'ID', 'DK', 'AR', 'MX', 'FI', 'CN', 'CL', 'ZA', 'SK', 'HU', 'IE', 'EG', 'TH', 'UA', 'RS', 'HK', 'GR', 'PT', 'LV', 'SG', 'IS', 'MY', 'CO', 'TN
Poland = ['United States', 'Japan', 'Italy', 'Korea', 'France', 'Germany', 'Taiwan', 'Russia', 'UK', 'Netherlands', 'Czech Republic', 'Turkey', 'Austria', 'Switzerland', 'Spain', 'Canada', 'Sweden', 'Israel', 'Poland', 'Iran', 'Norway', 'Romania', 'India', 'Vietnam', 'Belgium', 'Brazil', 'Bulgaria', 'Indonesia', 'Denmark', 'Argentina', 'Mexico', 'Finland', 'China', 'Chile', 'South Africa', 'Slovakia', 'Hungary', 'Ireland', 'Egypt', 'Thailand', 'Ukraine', 'Serbia', 'Hong Kong', 'Greece', 'Portugal', 'Latvia', 'Singapore', 'Iceland', 'Malaysia', 'Colombia', 'Tunisia
class CCTCHack:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        self.results = []
        self.total_found = 0
        self.scan_history = []
    def animate_searching(self):
        dots = ['   ', '.  ', '.. ', '...']
        for i in range(12):
            sys.stdout.write(f'\r{Colors.BRIGHT_CYAN}Searching CCTV feeds{dots[i % 4]}')
            sys.stdout.flush()
            time.sleep(0.2)
    def get_camera_ips(self, country_code: str, max_pages: int=10) -> List[str]:
        all_ips = []
        try:
            UI.print_info(f'Starting scan for {country_code}...')
            stop_animation = threading.Event()
            def show_animation():
                while not stop_animation.is_set():
                    self.animate_searching()
                    time.sleep(0.5)
            anim_thread = threading.Thread(target=show_animation)
            anim_thread.start()
            response = self.session.get(f'http://www.insecam.org/en/bycountry/{country_code}', timeout=10)
            stop_animation.set()
            anim_thread.join()
            UI.clear_screen()
            UI.print_header(f'SCANNING {country_code}')
            last_page_match = re.search('pagenavigator\\(\"\\?page=\", (\\d+)', response.text)
            if not last_page_match:
                UI.print_error('No cameras found or website structure changed')
                return []
            else:
                last_page = min(int(last_page_match.group(1)), max_pages)
                for page in range(1, last_page + 1):
                    UI.print_info(f'Scanning page {page}/{last_page}')
                    Animations.progress_bar(page, last_page, prefix='Progress:', suffix='Complete', length=40)
                    try:
                        page_response = self.session.get(f'http://www.insecam.org/en/bycountry/{country_code}/?page={page}', timeout=8)
                        ips = re.findall('http://\\d+\\.\\d+\\.\\d+\\.\\d+:\\d+', page_response.text)
                        if ips:
                            all_ips.extend(ips)
                            for ip in ips:
                                UI.print_success(f'Found: {ip}')
                                time.sleep(0.1)
                        time.sleep(0.5)
                    except Exception as e:
                        UI.print_error(f'Error on page {page}: {str(e)}')
                    else:
                        pass
                return all_ips
        except Exception as e:
            UI.print_error(f'Connection error: {str(e)}')
            return []
    def display_country_list(self, page: int=1, per_page: int=20):
        total_pages = (len(COUNTRIES) + per_page - 1) // per_page
        start_idx = (page - 1) * per_page
        end_idx = min(start_idx + per_page, len(COUNTRIES))
        UI.clear_screen()
        UI.print_banner()
        UI.print_header('COUNTRY SELECTION')
        print(f'{Colors.BRIGHT_WHITE}Page {page} of {total_pages} | Countries {start_idx + 1}-{end_idx} of {len(COUNTRIES)}')
        print(f"{Colors.CYAN}{'────────────────────────────────────────────────────────────'}{Colors.RESET_ALL}\n")
        for i in range(start_idx, end_idx, 3):
            for j in range(3):
                idx = i + j
                if idx < end_idx:
                    num = idx + 1
                    code = COUNTRIES[idx]
                    name = COUNTRY_NAMES[idx]
                    colors = [Colors.BRIGHT_GREEN, Colors.BRIGHT_CYAN, Colors.BRIGHT_YELLOW]
                    color = colors[j % len(colors)]
                    print(f'{color}[{num:3d}] {name:<25} ({code})', end='')
            print()
        print(f"\n{Colors.BRIGHT_WHITE}{'────────────────────────────────────────────────────────────'}")
        print(f'{Colors.BRIGHT_MAGENTA}Navigation: {Colors.BRIGHT_WHITE}N-next  P-previous  [number]-select  M-menu')
        print(f"{Colors.BRIGHT_WHITE}{'────────────────────────────────────────────────────────────'}")
    def save_results(self, country_code: str, ips: List[str]):
        if not ips:
            return
        else:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'cctv_results_{country_code}_{timestamp}.txt'
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f'CCTV Scan Results - {country_code}\n')
                    f.write(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f'Total IPs Found: {len(ips)}\n')
                    f.write('Tool: CCTCHack by @XNoctra\n')
                    f.write('Community: t.me/Atlas4Sec\n')
                    f.write('==================================================\n\n')
                    for ip in ips:
                        f.write(f'{ip}\n')
                UI.print_success(f'Results saved to: {filename}')
                self.scan_history.append({'country': country_code, 'timestamp': datetime.now().isoformat(), 'count': len(ips), 'filename': filename})
                self.save_history()
            except Exception as e:
                UI.print_error(f'Failed to save results: {str(e)}')
    def save_history(self):
        # irreducible cflow, using cdg fallback
        # ***<module>.CCTCHack.save_history: Failure: Compilation Error
        with open('cctv_history.json', 'w', encoding='utf-8') as f:
            json.dump(self.scan_history, f, indent=2)
                        return None
    def load_history(self):
        # irreducible cflow, using cdg fallback
        # ***<module>.CCTCHack.load_history: Failure: Compilation Error
        if os.path.exists('cctv_history.json'):
            with open('cctv_history.json', 'r', encoding='utf-8') as f:
                self.scan_history = json.load(f)
                        self.scan_history = []
def main():
    # irreducible cflow, using cdg fallback
    # ***<module>.main: Failure: Compilation Error
    hacker = CCTCHack()
    hacker.load_history()
    UI.clear_screen()
    UI.print_banner()
    UI.print_menu()
    choice = input(f'\n{Colors.BRIGHT_GREEN}[CCTCHack]>{Colors.BRIGHT_WHITE} ').strip()
    if choice == '1':
        page = 1
        per_page = 20
        hacker.display_country_list(page, per_page)
        nav = input(f'\n{Colors.BRIGHT_CYAN}Select >{Colors.BRIGHT_WHITE} ').strip().upper()
        if nav == 'N' and page < (len(COUNTRIES) + per_page - 1) // per_page:
            page += 1
        else:
            if nav == 'P' and page > 1:
                page -= 1
            else:
                if nav == 'M':
                    break
                if nav.isdigit():
                    country_num = int(nav)
                    if 1 <= country_num <= len(COUNTRIES):
                            country_code = COUNTRIES[country_num - 1]
                            country_name = COUNTRY_NAMES[country_num - 1]
                            UI.clear_screen()
                            UI.print_banner()
                            UI.print_header(f'SELECTED: {country_name} ({country_code})')
                            confirm = input(f'\n{Colors.BRIGHT_YELLOW}Scan this country? (Y/N): {Colors.BRIGHT_WHITE}').strip().upper()
                            if confirm == 'Y':
                                UI.clear_screen()
                                UI.print_banner()
                                UI.print_header(f'SCANNING {country_name}')
                                print(f'\n{Colors.BRIGHT_CYAN}Starting scan for {country_name} ({country_code})...')
                                print(f'{Colors.BRIGHT_YELLOW}This may take a few moments...')
                                ips = hacker.get_camera_ips(country_code)
                                UI.clear_screen()
                                UI.print_banner()
                                if ips:
                                    UI.print_success(f'✓ Scan completed! Found {len(ips)} CCTV feeds')
                                    print(f'\n{Colors.BRIGHT_CYAN}[1] Save to file')
                                    print(f'{Colors.BRIGHT_CYAN}[2] View IPs')
                                    print(f'{Colors.BRIGHT_CYAN}[3] Back to menu')
                                    action = input(f'\n{Colors.BRIGHT_CYAN}Select action: {Colors.BRIGHT_WHITE}').strip()
                                    if action == '1':
                                        hacker.save_results(country_code, ips)
                                        input(f'\n{Colors.BRIGHT_CYAN}Press Enter to continue...')
                                    else:
                                        if action == '2':
                                            UI.clear_screen()
                                            UI.print_banner()
                                            UI.print_header(f'CCTV IP ADDRESSES - {country_name}')
                                            for idx, ip in enumerate(ips, 1):
                                                if idx <= 50:
                                                    print(f'{Colors.BRIGHT_GREEN}[{idx:3d}] {Colors.BRIGHT_CYAN}{ip}')
                                            if len(ips) > 50:
                                                print(f'\n{Colors.BRIGHT_YELLOW}... and {len(ips) - 50} more IPs (saved in file)')
                                            input(f'\n{Colors.BRIGHT_CYAN}Press Enter to continue...')
                                else:
                                    UI.print_error('✗ No CCTV feeds found')
                                    input(f'\n{Colors.BRIGHT_CYAN}Press Enter to continue...')
                else:
                    UI.print_error('Invalid selection!')
                    time.sleep(1)
        continue
    else:
        if choice == '2':
            UI.clear_screen()
            UI.print_banner()
            UI.print_header('RANDOM SCAN')
            random_idx = random.randint(0, len(COUNTRIES) - 1)
            country_code = COUNTRIES[random_idx]
            country_name = COUNTRY_NAMES[random_idx]
            UI.print_info(f'Selected random country: {country_name} ({country_code})')
            print(f'\n{Colors.BRIGHT_YELLOW}Starting scan in:', end='')
            for i in range(3, 0, (-1)):
                print(f' {i}...', end='')
                sys.stdout.flush()
                time.sleep(1)
            print()
            UI.clear_screen()
            UI.print_banner()
            UI.print_header(f'RANDOM SCAN: {country_name}')
            print(f'\n{Colors.BRIGHT_CYAN}Scanning {country_name} ({country_code})...')
            print(f'{Colors.BRIGHT_YELLOW}This may take a few moments...')
            ips = hacker.get_camera_ips(country_code, max_pages=3)
            UI.clear_screen()
            UI.print_banner()
            if ips:
                UI.print_success(f'✓ Found {len(ips)} CCTV feeds in {country_name}')
                hacker.save_results(country_code, ips)
                print(f'\n{Colors.BRIGHT_CYAN}Sample IPs found:')
                for idx, ip in enumerate(ips[:5], 1):
                    print(f'{Colors.BRIGHT_GREEN}[{idx}] {Colors.BRIGHT_CYAN}{ip}')
                if len(ips) > 5:
                    print(f'{Colors.BRIGHT_YELLOW}... and {len(ips) - 5} more IPs (saved in file)')
                input(f'\n{Colors.BRIGHT_CYAN}Press Enter to continue...')
            else:
                UI.print_error('✗ No feeds found in random selection')
                input(f'\n{Colors.BRIGHT_CYAN}Press Enter to continue...')
        else:
            if choice == '0':
                UI.clear_screen()
                UI.print_banner()
                UI.print_header('EXITING CCTCHack')
                print(f'\n{Colors.BRIGHT_MAGENTA}Thank you for using CCTCHack!')
                print(f'{Colors.BRIGHT_CYAN}Stay ethical. Stay curious.')
                print(f'\n{Colors.BRIGHT_YELLOW}Developer: @XNoctra')
                print(f'{Colors.BRIGHT_GREEN}Community: t.me/Atlas4Sec')
                print(f'\n{Colors.BRIGHT_CYAN}Goodbye! 👋\n')
                time.sleep(2)
                return
            else:
                UI.print_error('Invalid option! Please try again.')
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    print(f'\n\n{Colors.BRIGHT_RED}Interrupted by user')
    confirm = input(f'\n{Colors.BRIGHT_YELLOW}Exit CCTCHack? (Y/N): {Colors.BRIGHT_WHITE}').strip().upper()
    if confirm == 'Y':
        pass
    return None
    except Exception as e:
        pass
    UI.print_error(f'Error: {str(e)}')
    time.sleep(2)
if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print(f'{Colors.BRIGHT_RED}Error: \'requests\' module not installed!')
        print(f'{Colors.BRIGHT_WHITE}Install with: pip install requests')
        sys.exit(1)
    main()
        except KeyboardInterrupt:
            print(f'\n\n{Colors.BRIGHT_RED}Program terminated by user.')
            except Exception as e:
                    print(f'\n{Colors.BRIGHT_RED}Fatal error: {str(e)}')
                        # return None
                        e = None