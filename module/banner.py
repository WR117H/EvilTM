from colorama import Fore
import os

description="""
v1.0
EvilTM is a tool to crack NLTM hashes with sam.save 
and system.save to extract hash of windows password.
The newest version and documentation is always available at;
   [*] https://github.com/WR117H/EvilTM
"""

id="WR117H"
ascii=f"""
    ______      _ __________  ___
   / ____/   __(_) /_  __/  |/  /
  / __/ | | / / / / / / / /|_/ / 
 / /___ | |/ / / / / / / /  / /  
/_____/ |___/_/_/ /_/ /_/  /_/ 
"""

def ban():
   os.system("clear")
   print(Fore.LIGHTMAGENTA_EX+ascii+Fore.RESET)
def disc():
   print(description)
