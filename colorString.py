import colorama
import termcolor


class ColoredString(str):

    def __init__(self, string: str = "") -> None:
        self.string = string

        self.__colors = {
            "red" : colorama.Fore.RED,
            "lightred" : colorama.Fore.LIGHTRED_EX,

            "green" : colorama.Fore.GREEN,
            "lightgreen" : colorama.Fore.LIGHTGREEN_EX,

            "blue" : colorama.Fore.BLUE,
            "lightblue" : colorama.Fore.LIGHTBLUE_EX,

            "white" : colorama.Fore.WHITE,
            "lightwhite" : colorama.Fore.LIGHTWHITE_EX,

            "black" : colorama.Fore.BLACK,
            "lightblack" : colorama.Fore.LIGHTBLACK_EX,

            "cyan" : colorama.Fore.CYAN,
            "lightcyan" : colorama.Fore.LIGHTCYAN_EX,

            "yellow" : colorama.Fore.YELLOW,
            "lightyellow" : colorama.Fore.LIGHTYELLOW_EX,

            "magenta" : colorama.Fore.MAGENTA,
            "lightmagenta" : colorama.Fore.LIGHTMAGENTA_EX,
        }


        self.__secondColors = colors = {
            'ITALIC' : '\033[3m',
            'BOLD' : '\033[1m',
            'RED' : '\033[1;91m',
            'BLUE' : '\033[1;94m',
            'GREEN' : '\033[92m',
            'YELLOW' : '\033[1;93m',
            'END' : '\033[0m',
        }


    def colorText(self, color : str, fromwhere : int = 0, toWhere : int = -1, changeDefaultString : bool = False) -> str:
        if not self.colorExists(color):
            raise ValueError(f"Color '{color}' does not exists, to check if a color exits, you can check the method 'colorExits'")

        coloredstr = f"{self.__colors[color]}{self.string}{colorama.Fore.RESET}"

        if changeDefaultString:
            self.string = coloredstr

        return coloredstr


    def colorExists(self, color: str) -> bool:
        return color in self.colorList()


    def colorList(self) -> list[str]:
        return [color for color in self.__colors.keys()]



colortxt = ColoredString("Hello World !")
print(colortxt.colorText("lightwhite", changeDefaultString=True))
print(colortxt.colorList())
