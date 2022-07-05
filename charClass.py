class NotACharError(Exception):
    pass


class NonModifiableError(Exception):
    pass



class Char:

    def __init__(self, char: str = '', constant: bool = False) -> None :
        """Initializer of class 'Char'

        Args:
            char (str): the... char ? I don't know how to be more precise
            constant (bool): if set to 'True', cannot be modified

        Raises:
            NotACharError: if the length of 'char' is greater than 1, then it is not a char
        """

        if len(char) > 1:
            raise NotACharError(f"'{char}' is not a char because its length is greater than 1")

        self.__const = constant
        self.__char = char


    @property
    def is_empty(self) -> bool :
        """Returns if the char is empty

        Returns:
            (bool): returns True if the length of the char is 0, or if it is equal to empty string
        """

        # Could also do :
        # return self.__char == ''
        return len(self.__char) == 0


    @property
    def ascii_code(self) -> int :
        """Returns current char ASCII code

        Returns:
            (int): the ASCII code for current char
        """

        return ord(self.__char)


    @property
    def string(self) -> str :
        """Returns a copy of the char

        Returns:
            (str): a copy of the current char
        """

        return self.__char


    @property
    def length(self) -> int :
        """Returns the length of the char

        Returns:
            (int): the length of the char
        """

        return len(self.__char)


    def set(self, new_char: str) -> None :
        """Set the actual char to a new char

        Args:
            new_char (str): the new char you want to assign

        Raises:
            NonModifiableError: if in constructor 'constant' was set to True, will raise an error
            NotACharError: if the char length is over 1, then it's not a char
        """

        if self.__const:
            raise NonModifiableError("current object is not modifiable, but you can make it modifiable by setting 'constant' to 'False' in constructor")

        if len(new_char) > 1:
            raise NotACharError(f"'{new_char}' is not a char because its length is greater than 1")

        self.__char = new_char


    def clear(self) -> None :
        """Clears the actual char, inother words it sets thechar to empty string
        """

        self.set('')
