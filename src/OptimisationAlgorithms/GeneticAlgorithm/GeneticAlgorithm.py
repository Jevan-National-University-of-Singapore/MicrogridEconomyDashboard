import sys
import os

from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import numpy as np
from scipy.stats import norm

import heapq

from copy import deepcopy

pwd = os.getcwd()
if pwd not in sys.path:
    sys.path.append(pwd)

from Scenario.Scenario import Scenario

from .GeneticAlgorithmConfig import GeneticAlgorithmConfig

class GeneticAlgorithm(QObject):

    def __init__(self, 
        scenario:Optional[Scenario] = None, 
        config:GeneticAlgorithmConfig = None
    ):
        super().__init__()
        self.scenario: Scenario = Scenario() if scenario is None else scenario
        self.config:GeneticAlgorithmConfig = GeneticAlgorithmConfig() if config is None else config

    def mutateIndividual(self, individual:Scenario) -> Scenario:
        new_individual = deepcopy(individual)
        new_value = \
            individual.years_[1].technical_.battery_storage.ess_system.installed_capacity_kwh \
            + (
                np.random.normal()
                * self.config.randomness
            )
        
        new_individual.set_allYears_technical_batteryStorage_essSystem_installedCapacity(new_value)
        new_individual.set_allYears_technical_batteryStorage_essSystem_chargingStrategy( np.random.choice([1,2], 1))

        return new_individual

    def getOptimised(self) -> Scenario:
        survivals: list[Scenario] = [
            self.scenario.years_[1].technical_.battery_storage.ess_system.installed_capacity_kwh, deepcopy(self.scenario)
            for i in range(self.config.keep)
        ]

        for i in range(self.config.number_of_generations):
            next_survivals:list[Scenario] = []
            for survival in survivals:
                for n in range(self.config.population_size//self.config.keep):
                    new_individual = self.mutateIndividual(survival)
                    
                    heapq.heappush(
                        next_survivals,
                        (new_individual.years_[1].technical_.battery_storage.ess_system.installed_capacity_kwh,new_individual)
                    )
                    if len(next_survivals) > self.config.keep:
                        heapq.heappop(next_survivals)
            
            for survival in survivals[:self.config.population_size%self.config.keep]:
                new_individual = self.mutateIndividual(survival)
                
                heapq.heappush(
                    next_survivals,
                    (new_individual.years_[1].technical_.battery_storage.ess_system.installed_capacity_kwh,new_individual)
                )
                if len(next_survivals) > self.config.keep:
                    heapq.heappop(next_survivals)

            survivals = next_survivals  
