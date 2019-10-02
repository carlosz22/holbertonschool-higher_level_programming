#!/usr/bin/python3
"""
"""


class Node:
    """
    """
    def __init__(self, data, next_node=None):
        """
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        """
        if not isinstance(next_node, Node) or next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node

class SinglyLinkedList:
    """
    """
    def __init__(self):
        """
        """
        self.__head = None

    def __str__(self):
        """
        """
        result = ""
        if self.__head is None:
            return result
        else:
            tmp = self.__head
            while tmp is not None:
                result += str(tmp.data)
                if tmp.next_node is not None:
                    result += "\n"
                tmp = tmp.next_node
            return result

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        tmp = self.__head
        if tmp.data >= value:
            new_node.next_node(tmp)
            self.__head = new_node
            return

        while tmp is not None:
            before = tmp
            if tmp.data >= value:
                new_node.next_node(before.next_node)
                before.new_node(new_node)
                return
            tmp = tmp.next_node
