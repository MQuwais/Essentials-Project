from arm.ansi.font import *
from arm.banner import *
from system.clear import *

class AuxiliaryScanner:
    def Listing():
        while True:
            cclear()
            Banner()

            # MODUL!!
            print("""
NO   Modules            Descriptions
=======================================================================================
1    sqli_vuln          crawl the sqli vulnerable on the websites
            """)
