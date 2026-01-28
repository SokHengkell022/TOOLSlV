#!/usr/bin/env python3
import os
import sys
import time
import base64
import re
import subprocess
import marshal
import zlib
from datetime import datetime
from colorama import Fore, Style, Back, init

MERAH = "\033[31m"
BLUE_TERANG = "\033[94m"
CYAN_TERANG = "\033[96m"
MERAH_TERANG = "\033[91m"
BLUE = "\033[34m"
YELLOW_TERANG = "\033[33m"
HIJAU_TERANG = "\033[32m"
GREEN_TERANG = "\033[92m"
GREEN = "\033[32m"
BG_MERAH = "\033[41m"
MAGENTA_TERANG = "\033[95m"
PUTIH_TERANG = "\033[97m"
BG_BLUE = "\033[44m"
RESET = "\033[0m"

def banner():
    os.system('clear')
    print("")
    banner = f"""{MAGENTA_TERANG}
    ⠀⠀⠀⠀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠉⣹⠋⠉⢉⡟⢩⢋⠋⣽⡻⠭⢽⢉⠯⠭⠭⠭⢽⡍⢹⡍⠙⣯⠉⠉⠉⠉⠉⣿⢫⠉⠉⠉⢉⡟⠉⢿⢹⠉⢉⣉⢿⡝⡉⢩⢿⣻⢍⠉⠉⠩⢹⣟⡏⠉⠹⡉⢻⡍⡇
⠀⢸⢠⢹⠀⠀⢸⠁⣼⠀⣼⡝⠀⠀⢸⠘⠀⠀⠀⠀⠈⢿⠀⡟⡄⠹⣣⠀⠀⠐⠀⢸⡘⡄⣤⠀⡼⠁⠀⢺⡘⠉⠀⠀⠀⠫⣪⣌⡌⢳⡻⣦⠀⠀⢃⡽⡼⡀⠀⢣⢸⠸⡇
⠀⢸⡸⢸⠀⠀⣿⠀⣇⢠⡿⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠘⢇⠸⠘⡀⠻⣇⠀⠀⠄⠀⡇⢣⢛⠀⡇⠀⠀⣸⠇⠀⠀⠀⠀⠀⠘⠄⢻⡀⠻⣻⣧⠀⠀⠃⢧⡇⠀⢸⢸⡇⡇
⠀⢸⡇⢸⣠⠀⣿⢠⣿⡾⠁⠀⢀⡀⠤⢇⣀⣐⣀⠀⠤⢀⠈⠢⡡⡈⢦⡙⣷⡀⠀⠀⢿⠈⢻⣡⠁⠀⢀⠏⠀⠀⠀⢀⠀⠄⣀⣐⣀⣙⠢⡌⣻⣷⡀⢹⢸⡅⠀⢸⠸⡇⡇
⠀⢸⡇⢸⣟⠀⢿⢸⡿⠀⣀⣶⣷⣾⡿⠿⣿⣿⣿⣿⣿⣶⣬⡀⠐⠰⣄⠙⠪⣻⣦⡀⠘⣧⠀⠙⠄⠀⠀⠀⠀⠀⣨⣴⣾⣿⠿⣿⣿⣿⣿⣿⣶⣯⣿⣼⢼⡇⠀⢸⡇⡇⡇
⠀⢸⢧⠀⣿⡅⢸⣼⡷⣾⣿⡟⠋⣿⠓⢲⣿⣿⣿⡟⠙⣿⠛⢯⡳⡀⠈⠓⠄⡈⠚⠿⣧⣌⢧⠀⠀⠀⠀⠀⣠⣺⠟⢫⡿⠓⢺⣿⣿⣿⠏⠙⣏⠛⣿⣿⣾⡇⢀⡿⢠⠀⡇
⠀⢸⢸⠀⢹⣷⡀⢿⡁⠀⠻⣇⠀⣇⠀⠘⣿⣿⡿⠁⠐⣉⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠳⠄⠀⠀⠀⠀⠋⠀⠘⡇⠀⠸⣿⣿⠟⠀⢈⣉⢠⡿⠁⣼⠁⣼⠃⣼⠀⡇
⠀⢸⠸⣀⠈⣯⢳⡘⣇⠀⠀⠈⡂⣜⣆⡀⠀⠀⢀⣀⡴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣆⣀⠀⠀⠀⣀⣜⠕⡊⠀⣸⠇⣼⡟⢠⠏⠀⡇
⠀⢸⠀⡟⠀⢸⡆⢹⡜⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⣾⡏⡇⡎⡇⠀⡇
⠀⢸⠀⢃⡆⠀⢿⡄⠑⢽⣄⠀⠀⠀⢀⠂⠠⢁⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⡐⢀⠂⠀⠀⣠⣮⡟⢹⣯⣸⣱⠁⠀⡇
⠀⠈⠉⠉⠋⠉⠉⠋⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠋⡟⠉⠉⡿⠋⠋⠋⠉⠉⠁
    {RESET}{CYAN_TERANG} ╔═╗ ╔╗╔ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔╦╗     ╔╦╗ ╔═╗ ╔═╗ ╦   ╔═╗
    {RESET}{CYAN_TERANG} ║╣  ║║║ ║   ╠╦╝ ╚╦╝ ╠═╝  ║       ║  ║ ║ ║ ║ ║   ╚═╗
    {RESET}{CYAN_TERANG} ╚═╝ ╝╚╝ ╚═╝ ╩╚═  ╩  ╩    ╩       ╩  ╚═╝ ╚═╝ ╩═╝ ╚═╝
    {RESET}{PUTIH_TERANG}                  J U N E D  K W{RESET}"""
    print(banner)
    print("")
    print(f"[{BG_MERAH}{PUTIH_TERANG}INFO{RESET}]{PUTIH_TERANG} DONT USE TOOLS FOR ENC MALICIOUS TOOLS{RESET}")
    print("")
    print(f"{CYAN_TERANG}[01] {RESET}{GREEN_TERANG}ENCRYPT BASE64 zlib [python]{RESET}")
    print(f"{CYAN_TERANG}[02] {RESET}{GREEN_TERANG}ENCRYPT MARSHAL [python]{RESET}")
    print(f"{CYAN_TERANG}[03] {RESET}{GREEN_TERANG}DECRYPT BASE64 zlib [python]{RESET}")
    print(f"{CYAN_TERANG}[04] {RESET}{GREEN_TERANG}ENC MARSHAL INCLUDE [python]{RESET}")
    print(f"{CYAN_TERANG}[05] {RESET}{GREEN_TERANG}JAVASCRIPT ENCRYPT [javascript]{RESET}")
    print(f"{CYAN_TERANG}[06] {RESET}{GREEN_TERANG}BASH ENCRYPT [bash only]{RESET}")
    print(f"{CYAN_TERANG}[07] {RESET}{GREEN_TERANG}XOR ENCRYPT [python only]{RESET}")
    print(f"{CYAN_TERANG}[08] {RESET}{GREEN_TERANG}HTML ENCODE{RESET}")
    print(f"{CYAN_TERANG}[10] {RESET}{GREEN_TERANG}IKUTI MY SALURAN{RESET}")
    print(f"{CYAN_TERANG}[11] {RESET}{GREEN_TERANG}HUBUNGI DEVELOPER{RESET}")
    print(f"{CYAN_TERANG}[12] {RESET}{GREEN_TERANG}EXIT{RESET}")

