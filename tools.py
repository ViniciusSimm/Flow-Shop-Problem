import numpy as np

class Tools():
    def __init__(self,description,jobs):
        self.description = description
        self.jobs = jobs

    def check_constrains(self,used):
        mult = np.multiply(self.rest,used)
        sum = np.sum(mult,axis=1)
        diff = self.capacities - sum
        if any(diff < 0):
            return False
        else:
            return True

    def evaluate(self,used):
        mult = np.multiply(self.weights,used)
        sum = np.sum(mult)
        return sum
