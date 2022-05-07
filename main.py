import pyfiglet, os, re
from colorama import Fore, init
from multiprocessing.dummy import Pool as ThreadPool
import requests as req

red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

try:
    open("result.txt", "a")
except:
    pass

init(autoreset=True)

def __banner__():
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("Cpanel-Checker", font="slant", justify="center")
    print(f"{red}{my_banner}")
    print(f"{cyan}\t\t\t[ {white}Created By X-MrG3P5 {cyan}]\n")

def CpanelChecker(domain):
    try:
        req_data = req.get("http://"+ domain + ":2083", timeout=3)
        if req_data.status_code == 200:
            print(f"{cyan}[{green}200{cyan}] {white}{domain}:2083")
            open("result.txt", "a").write(domain + ":2083" + "\n")
        else:
            print(f"{cyan}[{red}BAD{cyan}] {white}{domain}:2083")
    except:
        print(f"{cyan}[{red}BAD{cyan}] {white}{domain}:2083")

if __name__=="__main__":
    __banner__()
    input_list = open(input(f"{cyan}[{white}?{cyan}] {white}Domain List : ")).read().replace("http://", "").replace("https://", "")
    domain_fixer = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', input_list)
    Thread = input(f"{cyan}[{white}?{cyan}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(CpanelChecker, domain_fixer)
    pool.close()
    pool.join()
