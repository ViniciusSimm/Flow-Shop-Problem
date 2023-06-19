import itertools
import numpy as np
from tools import Tools
import random

class Heuristic():
    def permutation_1t(self,list_index):
        swaps = []
        for i in range(len(list_index)):
            for j in range(i+1, len(list_index)):
                new_vector = list_index.copy()
                new_vector[i], new_vector[j] = new_vector[j], new_vector[i]
                swaps.append(new_vector)
        return swaps

if __name__ == "__main__":
    heuristic = Heuristic()
    print(heuristic.permutation_1t([1,2,3,4]))