def encrypt_marshal():
    os.system('clear')
    ngentod = f"""{MAGENTA_TERANG}
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⠒⢲
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠉⠀⢀⡴⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⣁⠀⠀⣀⡴⠟⣪⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⣉⠤⢒⣩⠴⠒⠉⢁⡠⣚⢥⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣖⠪⠭⠈⣉⠽⣐⠮⢕⣊⡤⠤⠒⠋⢉⡤⠊⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⡰⢅⣖⡲⠾⠍⣩⢯⣒⣋⠥⢤⣒⠠⠤⠐⢛⡶⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⣹⢥⡗⠶⠌⣉⠯⠔⣒⣊⠩⠁⠀⣀⣠⣖⣏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣈⣷⡲⡏⠉⣙⡯⠭⠥⠒⠒⠊⠉⠉⠀⢀⡴⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡤⠚⡁⢠⡾⣟⣍⡎⠭⢖⣏⣉⡥⠤⠤⠤⠤⠴⠭⡅⠀⠀⠀⠀⠀
⠀⠀⠀⡖⣺⠻⣏⣰⣄⣿⣟⡼⡿⣾⣞⣉⠿⠭⢐⣀⣀⣀⣀⣤⡴⠚⠁⠀⠀⠀⠀⠀
⠀⠀⡼⣽⣟⡟⢿⢛⣎⡏⣾⢮⣟⣽⡷⡛⠧⢖⣒⣂⢀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀
⢀⣜⡗⣏⣹⡏⢻⣯⣻⢹⢱⣟⢼⢻⣳⡌⠑⠄⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣪⡎⡰⣫⢷⣻⢳⢻⠒⡿⡝⡍⣆⠱⠜⣶⠤⠄⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⠦⢞⡇⢪⠇⠘⣸⠀⡗⣧⢳⢸⠙⠦⠼⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠧⠾⡄⣠⠋⢧⣠⠎⠣⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{RESET}{CYAN_TERANG}╔╦╗ ╔═╗ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╦       ╔═╗ ╔╗╔ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔╦╗
{RESET}{CYAN_TERANG}║║║ ╠═╣ ╠╦╝ ╚═╗ ╠═╣ ╠═╣ ║       ║╣  ║║║ ║   ╠╦╝ ╚╦╝ ╠═╝  ║ 
{RESET}{CYAN_TERANG}╩ ╩ ╩ ╩ ╩╚═ ╚═╝ ╩ ╩ ╩ ╩ ╩═╝     ╚═╝ ╝╚╝ ╚═╝ ╩╚═  ╩  ╩    ╩ 
    {RESET}"""
    print(ngentod)
    print("")
    print(f"[{BG_MERAH}{PUTIH_TERANG}INFO{RESET}]{PUTIH_TERANG} INI MENGGUNAKAN ENCRYPT SISTEM MARSHAL{RESET}")

