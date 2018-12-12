import os

from UI.SystemSpecificUI import SystemSpecificUI

class DisplayHeader:

    def __init__(self):
        self._system = SystemSpecificUI()

    def display_header(self):
        """Displays the header for the main menu"""
        self._system.clear_screen()
        print(  "\t ______                         _                 ______               ______                        _ \n"#Create a seperate function called displayTitlebar
                "\t(____  \                       (_)               / _____)             (_____ \             _        | |\n"
                "\t ____)  ) ____ ____  ____  ____ _ ____  ____    | /      ____  ____    _____) ) ____ ____ | |_  ____| |\n"
                "\t|  __  ( / ___) _  |/ _  |/ _  | |  _ \|  _ \   | |     / _  |/ ___)  (_____ ( / _  )  _ \|  _)/ _  | |\n"
                "\t| |__)  ) |  ( ( | ( ( | ( ( | | | | | | | | |  | \____( ( | | |            | ( (/ /| | | | |_( ( | | |\n"
                "\t|______/|_|   \_||_|\_|| |\_|| |_|_| |_|_| |_|   \______)_||_|_|            |_|\____)_| |_|\___)_||_|_|\n"
                "\t                   (_____(_____|                                                                       \n"
                "\t************************blow your horn on a car from Bragginn car rental!******************************\n"
                )

    def display_header_rentals(self):
        """Displays the header for the rentals menu"""
        self._system.clear_screen()
        print(  "\t ______                        _         ______                    \n"
                "\t(_____ \             _        | |       |  ___ \                   \n"
                "\t _____) ) ____ ____ | |_  ____| | ___   | | _ | | ____ ____  _   _ \n"
                "\t(_____ ( / _  )  _ \|  _)/ _  | |/___)  | || || |/ _  )  _ \| | | |\n"
                "\t      | ( (/ /| | | | |_( ( | | |___ |  | || || ( (/ /| | | | |_| |\n"
                "\t      |_|\____)_| |_|\___)_||_|_(___/   |_||_||_|\____)_| |_|\____|\n"
                )


    def display_header_fleet(self):
        """Displays the header for the fleets menu"""
        self._system.clear_screen()
        print(  "\t _______ _                    ______                    \n"
                "\t(_______) |           _      |  ___ \                   \n"
                "\t _____  | | ____ ____| |_    | | _ | | ____ ____  _   _ \n"
                "\t|  ___) | |/ _  ) _  )  _)   | || || |/ _  )  _ \| | | |\n"
                "\t| |     | ( (/ ( (/ /| |__   | || || ( (/ /| | | | |_| |\n"
                "\t|_|     |_|\____)____)\___)  |_||_||_|\____)_| |_|\____|\n"
                )

    def display_header_customer(self):
        """Displays the header for the customer menu"""
        self._system.clear_screen()
        print(  "\t  ______                                          ______                    \n"
                "\t / _____)          _                             |  ___ \                   \n"
                "\t| /     _   _  ___| |_  ___  ____   ____  ____   | | _ | | ____ ____  _   _ \n"
                "\t| |    | | | |/___)  _)/ _ \|    \ / _  )/ ___)  | || || |/ _  )  _ \| | | |\n"
                "\t| \____| |_| |___ | |_| |_| | | | ( (/ /| |      | || || ( (/ /| | | | |_| |\n"
                "\t \______)____(___/ \___)___/|_|_|_|\____)_|      |_||_||_|\____)_| |_|\____|\n"
                )