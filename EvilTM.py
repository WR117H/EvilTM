import subprocess
from time import sleep
from colorama import Fore
from module import function
import argparse

parser = argparse.ArgumentParser(description=banner.disc())
parser.add_argument('--sam', type=str, help='Sam file with save format ')
parser.add_argument('--system', type=str, help='System file with save format')
parser.add_argument('--hash', type=str, help='Hash of ')
args = parser.parse_args()


has8 = args.hash
sam_file = args.sam
system_file = args.system
banner.ban()

def main():
    if has8 != None and system_file != None and sam_file != None:
        print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" Cant use --hash with the others")
        exit()
    if has8 != None:
        function.nltm(has8,None)

    else:

        if system_file == None and sam_file == None:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" There is no sam or system file specified")
            exit()
        if sam_file == None:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" There is no sam file specified")
            exit()
        if system_file == None:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" There is no system file specified")
            exit()
        if system_file == None and sam_file == None:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" There is no sam or system file specified")
            exit()

        function.nltm(sam_file,system_file)
if __name__ == "__main__":
    try:

       main()
    except KeyboardInterrupt:
        banner.ban()
        sleep(0.1)
        print('\n'+Fore.LIGHTRED_EX+"[-]"+Fore.RESET+" Exiting . . .")
        sleep(0.1)