def kontol():
    encrypt_marshal()
    file_kontol = input(f"{CYAN_TERANG}ENTER FILEPATH: {RESET}").strip()
    output = input(f"{CYAN_TERANG}ENTER OUTPUT: {RESET}").strip()
    
    if not os.path.exists(file_kontol):
        print(f"{MERAH}❌ file path ga ditemukan")
        input(f"\n{MERAH}TEKAN ENTER BUAT KEMBALI {RESET}{BG_MERAH}{PUTIH_TERANG}ENTER{RESET}")

    with open(file_kontol, 'r') as f:
        anjing = f.read()

    compiled = compile(anjing, file_kontol, 'exec')
    haha = base64.b64encode(marshal.dumps(compiled))
    
    with open(output, "w") as f:
        f.write('#encrypted by juned tools\n')
        f.write('import base64, marshal \n')
        f.write(f'exec(marshal.loads(base64.b64decode({haha})))')

    dirname = os.path.dirname(file_kontol)
    basename = os.path.basename(file_kontol)
    file_output = os.path.join(output, dirname)

    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPTED{RESET}")
    print(f"{GREEN_TERANG}[!] file asli: {basename}")
    print(f"{GREEN_TERANG}[!] directory: {dirname}")
    print(f"{GREEN_TERANG}[!] File After Enc: {file_output}")
    print(f"{GREEN_TERANG}[✓] succes encrypt by juned")
    print("")
    input(f"\n{GREEN_TERANG}Tekan Enter Buat Kembali: {RESET}{BG_BLUE}{PUTIH_TERANG}ENTER{RESET}")


def enc_base_64():
    music()
    os.system('clear')
    hama = f"""{MAGENTA_TERANG}
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⠿⣟⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣏⡏⠀⠀⠀⢣⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣟⠧⠤⠤⠔⠋⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⡀⢀⣶⠤⠒⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠈⢿⣆⣠⣤⣤⣤⣤⣴⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⢿⢿⠀⠀⠀⢀⣀⣀⠘⣿⠋⠁⠀⠙⢇⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⢇⡞⠘⣧⠀⢖⡭⠞⢛⡄⠘⣆⠀⠀⠀⠈⢧⠀⠀⠀⠙⢿⣄⠀⠀⠀⠀
⠀⠀⣠⣿⣛⣥⠤⠤⢿⡄⠀⠀⠈⠉⠀⠀⠹⡄⠀⠀⠀⠈⢧⠀⠀⠀⠈⠻⣦⠀⠀⠀
⠀⣼⡟⡱⠛⠙⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠹⣧⡀⠀
⢸⡏⢠⠃⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠸⣷⡀
⠸⣧⠘⡇⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⣿⠇
⠀⣿⡄⢳⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀
⠀⢹⡇⠘⣇⠀⠀⠀⠀⠀⠀⠰⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣼⡟⠀⠀
⠀⢸⡇⠀⢹⡆⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢳⣼⠟⠀⠀⠀
⠀⠸⣧⣀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢃⠀⢀⣴⡿⠁⠀⠀⠀⠀
⠀⠀⠈⠙⢷⣄⢳⡀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⣠⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢿⣷⣦⣄⣀⣀⣠⣤⠾⠷⣦⣤⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{RESET}{CYAN_TERANG}╔╗  ╔═╗ ╔═╗     ╔═╗ ╔╗╔ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔╦╗    
{RESET}{CYAN_TERANG}╠╩╗ ╠═╣ ║ ╦     ║╣  ║║║ ║   ╠╦╝ ╚╦╝ ╠═╝  ║     
{RESET}{CYAN_TERANG}╚═╝ ╩ ╩ ╚═╝     ╚═╝ ╝╚╝ ╚═╝ ╩╚═  ╩  ╩    ╩      ⠀{RESET}"""
    print(hama)
    print(f"[{BG_MERAH}{CYAN_TERANG}INFO{RESET}]{RESET} BAG ENCRYPT TOOLS FOR PYTHON ENCRYPT {RESET}")
    print("")

