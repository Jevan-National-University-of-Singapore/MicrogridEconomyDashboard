from __future__ import annotations

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class QTreeNode(QObject):
    dataChanged = Signal()
    parentNodeChanged = Signal()
    childrenNodesChanged = Signal()

    def __init__(self, 
        data: str, 
        parent_node: QTreeNode|None = None,
        children_nodes: list[QTreeNode]|None = None
    ):
        super().__init__()
        self.data_:str = data
        self.parent_node:QTreeNode = parent_node
        self.children_nodes:list[QTreeNode] = [] if children_nodes is None else children_nodes
        
        self.all_children_count = 0
        if children_nodes:
            for child in children_nodes:
                self.all_children_count += child.all_children_count

        self.depth:int = 1 + max(self.children, key=lambda child: child.depth).depth if children_nodes else 1

    @Property(str, notify=dataChanged) #getter
    def data(self) -> str:
        return self.data_
    
    @Property(QObject, notify=parentNodeChanged) #getter
    def parentNode(self) -> QObject:
        return self.parent_node

    @Property(list, notify=childrenNodesChanged) #getter
    def childrenNodes(self) -> list:
        return self.children_nodes
    
    def add_children(self, children:QTreeNode|list[QTreeNode]):
        if isinstance(children, QTreeNode):
            children = [children]

        for child in children:
            child.parent_node = self

        self.children_nodes.extend(children)
        self.depth += max(self.children_nodes, key=lambda child: child.depth).depth

    def is_root(self):
        return self.parent_node is None

    def is_leaf(self):
        return len(self.children_nodes) == 0