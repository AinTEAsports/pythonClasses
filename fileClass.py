import os


class File:

    def __init__(self, filename : str, createNew : bool = False) -> None :
        if not os.path.exists(filename) or createNew:
            with open(filename, 'w') as f:
                f.write("")

        self.__filename = filename
        self.__absolutePath = os.path.abspath(self.__filename)


    def write(self, text : str) -> None :
        if not text:
            return

        with open(self.__filename, 'w') as f:
            f.write(text)


    def append(self, text : str) -> None :
        if not text:
            return

        with open(self.__filename, 'a') as f:
            f.write(text)


    def read(self, encoding : str = 'utf-8') -> str :
            return open(self.__filename, 'r', encoding=encoding).read()


    def binaryRead(self) -> str :
        return open(self.__filename, 'rb').read()


    def getLines(self, encoding : str = 'utf-8') -> str :
        return self.read(encoding=encoding).split('\n')

