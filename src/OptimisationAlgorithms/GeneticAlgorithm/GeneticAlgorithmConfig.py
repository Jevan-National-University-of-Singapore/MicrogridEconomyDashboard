import sys
import os

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional


class GeneticAlgorithmConfig(QObject):

    def __init__(self,
            population_size:Optional[int] = 10,
            keep:Optional[int] = 5,
            number_of_generations:Optional[int] = 100,
            randomness:Optional[int] = 0.4
        ):
        super().__init__()
        self.population_size:int = population_size
        self.keep:int = keep
        self.number_of_generations:int = number_of_generations
        self.randomness:int = randomness