def enc():
    enc_base_64()
    file = input(f"{CYAN_TERANG}ENTER YOUR FILEPATH: {RESET}").strip()
    
    if not os.path.exists(file):
        print(f"{MERAH}❌ file path ga di temukan{RESET}")
        print("")
        input(f"\n{MERAH}tekan enter buat kembali: {RESET}{BG_MERAH}{YELLOW_TERANG}ENTER{RESET}")
        return
    
    with open(file, 'r') as f:
        ngentod = f.read()

    compress = zlib.compress(ngentod.encode())
    anjing = base64.b64encode(compress).decode()

    dir = os.path.dirname(file)
    basename = os.path.basename(file)
    enc_name = f"ENCRYPT_BY_JUNED{basename}"
    encrypt_path = os.path.join(dir, enc_name)

    with open(encrypt_path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('import base64, zlib\n')
        f.write(f'exec(zlib.decompress(bas64.b64decode("{anjing}")))')

    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPT{RESET}")
    print(f"{GREEN_TERANG}[!] file asli jing: {basename}")
    print(f"{GREEN_TERANG}[!] directory: {dir}")
    print(f"{GREEN_TERANG}[!] file sesudah di enc: {encrypt_path}")

    input(f"\n{GREEN_TERANG}TEKAN enter buat kembali: {RESET}{BG_BLUE}ENTER{RESET}")

def anjay():
    os.system('clear')
    k = f"""{MAGENTA_TERANG}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠟⠋⠁⣀⣤⣤⣤⣤⣀⠈⠙⠻⢿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢠⣾⣿⡿⠋⠀⠀⢀⣾⣿⡿⠿⠿⢿⣿⣷⡀⠀⠀⠙⢿⣿⣷⡄⠀⠀
⠀⢠⣿⣿⠏⠀⠀⠀⠀⣿⣿⡟⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠹⣿⣿⡄⠀
⢠⣿⣿⠏⠀⠀⠀⠀⠀⠛⠛⠃⠀⠀⠀⠀⠘⠛⠛⠀⠀⠀⠀⠀⠹⣿⣿⡄
⢸⣿⣿⠀⠀⠀⢠⣶⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡄⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⢸⡇⠀⣿⣿⣿⠋⠀⠀⠙⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⢸⡇⠀⣿⣿⣿⡀⠀⠀⢀⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⡇
⠘⣿⣿⣆⠀⠀⢸⡇⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⣰⣿⣿⠃
⠀⠘⣿⣿⣆⠀⢸⣧⣠⣿⣿⣿⣿⣄⣠⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⠃⠀
⠀⠀⠘⢿⣿⣷⣄⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣠⣾⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{RESET}{CYAN_TERANG}╔╦╗ ╔═╗ ╔═╗ ╔═╗ ╔╦╗ ╔═╗     ╔╦╗ ╔═╗ ╔═╗ ╦   ╔═╗
{RESET}{CYAN_TERANG} ║║ ║╣  ║   ║ ║  ║║ ║╣       ║  ║ ║ ║ ║ ║   ╚═╗
{RESET}{CYAN_TERANG}═╩╝ ╚═╝ ╚═╝ ╚═╝ ═╩╝ ╚═╝      ╩  ╚═╝ ╚═╝ ╩═╝ ╚═╝{RESET}"""
    print(k)
    print("")
    print(f"[{BG_MERAH}{PUTIH_TERANG}INFO{RESET}]{PUTIH_TERANG} THIS TOOLS DECRYPT FOR base64 {RESET}")
    print("")

def decode():
    anjay()
    path = input(f"{CYAN_TERANG}Masukkan path file: {RESET}").strip()

    if not os.path.isfile(path):
        print("❌ File tidak ditemukan")
        sys.exit(0)

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    pattern = r'ENC_DATA\s*\(\s*atob\s*\(\s*"(.*?)"\s*\)\s*\)'
    match = re.search(pattern, text, re.S)

    if not match:
        print(f"{MERAH_TERANG}❌ Tidak ditemukan payload base64")
        sys.exit()

    payload = match.group(1)
    print(f"{GREEN_TERANG}✔ Payload:", payload[:50], "...")

def marshal_ngentod():
    os.system('clear')
    print(f"""{MAGENTA_TERANG}
         (\__/)
         (•ㅅ•) 
        ノヽ ノ＼＿
    `/　`/ ⌒Ｙ⌒ Ｙ  ヽ
    ( 　(三ヽ人　 /　  |
    |　ﾉ⌒＼ ￣￣ヽ   ノ
    ヽ＿＿＿＞､＿_／
        ｜( 王 ﾉ〈   
         /ﾐ`ー―彡\  
        / ╰    ╯ \ /    
        \  /---\   /
       
{RESET}{CYAN_TERANG}╔╦╗ ╔═╗ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╦
{RESET}{CYAN_TERANG}║║║ ╠═╣ ╠╦╝ ╚═╗ ╠═╣ ╠═╣ ║
{RESET}{CYAN_TERANG}╩ ╩ ╩ ╩ ╩╚═ ╚═╝ ╩ ╩ ╩ ╩ ╩═╝ {RESET}""")
    print("")
    print(f"[{BG_MERAH}{YELLOW_TERANG}INFO{RESET}]{PUTIH_TERANG} TOOLS INI MENGGUNAKAN ENC SISTEM MARSHAL + BASE64 + ZLIB")
    print("")

def gatau():
    marshal_ngentod()
    path = input(f"{CYAN_TERANG}ENTER YOUR FILEPATH: {RESET}")
    out = input(f"{CYAN_TERANG}ENTER YOUT OUTPUT: {RESET}")

    if not os.path.exists(path):
        print(f"{MERAH_TERANG}[!] File Path Ga Di Temukan {RESET}")
        time.sleep(2)
        sys.exit(0)
    
    with open(path, "r", encoding='utf-8') as f:
        anjing = f.read()

    c = compile(anjing, path, "exec")
    dumped = marshal.dumps(c)
    ngen = zlib.compress(dumped, 9)
    b = base64.b64encode(ngen).decode()

    d = os.path.dirname(path)
    ytim = os.path.basename(path)
    p = os.path.join(d, out)

    with open(out, "w") as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# im juned tools encode\n')
        f.write('import marshal, base64, zlib\n')
        f.write(f'exec(marshal.loads(zlib.decompress(base64.b64decode("{b}"))))')
        
    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPT BY JUNED{RESET}")
    print(f"{GREEN_TERANG}[!] Directory: {d}{RESET}")
    print(f"{GREEN_TERANG}[!] FILE: {ytim}{RESET}")
    print(f"{GREEN_TERANG}[!] FILE AFTER ENC: {p}{RESET}")
    print("")
    input(f"\n{MERAH_TERANG}Tekan enter buat kembali: {RESET}{BG_BLUE}{PUTIH_TERANG}ENTER{RESET}")

def js_encode():
    os.system('clear')
    ahnjy = f"""{MAGENTA_TERANG}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣶⣽⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡟⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
        ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⣽⣛⠀⠀⠀⠀
        ⠀⠀⢠⣿⣿⣿⣿⣿⣿⠿⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠿⣿⣿⣿⣿⣿⣶⡄⠀⠀
        ⠀⢰⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⣿⣿⡆⠀
        ⡰⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢆

{RESET}{CYAN_TERANG}  ╦ ╔═╗ ╦  ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╦ ╔═╗ ╔╦╗     ╔═╗ ╔╗╔ ╔═╗
{RESET}{CYAN_TERANG}  ║ ╠═╣ ║  ║ ╠═╣ ╚═╗ ║   ╠╦╝ ║ ╠═╝  ║      ║╣  ║║║ ║  
{RESET}{CYAN_TERANG}╚═╝ ╩ ╩ ╚══╝ ╩ ╩ ╚═╝ ╚═╝ ╩╚═ ╩ ╩    ╩      ╚═╝ ╝╚╝ ╚═╝{RESET}"""
    print(ahnjy)
    print("")
    print(f"[{BG_MERAH}{YELLOW_TERANG}INFO{RESET}]{PUTIH_TERANG} THIS TOOLS FOR JAVASCRIPT ENCRYPTED{RESET}")

def main_js_encode():
    js_encode()
    print("")
    males_ah = input(f"{CYAN_TERANG}ENTER YOUR FILEPATH: {RESET}").strip()
    asu = input(f"{CYAN_TERANG}ENTER YOUR OUTPUT: {RESET}").strip()
    
    if not os.path.exists(males_ah):
        print(f"{MERAH_TERANG}[!] TIDAK MENEMUKAN FILEPATH {RESET}")
        time.sleep(1)
        sys.exit(0)
    
    with open(males_ah, "r", encoding='utf-8') as f:
        taktau = f.read()

    bngke = zlib.compress(taktau.encode('utf-8'), 9)
    hmm = base64.b64encode(bngke).decode()

    ilik = os.path.dirname(males_ah)
    bas = os.path.basename(males_ah)
    en = os.path.join(ilik, asu)

    with open(asu, "w") as f:
        f.write('const zlib = require("zlib")\n\n')
        f.write(f'const buf = Buffer.from("{hmm}", "base64")\n')
        f.write('const code = zlib.inflateSync(buf).toString();\n\n')
        f.write('eval (code);')

    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPT BY JUNED{RESET}")
    print(f"{GREEN_TERANG}[!] FILE ASLI: {bas}")
    print(f"{GREEN_TERANG}[!] DIRECTORY: {ilik}")
    print(f"{GREEN_TERANG}[!] FILE AFTER: {en}")
    input(f"\n{MERAH_TERANG} PRESS ENTER TO EXIT: {RESET}{BG_MERAH}{YELLOW_TERANG}ENTER{RESET}")

def shell_encode():
    os.system('clear')
    print(f"""{MERAH_TERANG}
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⡴⣶⡶⣶⢶⣶⢶⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡶⣿⣽⣻⢾⣳⡿⣯⢿⣽⢿⣞⣿⣽⢾⣳⣟⡿⣟⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣻⢷⣻⡷⣯⣟⡿⣽⣻⣽⢿⣽⣻⣾⣻⢾⣟⣯⡿⣽⣟⡷⣯⡿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣶⣿⣻⢾⣽⣟⣯⣿⣽⢾⣟⡿⣽⢯⣿⣞⣯⡷⣟⣿⢾⡯⠛⠋⠚⠻⣽⣻⢷⣯⣟⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣻⢾⣽⣟⡷⣯⣷⣟⡾⣿⣽⣻⢯⣿⣳⣯⡿⣽⢿⣽⡛⠀⠀⠀⠀⠀⢸⣟⡿⣾⣽⢾⣻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣟⣾⡽⣟⣷⣯⢿⣻⡾⣽⣻⢷⡏⠉⠉⠀⠀⠀⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⣸⣯⢿⣳⣯⣿⣻⢾⡿⡄⠀⠀⠀
⠀⠀⢠⣿⣳⢿⣞⡿⣯⣷⣻⣟⡷⣿⠟⠉⠹⣟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣦⣶⣾⣻⡽⣟⣯⣷⢯⣟⣯⡿⣿⣆⠀⠀
⠀⢠⡿⣯⣟⣯⡿⣽⣷⣻⢷⣻⠟⠁⠀⠀⠀⠹⡿⣤⣶⢶⡿⣿⢶⡶⣤⣀⠀⠀⠀⠀⠈⠻⣽⢿⣽⢾⣟⣯⡿⣽⣷⣻⡄⠀
⠀⣾⣟⣷⣻⣽⣻⣽⡾⣯⣿⠃⠀⠀⠀⠀⣠⣾⣻⣽⡾⣿⡽⣯⣟⣿⡽⣯⣷⣄⠀⠀⠀⠀⠙⣿⢾⣻⣽⣾⣻⢷⣯⡷⣷⠀
⢰⣟⣾⡽⣯⣷⣟⡷⣿⣽⡆⠀⠀⠀⠀⣼⢯⣷⣟⡷⣿⣳⡿⣯⣟⣾⢿⣽⡾⣽⣧⠀⠀⠀⠀⢸⡿⣯⣷⢯⣟⡿⣾⣽⣟⡂
⢸⣯⡷⣿⣻⠎⠁⠀⠀⠉⢿⣄⠀⠀⢸⣟⣯⣷⢿⣽⡷⣿⡽⣷⣻⣽⣟⣾⣽⡷⣯⡇⠀⠀⠀⠀⣿⢷⣯⡿⣯⢿⣳⡿⣾⠇
⢸⡷⣟⣯⡗⠀⠀⠀⠀⠀⢈⡷⠀⠀⣿⢯⣷⣻⣟⣾⣽⢷⣟⣯⡿⣾⣽⢾⣳⡿⣯⢿⠞⡷⠿⠶⣿⣻⣾⡽⣟⣿⣽⣻⣽⡇
⢸⣟⣯⡿⣽⣆⡀⠀⠀⣠⣾⠋⠀⠀⢸⣟⣷⣯⢿⡾⣽⢿⣞⣯⣿⣳⣯⡿⣯⢿⣽⡇⠀⠀⠀⠀⣿⢷⣯⣟⡿⣞⣷⣟⡷⡇
⠸⣯⣷⢿⣯⣟⣿⣻⣟⣯⣇⠀⠀⠀⠀⢻⡾⣽⣯⢿⣻⣯⣟⣷⢯⣷⢿⣽⣻⣯⡗⠀⠀⠀⠀⣸⣟⡿⣾⣽⣻⢯⣷⣟⡿⠅
⠀⢿⣞⡿⣾⣽⢾⣷⣻⣽⣾⣄⠀⠀⠀⠀⠙⢟⣾⢿⣽⡾⣽⡾⣿⣽⣻⡾⡷⠋⠀⠀⠀⠀⣰⣯⢿⣽⡷⣯⣟⣿⣳⣯⡿⠀
⠀⠘⣯⢿⣳⣯⣿⣞⣯⡷⣟⣾⢦⡀⠀⠀⠀⣰⣯⠛⠾⠻⢽⡟⠷⠯⠓⠉⠀⠀⠀⠀⢀⣴⣟⣾⣟⡷⣟⣯⡿⣾⣽⣳⠁⠀
⠀⠀⠘⣿⢯⣷⣟⣾⢯⣟⡿⣽⣻⢿⣦⣀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠛⠿⢻⣟⣾⣽⢾⣻⣟⡷⣿⣽⢾⠃⠀⠀
⠀⠀⠀⠘⢿⣳⢿⣾⣻⢯⣿⣻⣽⢿⡾⣽⡾⣧⣄⣀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⢹⡷⣯⣿⣻⢾⡿⣽⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣟⣾⢯⣿⣳⣯⣟⣯⡿⣯⣟⣷⣻⢯⣿⣟⡿⣟⡿⣟⣿⢦⠀⠀⠀⠀⠀⣸⢿⣽⣞⡿⣯⢿⠳⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠯⣿⣳⣟⡷⣯⡿⣽⣷⣻⣽⢯⣿⣳⣯⢿⣻⣽⢿⣽⣻⢷⣤⣤⣤⣴⣟⡿⣾⣽⣻⡽⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢞⣿⣽⣻⢷⣯⣟⣾⣟⡷⣿⣽⣻⢯⣟⡿⣞⣿⣻⡾⣽⣳⡿⣞⣿⣳⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠿⣻⣾⣽⣳⣯⢿⡷⣯⣟⡿⣽⣻⣯⡷⣿⡽⣿⣽⡻⠝⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠛⠙⠯⠿⠽⠾⠟⠿⠳⠯⠟⠓⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{RESET}{CYAN_TERANG}╔╗  ╔═╗ ╔═╗ ╦ ╦     ╔═╗ ╔╗╔ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔╦╗ ╔═╗ ╔╦╗
{RESET}{CYAN_TERANG}╠╩╗ ╠═╣ ╚═╗ ╠═╣     ║╣  ║║║ ║   ╠╦╝ ╚╦╝ ╠═╝  ║  ║╣   ║║
{RESET}{CYAN_TERANG}╚═╝ ╩ ╩ ╚═╝ ╩ ╩     ╚═╝ ╝╚╝ ╚═╝ ╩╚═  ╩  ╩    ╩  ╚═╝ ═╩╝{RESET}""")
    print("")
    print(f"[{BG_MERAH}{YELLOW_TERANG}INFO{RESET}]{PUTIH_TERANG} THIS TOOLS FOR BASH ENCRYPT")
    print("")

def main_bash():
    print("")
    shell_encode()
    bash_path = input(f"{CYAN_TERANG}Enter Your Bash Path: {RESET}").strip()
    oub = input(f"{CYAN_TERANG}Enter The Output: {RESET}").strip()
    
    if not os.path.exists(bash_path):
        print(f"{MERAH_TERANG}[×] FILEPATH GA DI TEMUKAN {RESET}")
        input(f"\n{MERAH_TERANG}Tekan Enter Buat Kembali: {RESET}{BG_MERAH}{PUTIH_TERANG}ENTER{RESET}")

    with open(bash_path, "r", encoding='utf-8', errors='ignore') as f:
        yatim = f.read()
    
    coppy = zlib.compress(yatim.encode())
    gata = base64.b64encode(coppy).decode()

    dire = os.path.dirname(bash_path)
    name = os.path.basename(bash_path)
    after_enc = os.path.join(dire, oub)

    with open(oub, "w") as f:
        f.write('#ngentod\n')
        f.write('TMP_FILE=$(mktemp)\n')
        f.write('cat > "$TMP_FILE" << "ENDOFFILE"\n')
        f.write(gata + '\n')
        f.write('ENDOFFILE\n')
        f.write('base64 "$TMP_FILE" | bash\n')
        f.write('rm -f "$TMP_FILE"')

    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPT BY JUNED{RESET}")
    print(f"{GREEN_TERANG}[!] DIRECTORY ASLI: {dire}{RESET}")
    print(f"{GREEN_TERANG}[!] FILE ASLI: {name}{RESET}")
    print(f"{GREEN_TERANG}[!] FILE AFTER ENC {after_enc}{RESET}")
    print("")
    input(f"\n{GREEN_TERANG}[!] TEKAN ENTER BUAT KEMBALI: {RESET}{BG_MERAH}{PUTIH_TERANG}ENTER{RESET}")

def xor_data(data: bytes, key: bytes) -> bytes:
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len(key)])
    return bytes(result)

