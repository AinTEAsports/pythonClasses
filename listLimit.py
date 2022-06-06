from typing import Any, Tuple
from dataclasses import dataclass, field


class SizeError(Exception):
    pass


@dataclass(kw_only=True)
class LimitedList:
    array: tuple[Any] = field(default_factory=tuple)
    max_length: int
    fill_with: Any = field(default=None)


    def __post_init__(self) -> None :
        """Post init function

        Args:
            array (tuple[Any], optional): list given. Defaults to '()'.
            max_length (int): list max length
            fillWith (object, optional): . Defaults to None.

        Raises:
            ValueError: _description_
        """
        
        if limit <= 0:
            raise ValueError("You can't set max value to 0 or beneath")
        
        # By default, all list elements will be None
        if not preList:
            preList = [fillWith] * limit
        elif preList and fillWith:
            preList += [fillWith] * (limit-len(preList))
        else:
            if len(preList) > limit:
                raise ValueError(f"'preList' parameter's length cannot be superior to 'limit' parameter")

        self.limit = limit
        self.__limitedList = preList
        self.__defaultValue = fillWith


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
