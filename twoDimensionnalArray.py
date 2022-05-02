# TDA means "Two Dimensionnal Array", it's an abreviation
class TDA:
    
    def __init__(self, length : int, width : int, fillWith : object = None) -> None :
        if type(length) != int:
            raise ValueError("'length' parameter is not 'int' instance")
        elif type(width) != int:
            raise ValueError("'width' parameter is not 'int' instance")

        if length < 1:
            raise ValueError(f"Array cannot be {length} unity long")
        elif length < 1:
            raise ValueError(f"Array cannot be {width} unity wide")


        self.__length = length
        self.__width = width

        self.__tda = [[fillWith for x in range(self.__length)] for y in range(self.__width)]


    def getObject(self, x : int, y : int) -> object :
        return self.__tda[x][y]
    

    def getTDA(self) -> list[list[object]] :
        return self.__tda


    def getLength(self) -> int :
        return self.__length


    def getWidth(self) -> int :
        return self.__width


    def formatArray(self) -> str :
        formattedString = "[\n"

        for array in self.__tda:
            formattedString += f"\t{array},\n"

        formattedString += "]"

        return formattedString


if __name__ == "__main__":
    tda = TDA(10, 10)
    print(tda.formattedArray())

