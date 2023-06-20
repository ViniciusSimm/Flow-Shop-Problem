import random
from csv import writer
import time
import numpy as np
import cv2

from constructor import Constructor
from heuristic import Heuristic
from tools import Tools

from data import CAR1,CAR2,CAR3,CAR4,CAR5,CAR6
from data import HEL1,HEL2


class Model():
    def __init__(self,data):
        self.data = data
        self.tools = Tools()
        self.constructor = Constructor()
        self.heuristic = Heuristic()

    def GRASP(self):
        start_time = time.time()

        counting_visited_solutions = 0

        df = self.data.dataframe
        columns = df.columns
        num_machines = len(data.dataframe.columns)
        list_index = list(data.dataframe.index)
        neighbors = self.heuristic.permutation_1t(list_index)
        best_result = 1000000000000

        while neighbors:
            print('Num of Neighbors:',len(neighbors))
            neighbor = neighbors.pop(0)
            matrix = self.constructor.flow_shop_based_on_index_list(num_machines,df,neighbor)
            highest_finish = self.tools.evaluate(matrix)
            counting_visited_solutions = counting_visited_solutions + 1
            if highest_finish < best_result:
                img = self.tools.create_graph(matrix,self.data.limit_x_axis,columns)
                # cv2.imwrite('image.png', img)
                best_index = neighbor.copy()
                best_matrix = matrix.copy()
                print(neighbor)
                best_result = highest_finish
                neighbors = self.heuristic.permutation_1t(neighbor)
                random.shuffle(neighbors)
                print('RESTART -----------------------------------')
                print('BEST_RESULT:', best_result)
                print('CURRENT SOLUTION:', best_index)

        cv2.imwrite('image.png', img)
        print(best_index)
        print('Best result:',best_result)
        print('Visited Solutions:', counting_visited_solutions)
        final_time = time.time()

        print(best_matrix)
        print(best_result)
        print(best_index)

        with open('GRASP.csv', 'a') as f_object:
            writer_object = writer(f_object)
            List = [data.name_data,len(data.dataframe.columns),len(list(data.dataframe.index)),best_index,best_result]
            print(List)
            writer_object.writerow(List)
            f_object.close()


if __name__ == "__main__":

    for data in [CAR1()]:
        for i in range(1):
            data = data
            model = Model(data)
            model.GRASP()
