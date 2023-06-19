import numpy as np

class Tools():

    # def check_constrains(self,used):
    #     mult = np.multiply(self.rest,used)
    #     sum = np.sum(mult,axis=1)
    #     diff = self.capacities - sum
    #     if any(diff < 0):
    #         return False
    #     else:
    #         return True

    # def evaluate(self,used):
    #     mult = np.multiply(self.weights,used)
    #     sum = np.sum(mult)
    #     return sum

    def evaluate(self,matrix):
        highest_finish = 0
        for m in matrix:
            finish = m[-1][-1]
            if finish > highest_finish:
                highest_finish = finish
        return highest_finish
    
    