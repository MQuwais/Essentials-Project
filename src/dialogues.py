from arm.ansi.font import *
from system.dap import *
from system.clear import *
from arm.banner import *
from arm.data.prompts import *
from arm.data.data import *
from arm.data.version import *
from src.liblary.auxiliary import *

import time
import sys

class Dialogues:
    def awal():
        while True:
            cclear()
            Banner()
            print("""
\033[37mWelcome To Essentials Project \033[31m{0}
Choice activity you want to do
  1. Penetration Testing
  2. Exit
            """.format(Essentials.version))
            x = input(Prompts.esp)
            if x == "1":
                Dialogues.pentest()
            elif x == "2":
                DAP()
                sys.exit()
            else:
                print("[!] Invalid input")
                time.sleep(2)
    def pentest():
        while True:
            cclear()
            Banner()
            print("""
\033[37mChoice The module Category
  \033[37m1. \033[34mAuxiliary (\033[32m{0}\033[34m)
  \033[37m2. \033[31mExploit (\033[37m{1}\033[31m)
  \033[37m3. Back
            """.format(Data.auxiliary,Data.exploit))
            x = input(Prompts.n+"Pentesting"+Prompts.f)
            if x == "1":
                Auxiliary.first()
            elif x == "2":
                pass
            elif x == "3":
                Dialogues.awal()
            else:
                print("[!] Invalid input")
                time.sleep(2)