def gatau_anjing():
    os.system('clear')
    print("")
    print(f"""{MAGENTA_TERANG}
    ⠉⠉⠉⠉⠁⠒⠂⠰⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠀⠐⠒⠒⠀⠀⠈⠉⠉⠉⠉⢉⣉⣉⣉⣙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠒⠒⠉⠁⠀⠀⠀⠀⠳⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠉⠛⠛⠶⢦⣤⡐⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⢳⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠳⠶⢶⣦⠤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠉⠑⢄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄
{RESET}{CYAN_TERANG}        ═╦╦═ ╔═╗ ╔═╗     ╔═╗ ╔╗╔ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔╦╗
{RESET}{CYAN_TERANG}         ╬╬  ║ ║ ╠╦╝     ║╣  ║║║ ║   ╠╦╝ ╚╦╝ ╠═╝  ║ 
{RESET}{CYAN_TERANG}        ═╩╩═ ╚═╝ ╩╚═     ╚═╝ ╝╚╝ ╚═╝ ╩╚═  ╩  ╩    ╩ """)
    print("")
    print(f"[{BG_MERAH}{YELLOW_TERANG}INFO{RESET}]{PUTIH_TERANG} THIS TOOLS USING XOR FOR ENCRYPT{RESET}")
    print("")

def xor_encrypt_main():
    gatau_anjing()
    print("")
    input_path = input(f"{CYAN_TERANG}ENTER YOUR FILEPATH: {RESET}").strip()
    output_path = input(f"{CYAN_TERANG}ENTER OUTPUT FILE: {RESET}").strip()
    key = input(f"{CYAN_TERANG}ENTER YOUR KEY: {RESET}").strip()
    
    if not key:
        print(f"{MERAH_TERANG}[!] KEY CANNOT BE EMPTY{RESET}")
        input(f"\n{MERAH_TERANG}[!] PRESS ENTER FOR RETURN TO MENU{RESET}")
        return
    
    key_bytes = key.encode()
    
    if not os.path.exists(input_path):
        print(f"{MERAH_TERANG}[!] YOUR FILEPATH IS NOT EXISTS {RESET}")
        input(f"\n{MERAH_TERANG}[!] PRESS ENTER FOR RETURN TO MENU{RESET}")
        return

    with open(input_path, 'rb') as f:
        original_data = f.read()

    compressed_data = zlib.compress(original_data)
    encrypted_data = xor_data(compressed_data, key_bytes)
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')

    asli = os.path.dirname(input_path)
    file_asli = os.path.basename(input_path)
    after_sex = os.path.join(asli, output_path)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('import base64\n')
        f.write('import zlib\n')
        f.write('import sys\n\n')
        f.write(f'ENCRYPTED_DATA = """{encoded_data}"""\n\n')
        f.write(f'KEY = b"{key}"\n\n')
        f.write('def xor_decrypt(data, key):\n')
        f.write('    result = bytearray()\n')
        f.write('    for i in range(len(data)):\n')
        f.write('        result.append(data[i] ^ key[i % len(key)])\n')
        f.write('    return bytes(result)\n\n')
        f.write('try:\n')
        f.write('    encrypted_bytes = base64.b64decode(ENCRYPTED_DATA)\n')
        f.write('    compressed_data = xor_decrypt(encrypted_bytes, KEY)\n')
        f.write('    original_code = zlib.decompress(compressed_data)\n')
        f.write('    exec(original_code.decode("utf-8"))\n')
        f.write('except Exception as e:\n')
        f.write('    print(f"Error decrypting/executing: {e}")\n')
        f.write('    sys.exit(1)\n')
    
    if os.name != 'nt':
        os.chmod(output_path, 0o755)

    print("")
    print(f"{GREEN_TERANG}[✓] SUCCESSFULLY ENCRYPTED BY JUNED{RESET}")
    print(f"{GREEN_TERANG}[!] DIRECTORY: {asli}")
    print(f"{GREEN_TERANG}[!] ORIGINAL FILE: {file_asli}")
    print(f"{GREEN_TERANG}[!] ENCRYPTED FILE: {after_sex}")
    print(f"{GREEN_TERANG}[!] KEY USED: {key}")
    print(f"{GREEN_TERANG}[!] FILE SIZE: {len(encoded_data)} characters")
    print("")
    input(f"\n{GREEN_TERANG}PRESS ENTER FOR BACK TO MENU: {RESET}{BG_MERAH}{YELLOW_TERANG}ENTER{RESET}")

