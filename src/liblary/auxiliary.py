from arm.ansi.font import *
from system.clear import *
from src.dialogues import *
from arm.banner import *
from src.liblary.dial.aux.scanner import *
from src.liblary.dial.aux.admin import *

import time

class Auxiliary:
    def first(self):
        while True:
            cclear()
            Banner()
            print("""
Choice Auxiliary Type
  1. Scanner
  2. Admin
  3. back
            """)
            x = input(Prompts.n+"Pentesting/Auxiliary"+Prompts.f)
            if x == "1":
                AuxiliaryScanner.Listing()
            elif x == "2":
                AuxiliaryAdmin.Listing()
            elif x == "3":
                Dialogues.pentest()
            else:
                print("[!] Invalid input")
                time.sleep(2)
