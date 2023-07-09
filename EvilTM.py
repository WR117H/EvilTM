import tempfile
import os
from module import banner
import subprocess
import hashlib
from Cryptodome.Hash import MD4
from time import sleep
from datetime import datetime
from colorama import Fore
from module import function
import argparse

parser = argparse.ArgumentParser(description=banner.disc())
parser.add_argument('--sam', type=str, help='sam file with save format ')
parser.add_argument('--system', type=str, help='system file with save format')
args = parser.parse_args()



sam_file = args.sam
system_file = args.system
os.system("clear")
banner.ban()

def main():

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
    main()
