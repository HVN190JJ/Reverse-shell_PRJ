from colorama import init, Fore, Style
import logging

init(autoreset=True)

def print_banner() :
    "banner = f """
{Fore.GREEN}
  


{Style.RESET_ALL} 


print("SIGMA")

def setup_logger():
    logging.basicConfig(
        filename='shell_activity.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )

def log_activity(msg):
    logging.info(msg)            
