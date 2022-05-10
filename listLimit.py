class LimitedList(tuple):

    def __init__(self, limit : int, preList : list = None, fillWith : object = None):
        """Init function

        Args:
            limit (int): list max length
            preList (list, optional): list given, if no. Defaults to None.
            fillWith (object, optional): _description_. Defaults to None.

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
