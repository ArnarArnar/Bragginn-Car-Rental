"""Class for OS specific commands"""

import os
import platform

class SystemSpecificUI:

    def clear_screen(self):
        """Clear screen for most common operating systems"""
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Darwin':
            os.system('clear')
        elif platform.system() == 'Linux':
            os.system('clear')
    
    def pause_system(self):
        """Pause system for most common operating systems"""
        if platform.system() == 'Windows':
            os.system('pause')
        else:
            input("Press enter to continue...")


