from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Pair:
    __first: Any
    __second: Any
    
    
    @property
    def first(self) -> Any :
        """Get first value

        Returns:
            Any: first value
        """
        
        return self.__first
    
    
    @property
    def second(self) -> Any :
        """Get second value

        Returns:
            Any: second value
        """
        
        return self.__second
    
    
    @property
    def pair_tuple(self) -> tuple[Any, Any] :
        """Get pair tuple

        Returns:
            tuple[Any, Any]: tuple of first and second value
        """
        
        return (self.__first, self.__second)
    
    
    def set_first(self, new_value : Any) -> None :
        """Sets first value

        Args:
            new_value (Any): new value
        """
        
        self.__first = new_value
        
    
    def set_second(self, new_value : Any) -> None :
        """Sets second value

        Args:
            new_value (Any): new value
        """
        
        self.__second = new_value
        


if __name__ == "__main__":
    print("Chuck Norris won at rock paper scissors against a mirror.")
