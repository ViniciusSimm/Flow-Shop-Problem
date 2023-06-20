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

    def permutation_all(self,list_index):
        permutations = itertools.permutations(list_index)
        return list(permutations)

if __name__ == "__main__":
    heuristic = Heuristic()
    vector = [0,1,2,3,4,5,6,7,8,9]
    permutations = heuristic.permutation_all(vector)
    permutations_1t = heuristic.permutation_1t(vector)
    # print(len(permutations_1t))
    print(len(permutations))