def html_encode():
    os.system('clear')
    print("")
    print(f"""
        \033[1;30m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⢫⡌⣿⣿⢉⣤⠹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣜⠗⠉⠙⠘⠻⢡⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣥⡀⠀⢀⡠⣐⣸⣿⡿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
        \033[1;37m⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠇⠉⠒⠶⠉⠀⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣠⣿⠃⠀⠀⠀⠁⠀⠀⠀⠀⢻⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣦⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡆⠀⠀⠀⠀\033[0m
        \033[1;33m⠀⠀⠀⠀⢀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀
        ⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀
        ⠀⠀⠀⡸⠋⠛⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢼⣿⣿⣿⣿⠃⠀⠀⠀\033[0m
        \033[1;30m⡐⠀⠈⠀⠀⠀⠈⢻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡿⠿⠃⠀⠀⠀⠀
        ⢡⠀⠀⠀⠀⠀⠀⠀⠻⣿⠷⠀⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠐⠠⡀
        ⡄⠀⠀⠀⠀⠀⠀⠀⠀⠑⣄⠀⠀⠀⠀⣀⣤⣾⣿⠀⠀⠀⠀⠀⠀⠀⣀⡠⠃
        ⠒⠠⠤⣀⣄⡀⠀⠀⢀⣰⣿⠿⠿⠿⠿⠿⠿⠿⣿⡄⠀⠀⢀⡠⠔⠉⠀⠀⠀
        ⠀⠀⠀⠀⠀⠉⠙⠻⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠿⠋⠀⠀⠀⠀⠀⠀\033[0m
{RESET}{CYAN_TERANG}╦ ╦ ╔╦╗ ╔╦╗ ╦       ╔═╗ ╔╗  ╔═╗ ╦ ╦ ╔═╗ ╔═╗ ╔═╗ ╔╦╗ ╔═╗
{RESET}{CYAN_TERANG}╠═╣  ║  ║║║ ║       ║ ║ ╠╩╗ ║╣  ║ ║ ╚═╗ ║   ╠═╣  ║  ║╣ 
{RESET}{CYAN_TERANG}╩ ╩  ╩  ╩ ╩ ╩═╝     ╚═╝ ╚═╝ ╚   ╚═╝ ╚═╝ ╚═╝ ╩ ╩  ╩  ╚═╝{RESET}""")
    print("")
    print(f"[{BG_MERAH}{YELLOW_TERANG}INFO{RESET}]{PUTIH_TERANG}THIS TOOLS FOR HTML ENCODE ")

