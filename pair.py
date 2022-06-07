from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Pair:
    __first: Any
    __second: Any
    
    
    @property
    def first(self) -> Any :
        return self.__first
    
    
    @property
    def second(self) -> Any :
        return self.__second
    
    
    @property
    def pair_tuple(self) -> tuple:
        return (self.__first, self.__second)
    
    
    def set_first(self, new_value : Any) -> None :
        self.__first = new_value
        
    
    def set_second(self, new_value : Any) -> None :
        self.__second = new_value
        
