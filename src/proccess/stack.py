from copy import copy
from typing import Any, TypeVar

TypeNode = TypeVar("TypeNode")

class Node():
    def __init__(self, data: Any) -> None:
        self.__data = copy(data)
        self.__next = None

    def setNext(self, next: TypeNode | None = None) -> None:
        self.__next = next

    def getNext(self) -> TypeNode | None:
        return self.__next
    
    def setData(self, data: Any) -> None:
        self.__data = data

    def getData(self) -> Any:
        return self.__data        

    def __repr__(self) -> str:
        return f"{self.__data}"
    

class Stack():
    def __init__(self) -> None:
        self._length: int = 0
        self._last: Node | None = None
        self._first: Node | None = None

    @property
    def length(self) -> int:
        return self._length

    def push(self, data: Any) -> None:
        node = Node(data)
        node.setNext(self._first)
        self._first = node
        
        if self._last is None:
            self._last = node
        
        self._length += 1

    def pop(self) -> Any:
        node = self._first
        data = node.getData()
        self._first = self._first.getNext() 

        if node == self._last:
            self._last = None

        self._length -= 1

        del node
        return data
    
    def clear(self) -> None:
        while self._first != self._last:
            node = self._first
            self._first = self._first.getNext()
            del node

        node = self._first
        self._first = self._last = None
        del node

    def __str__(self) -> str:
        node = self._first
        st = ""

        while node != None:
            if node == None:
                st = "null"
                break
            elif node == self._first:
                st = f"{node.getData()}"
            else:
                st = f"{st}, {node.getData()}"
            
            node = node.getNext()
            
        return f"[{st}]" 
    