def main_html_encode():
    html_encode()
    print("")
    idiot = input(f"{CYAN_TERANG}ENTER YOUR FILEPATH: {RESET}")
    bego = input(f"{CYAN_TERANG}ENTER YOUR OUTPUT: {RESET}")

    if not os.path.exists(idiot):
        print(f"{MERAH_TERANG}[×] FILEPATH GA DI TEMUKAN{RESET}")
        input(f"{MERAH_TERANG}TEKAN ENTER BUAT BALIK MENU: {RESET}{BG_MERAH}{PUTIH_TERANG}ENTER{RESET}")
    
    with open(idiot, "rb") as f:
        dec = f.read()

    base_code = base64.b64encode(dec).decode("utf-8")

    base_dir = os.path.dirname(idiot)
    name = os.path.basename(idiot)
    af = os.path.join(base_dir, bego)

    with open(af, "w") as f:
        f.write('<#!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<body>\n')
        f.write('<script>')
        f.write(f'document.write(atob("{base_code}"))\n')
        f.write('</script>\n')
        f.write('</body>\n')
        f.write('</html>')

    print(f"{GREEN_TERANG}[✓] SUCCES ENCRYPTED BY JUNED{RESET}")
    print(f"{GREEN_TERANG}[!] DIRECTORY {base_dir}{RESET}")
    print(f"{GREEN_TERANG}[!] BEFORE ENCRYPT: {name}{RESET}")
    print(f"{GREEN_TERANG}[!] AFTER ENCRYPT: {af}{RESET}")
    print("")
    input(f"\n{GREEN_TERANG}TEKAN ENTER BUAT KEMBALI: {RESET}{BG_MERAH}{YELLOW_TERANG}ENTER{RESET}")
    
