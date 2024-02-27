import requests
from termcolor import colored
import ipaddress
import random

def generate_random_ip():
    # Gera um endereço IP aleatório
     return colored(str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1))), 'red')

# ... (Funções de verificação de vulnerabilidades)

def scan_website(url):
    print(f"\nVarrendo: {url}")
    print(check_sql_injection(url))
    print(check_xss(url))
    print(check_csrf(url))
    print(check_ssrf(url))
    print(check_lfi(url))
    print(check_rce(url))

# URL do seu Telegram (substitua com o seu link real)
telegram_link = "https://t.me/gbr0004"

def main_menu():
    print("\nMain menu:")
    print("[1] Perform new scan")
    print("[2] Batch scan from .txt file")
    print("[3] Exit the program")

def perform_batch_scan(file_name):
    try:
        with open(file_name, 'r') as file:
            urls = file.read().splitlines()

        for url in urls:
            # Verifica se o link é válido antes de realizar a varredura
            if is_valid_url(url):
                scan_website(url)
            else:
                print(f"invalid link: {url}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error performing batch scan: {str(e)}")

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def main():
    print("\033[91m")

art = f'''
{colored("██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗", 'red')}
{colored("██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝", 'yellow')}
{colored("██████╔╝█████╗  ██║  ██║███████╗█████╗  ██║", 'green')}
{colored("██╔══██╗██╔══╝  ██║  ██║╚════██║██╔══╝  ██║", 'cyan')}
{colored("██║  ██║███████╗██████╔╝███████║███████╗╚██████╗", 'blue')}
{colored("╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝  v1", 'magenta')}
{colored("    MY TELEGRAM: ", 'white')}{colored(telegram_link, 'blue')}
{colored("    YOUR IP: ", 'white')}{colored(generate_random_ip(), 'red')}
'''

print(art)

while True:
        main_menu()
        opcao = input("Choose an option (1, 2 or 3): ")

        if opcao == '1':
            user_url = input("Enter the website URL:  ")
            try:
                print("\nsweeping...")
                scan_website(user_url)
            except:
                print("Something went wrong. Check the URL and try again.")
        elif opcao == '2':
            file_name = input("Enter the name of the .txt file: ")
            print("\nVarrendo em lote...")
            perform_batch_scan(file_name)
        elif opcao == '3':
            print("Leaving the tool...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
