import itertools
import numpy as np
from tools import Tools
import random

class Heuristic():
    def permutation(self,list_index):
        permutations = list(itertools.permutations(list_index))
        return permutations
    