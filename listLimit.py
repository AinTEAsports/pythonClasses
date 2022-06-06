from typing import Any, Tuple
from dataclasses import dataclass, field


class SizeError(Exception):
    pass



@dataclass(kw_only=True)
class LimitedList:
    array: tuple[Any] = field(default_factory=tuple)
    max_length: int


    def __post_init__(self) -> None :
        """Post init function

        Args:
            array (tuple[Any], optional): list given. Defaults to '()'.
            max_length (int): list max length

        Raises:
            ValueError: if the max length is less than 0
        """

        if self.max_length < 0:
            raise ValueError("You can't set max value to 0 or beneath")
        
        if len(self.array) > self.max_length:
            raise SizeError("The list is too long")


    def setValue(self, index : int, newValue):
        if index >= self.limit:
            raise IndexError(f"Index ({index}) is not valid, this object limit is '{self.limit}'")

        tempList = list(self.__limitedList)
        tempList[index] = newValue

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


    def getTuple(self, showDefaultValue : bool = False) -> tuple :
        if not showDefaultValue:
            return [element for element in self.__limitedList if element != self.__defaultValue]
        
        return self.__limitedList
        


    def getLimit(self) -> int :
        return self.limit


if __name__ == "__main__":
    print(isinstance(None, object))



# REVOIR L'ALGO DE TOUT CE BORDEL ET CHANGER SI BESOIN, IDEM POUR LES AUTRES FICHIERS
