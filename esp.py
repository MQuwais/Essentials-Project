from system.dap import *
from arm.ansi.font import *
from arm.data.version import *
from system.clear import *
from arm.data.prompts import *
from arm.banner import *
from arm.data.data import *
from src.liblary.auxiliary import *
from src.liblary.dial.aux.scanner import *
from src.liblary.dial.aux.admin import *

import sys

try:
    Dialogues.awal()
except KeyboardInterrupt:
    DAP()
    sys.exit()
