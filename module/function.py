import tempfile
import os
from module import banner
import subprocess
import hashlib
from Cryptodome.Hash import MD4
from time import sleep
import time

from datetime import datetime
from colorama import Fore
import argparse

def nltm(sam_file,system_file):
    command = f"impacket-secretsdump -sam {sam_file} -system {system_file} LOCAL"
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    # Execute the command and capture the output
    output = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Split the output into lines
    lines = output.stdout.splitlines()

    # Iterate over the lines and print the relevant information
    li=[]
    for line in lines:
        if line.startswith("[*] Dumping local SAM hashes"):
            continue  # Skip the header line
        elif line[0:27] == ("[*] Target system bootKey: "):
            print(Fore.LIGHTMAGENTA_EX+'[^] '+Fore.RESET+'Target system bootKey: '+line[27:]+'\n')
        elif line[0:2]== '':
            continue
        elif line[0:41] == ("[-] [Errno 2] No such file or directory: "):
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+f" No such file or directory: {line[41:]}")
            exit()
        elif line[0:71] == ("[-] SAM hashes extraction failed: [Errno 2] No such file or directory: "):
            print(Fore.LIGHTRED_EX+"[-]"+Fore.RESET+f" SAM hashes extraction failed: [Errno 2] No such file or directory: {line[71:]}")
            exit()
        elif line[0:8]==("Impacket"):
            continue
        elif line.startswith("[*] Cleaning up"):
            break  # Stop iterating at the cleanup line
        elif line[-1] == ':':
            line = line.split(":")
            result = f"{line[0]}:{line[3]}"
            li.append(result)
            

            
        else:
            print(line)
    for i, s in enumerate(li):
       print("{}) {}".format(i+1, s))


# print(my_list[choice-1])
    print('')
    while True:
        Hash = int(input('Enter the specified hash > '))
        try:
            if li[Hash-1]:
               break
        except:
            print("Please enter a number that corresponds with the choices available.")
        


    Hash = li[Hash-1]
    Hash = Hash.split(":")
    Hash = Hash[1]
    passlist = input('Path of your password list > ')
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print('')
    sleep(0.6)
    result_file = f"result_{current_time}.txt"

    
    result = 0
    
    start_time = time.time()
    
    print(Fore.LIGHTGREEN_EX+"[$]"+Fore.RESET+" Cracking the hash . . .")
    with open(passlist, 'r') as f:
        # Loop through each password in the file
        num_passwords = sum(1 for _ in f)
        f.seek(0)  # Reset the file pointer to the beginnin
        count = 0
        for password in f:
            elapsed_time = time.time() - start_time
            if count > 0:
               avg_time_per_password = elapsed_time / count
               remaining_time = (num_passwords - count) * avg_time_per_password
            else:
               avg_time_per_password = 0
               remaining_time = 0
            if remaining_time < 60:
               remaining_time = f"{remaining_time:.2f} "
            elif remaining_time < 3600:
               minutes, remaining_time = divmod(remaining_time, 60)
               remaining_time = f"{int(minutes):02d}:{int(remaining_time):02d} " 
            elif remaining_time < 86400:
               hours, remaining_time = divmod(remaining_time, 3600)
               minutes, remaining_time = divmod(remaining_time, 60)
               remaining_time = f"{int(hours):02d}:{int(minutes):02d}:{int(remaining_time):02d} "
            else:
               days, remaining_time = divmod(remaining_time, 86400)
               hours, remaining_time = divmod(remaining_time, 3600)
               minutes, remaining_time = divmod(remaining_time, 60)
               remaining_time = f"{int(days):02d}:{int(hours):02d}:{int(minutes):02d}:{int(remaining_time):02d} "
            password = password.strip()
            lm_hash = hashlib.new('md4', password.encode('utf-16le')).digest()
            nt_hash = MD4.new(password.encode('utf-16le')).digest()
            new_ntlm_hash = lm_hash.hex()
            print('\r'+f"[{new_ntlm_hash}] | {remaining_time}remaining", end="    ")

            if str(new_ntlm_hash) == Hash:
                result+=1
                break
            count += 1

    if result == 1:
        print('\r'+Fore.LIGHTMAGENTA_EX+"[^] "+Fore.RESET+f"Hash cracked successfully [{Fore.LIGHTYELLOW_EX}{Hash}{Fore.RESET}:{Fore.LIGHTBLUE_EX}{password}{Fore.RESET}]",end=' ')
        with open(result_file, 'w') as f:
           f.write(Hash+":"+password)
           f.close()
        print('\n'+Fore.LIGHTYELLOW_EX+'[~] '+Fore.RESET+f"Result's been saved in {result_file}")
    else:
        print('\r'+Fore.LIGHTRED_EX+'[-] '+Fore.RESET+f"Couldn't crack the hash",end=' ')
