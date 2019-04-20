import datetime
import threading

from colorama import init, Fore


lock = threading.Lock()

try:
    init()
except:
    pass


def info(output: str):
    lock.acquire()
    print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now().strftime('%H-%M-%S %d/%m/%y'))}{Fore.RESET} {Fore.CYAN}[INFO]{Fore.RESET} {output}")
    lock.release()
    return


def exception(output: object):
    lock.acquire()
    print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now().strftime('%H-%M-%S %d/%m/%y'))}{Fore.RESET} {Fore.MAGENTA}[EXCEPTION]{Fore.RESET} {output}")
    lock.release()
    return


def warn(output: str):
    lock.acquire()
    print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now().strftime('%H-%M-%S %d/%m/%y'))}{Fore.RESET} {Fore.RED}[WARNING]{Fore.RESET} {output}")
    lock.release()
    return


def alert(output: str):
    lock.acquire()
    print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now().strftime('%H-%M-%S %d/%m/%y'))}{Fore.RESET} {Fore.YELLOW}[ALERT]{Fore.RESET} {output}")
    lock.release()
    return


def bulle(address: str, output: int):
    lock.acquire()
    print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now().strftime('%H-%M-%S %d/%m/%y'))}{Fore.RESET} [{address}] {Fore.MAGENTA}[BULLE]{Fore.RESET} {str(output)}")
    lock.release()
    return
