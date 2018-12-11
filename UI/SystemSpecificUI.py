"""Class for OS specific commands"""

import os
import platform

class SystemSpecificUI:

    def clear_screen(self):
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Darwin':
            os.system('clear')
        elif platform.system() == 'Linux':
            os.system('clear')
    
    def pause_system(self):
        if platform.system() == 'Windows':
            os.system('pause')
        else:
            input("Press enter to continue...")


