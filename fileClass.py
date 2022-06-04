import os
import hashlib

from dataclasses import dataclass, field


@dataclass(frozen=True)
class File:
    __filename: str
    create_new: bool = False

    def __post_init__(self) -> None :
        """Post init function

        Args:
            filename (str): the file's name
            createNew (bool, optional): Parameter to know if we can overwrite an existing file. Defaults to False.
        """
        
        if not self.create_new and not os.path.exists(self.__filename):
            raise FileNotFoundError(f"file '{self.__filename}' not found, if you want to automatically create it, even it does not exists, make sure parameter 'createNew' is set up to 'True'")
        
        
        if not os.path.exists(self.__filename) and self.create_new:
            with open(self.__filename, 'w') as f:
                f.write("")
                
        del create_new

        
        @property
        def __absolute_path(self) -> str :
            return os.path.abspath(self.__filename)


    def write(self, text : str) -> None :
        """Method to write text in a file, it will overwrite the file. For not overwriting the file, use the 'append' method

        Args:
            text (str): the text to write in the file
        """
        
        if not text:
            return

        with open(self.__filename, 'w') as f:
            f.write(text)


    def append(self, text : str) -> None :
        """Method to write text in a file, it will not overwrite it, just append the text in the end of the file

        Args:
            text (str): the text to write in the file
        """

        if not text:
            return

        with open(self.__filename, 'a') as f:
            f.write(text)


    def read(self, encoding : str = 'utf-8') -> str :
        """Method to read the content of the file

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.

        Returns:
            str: the file's content
        """
        
        with open(self.__filename, 'r') as f:
            fileContent = f.read()

        return fileContent


    def binaryRead(self) -> str :
        """Method to read the content of the file, in binary

        Returns:
            str: the file's content, in binary
        """
        
        with open(self.__filename, 'rb') as f:
            binaryContent = f.read()
            
        return binaryContent


    def getLines(self, encoding : str = 'utf-8', delimitor : str = '\n') -> list[str] :
        """Method to get files lines

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.
            delimitor (str, optional): the delimitor between the lines. Defaults to '\\n'

        Returns:
            list[str]: a list containing the file's lines
        """
        
        return self.read(encoding=encoding).split(delimitor)


    def xorCrypt(self, password : str, outputFile : str) -> None :
        if outputFile == self.__filename:
            raise FileExistsError("You can't replace your actual file, for the moment...")

        hashedPasswd = hashlib.sha256(password.encode('utf-8')).digest()
        
        with open(self.__filename, 'rb') as f:
            with open(outputFile, 'wb') as f2:
                i = 0

                while f.peek():
                    c = ord(f.read(1))
                    j = i % len(hashedPasswd)
                    b = bytes([c^hashedPasswd[j]])
                    f2.write(b)

                    i += 1



if __name__ == "__main__":
    print("Chuck Norris has no dad, we do not f*ck Chuck Norris mother")
