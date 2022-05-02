import sys


class Vector:

    def __init__(self, vector : list = [], vectorType=None) -> None :
        if vectorType:
            self.__vectorType = vectorType
        else:
            if not len(vector):
                raise ValueError(f"Parameter 'vector' invalid, cannot get vector type if the list is empty")

            self.__vectorType = type(vector[0])

        for index, element in enumerate(vector):
            if type(element) != self.__vectorType:
                raise ValueError(f"Value number {index+1} is not same type as all the list")

        self.__vector = vector


    def append(self, toAppend) -> None :
        if type(toAppend) != self.__vectorType:
            raise ValueError(f"Parameter 'toAppend' ({toAppend}) not the good type (it should be '{self.__vectorType}' instead of '{type(toAppend)}')")

        self.__vector.append(toAppend)


    def clear(self) -> None :
        self.__vector = []


    def copy(self) -> list :
        return self.__vector[:]


    def count(self, value) -> int :
        occurences = 0

        for element in self.__vector:
            if element == value:
                occurences += 1

        return occurences
    

    def extend(self, iterable) -> None :
        for element in iterable:
            self.append(element)


    def index(self, value) -> int :
        for index, element in enumerate(self.__vector):
            if element == value:
                return index

        raise ValueError(f"Value '{value}' was not found in the vector")


    def insert(self, index : int, value) -> None :
        copiedVector = [None] * len(self.__vector)

        for i in range(len(copiedVector)):
            if index == i:
                copiedVector[i] = value
            else:
                copiedVector[i] = self.__vector[i]


    def pop(self, index : int = -1):
        return self.__vector.pop(index)
    

    def remove(self, value) -> None :
        for index, element in enumerate(self.__vector):
            if element == value:
                del self.__vector[index]
                return


    def removeAll(self, value) -> None :
        for index, element in enumerate(self.__vector):
            if element == value:
                del self.__vector[index]


    def reverse(self) -> None :
        self.__vector.reverse()


    def sort(self, key=None, reverse : bool = False) -> None :
        self.__vector.sort(key=key, reverse=reverse)


    def getType(self):
        return self.__vectorType
    

    def size(self) -> int :
        return sys.getsizeof(self.__vector)


    def typeSize(self, index : int = 0) -> int :
        return sys.getsizeof(self.__vector[index])


    def length(self) -> int :
        return len(self.__vector)


if __name__ == "__main__":
    va = Vector([1, 2, 3, 4, 5])

