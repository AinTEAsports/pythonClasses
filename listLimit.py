from typing import Any, Tuple
from dataclasses import dataclass, field


class SizeError(Exception):
    pass



@dataclass(kw_only=True)
class LimitedList:
    __array: tuple[Any] = field(default_factory=tuple)
    __max_length: int


    def __post_init__(self) -> None :
        """Post init function

        Args:
            array (tuple[Any], optional): list given. Defaults to '()'.
            max_length (int): list max length

        Raises:
            ValueError: if the max length is less than 0
        """

        if self.__max_length < 0:
            raise ValueError("You can't set max value to 0 or beneath")
        
        if len(self.__array) > self.__max_length:
            raise SizeError("The list is too long")


    @property
    def tuple_array(self) -> tuple[Any] :
        return self.__array
    
    
    @property
    def list_array(self) -> list :
        return list(self.__array)
    
    
    @property
    def max_length(self) -> int :
        return self.__max_length


    @property
    def size(self) -> int :
        return len(self.tuple_array)


    def set_array(self, new_tuple : tuple[Any]) -> None :
        if len(new_tuple) > self.max_length:
            raise SizeError("size of new tuple is greater than authorized")
        
        if not isinstance(new_tuple, tuple):
            raise TypeError("new tuple has not tuple type")
        
        self.__array = new_tuple


    def set_value(self, index : int, new_value : Any) -> None :
        if index >= self.__max_length:
            raise IndexError(f"Index ({index}) is not valid, this object limit is '{self.max_length}'")
        elif index < 0:
            raise IndexError("index cannot be beneath 0")

        temp_list = self.list_array
        temp_list[index] = new_value

        self.__array = tuple(temp_list)
        
        
    def add(self, value : Any) -> None :
        if len(self.tuple_array) == self.max_length:
            return SizeError("array is already at maximum size")
        
        temp_list = self.list_array
        temp_list.append(value)
        
        self.__array = tuple(temp_list)
        
    
    def insert(self, index : int, value : int) -> None :
        if len(self.tuple_array) == self.max_length:
            return SizeError("array is already at maximum size")
        
        temp_list = self.list_array
        temp_list.insert(index, value)
        
        self.__array = tuple(temp_list)


    def pop(self, index : int = -1) -> Any :
        temp_list = self.list_array
        return_value = temp_list.pop(index)
        
        self.__array = tuple(temp_list)
        
        return return_value
    
    
    def clear(self) -> None :
        self.__array = ()



if __name__ == "__main__":
    print("When Chuck Norris goes out, the one who wears a mask is Coronavirus")

# REVOIR L'ALGO DE TOUT CE BORDEL ET CHANGER SI BESOIN, IDEM POUR LES AUTRES FICHIERS