def main():
    while True:
        banner()
        print("")
        pilih = input(f"{CYAN_TERANG}PILIH MAU YANG MANA: {RESET}")

        if pilih == "1":
            enc()
        elif pilih == "2":
            kontol()
        elif pilih == "3":
            decode()
        elif pilih == "4":
            gatau()
        elif pilih == "5":
            main_js_encode()
        elif pilih == "6":
            main_bash()
        elif pilih == "7":
            xor_encrypt_main()
        elif pilih == "8":
            main_html_encode()
        elif pilih == "9":
            os.system("xdg-open https://t.me/usersjuned")
        elif pilih == "10":
            os.system("xdg-open https://whatsapp.com/channel/0029Vb7fs8bA89MaZwiKhE0t")
        elif pilih == "11":
            print(f"{MERAH}👋 MAKASEH UDH GUNAI TOOLS INI{RESET}")
            time.sleep(1)
            break
        elif pilih == "12":
            print(f"{MERAH}❌ pilihan ga valid lagi anjing{RESET}")
            print("")
            input(f"{CYAN_TERANG}TEKAN ENTER BUAT KEMBALI KE MENU: {RESET}{BG_BLUE}{PUTIH_TERANG}ENTER{RESET}")
            time.sleep(0.1)
            return
        else:
            print(f"{MERAH_TERANG}❌ PILIHAN GA VALID KELUAR DARI TOOLS...")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()

