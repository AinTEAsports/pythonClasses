class LimitedList(tuple):

    def __init__(self, limit : int, preList : list=None, fillWith=None):
        if limit <= 0:
            raise ValueError("You can't set max value to 0 or beneath")

        # By default, all list elements will be None
        if not preList:
            preList = [fillWith] * limit

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
        if showDefaultValue:
            return self.__limitedList
        else:
            toReturn = []

            for element in self.__limitedList:
                if element != self.__defaultValue:
                    toReturn.append(element)

            return tuple(toReturn)

        return self.__limitedList


    def getLimit(self) -> int :
        return self.limit


if __name__ == "__main__":
    lim = LimitedList(limit=5)
    lim.setValue(1, 'Prout')
    print(lim.getTuple())
    print(lim.getList())

