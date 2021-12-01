from arm.ansi.font import *
from arm.banner import *
from system.clear import *

class AuxiliaryAdmin:
    def Listing():
        while True:
            cclear()   
            Banner()

            # MODUL!!
            print("""
NO   Modules            Descriptions
=======================================================================================
1    login_finder       find the login pages of the website
            """)
