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
    def __max_length(self) -> int :
        return self.__max_length
    

    def set_value(self, index : int, new_value : Any) -> None :
        if index >= self.__max_length:
            raise IndexError(f"Index ({index}) is not valid, this object limit is '{self.limit}'")

        tempList = list(self.__limitedList)
        tempList[index] = new_value

        self.__limitedList = tuple(tempList)


    def getList(self, showDefaultValue : bool = False) -> list :
        if showDefaultValue:
            return list(self.__limitedList)
        else:
            toReturn = []

            for element in self.__limitedList:
                if element != self.__defaultValue:
                    toReturn.append(element)

            return toReturn



if __name__ == "__main__":
    print(isinstance(None, object))

# REVOIR L'ALGO DE TOUT CE BORDEL ET CHANGER SI BESOIN, IDEM POUR LES AUTRES FICHIERS
