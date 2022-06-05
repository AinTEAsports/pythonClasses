import os
import hashlib

from dataclasses import dataclass


@dataclass(frozen=True)
class File:
    __filename: str
    create_new: bool = False

    def __post_init__(self) -> None :
        """Post init function

        Raises:
            FileNotFoundError: if the file was not found.
                If you want to escape this error set arg
                'create_new' to 'True' in initializer
        """
        
        if not self.create_new and not os.path.exists(self.__filename):
            raise FileNotFoundError(f"file '{self.__filename}' not found, if you want to automatically create it, even it does not exists, make sure parameter 'createNew' is set up to 'True'")
        
        
        if not os.path.exists(self.__filename) and self.create_new:
            with open(self.__filename, 'w') as f:
                f.write("")
                
        del self.create_new


        @property
        def __absolute_path(self) -> str :
            return os.path.abspath(self.__filename)


    def write(self, text : str, encoding : str = "utf-8") -> None :
        """Method to write text in a file, it will overwrite the file. For not overwriting the file, use the 'append' method

        Args:
            text (str): the text to write in the file
        """
        
        if not text:
            return

        with open(self.__filename, 'w', encoding=encoding) as f:
            f.write(text)


    def append(self, text : str, encoding : str = "utf-8") -> None :
        """Method to write text in a file, it will not overwrite it, just append the text in the end of the file

        Args:
            text (str): the text to write in the file
        """

        if not text:
            return

        with open(self.__filename, 'a', encoding=encoding) as f:
            f.write(text)


    def read(self, encoding : str = 'utf-8', ignore_errors : bool = False) -> str :
        """Method to read the content of the file

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.

        Returns:
            str: the file's content
        """
        
        if ignore_errors:
            with open(self.__filename, 'r', encoding=encoding, errors="ignore") as f:
                file_content = f.read()
        else:
            with open(self.__filename, 'r', encoding=encoding) as f:
                file_content = f.read()

        return file_content


    def binary_read(self) -> str :
        """Method to read the content of the file, in binary

        Returns:
            str: the file's content, in binary
        """
        
        with open(self.__filename, 'rb') as f:
            binary_content = f.read()
            
        return binary_content


    def get_lines(self, encoding : str = 'utf-8', delimitor : str = '\n') -> list[str] :
        """Method to get files lines

        Args:
            encoding (str, optional): the encoding you want to read the file with. Defaults to 'utf-8'.
            delimitor (str, optional): the delimitor between the lines. Defaults to '\n'

        Returns:
            list[str]: a list containing the file's lines
        """
        
        return self.read(encoding=encoding).split(delimitor)


    def xor_crypt(self, password : str, output_filename : str) -> None :
        if output_filename == self.__filename:
            raise FileExistsError("You can't replace your actual file, for the moment...")

        hashed_password = hashlib.sha256(password.encode('utf-8')).digest()
        
        with open(self.__filename, 'rb') as f:
            with open(output_filename, 'wb') as f2:
                i = 0

                while f.peek():
                    c = ord(f.read(1))
                    j = i % len(hashed_password)
                    b = bytes([c^hashed_password[j]])
                    f2.write(b)

                    i += 1



if __name__ == "__main__":
    print("Chuck Norris has no dad, we do not f*ck Chuck Norris mother")
