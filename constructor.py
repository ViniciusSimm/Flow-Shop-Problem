import random
import numpy as np
from tools import Tools
from data import CAR1

class Constructor():

    def build_blank_matrix(self,num_machines):
        matrix = []
        for i in range(num_machines):
            matrix.append([])
        return matrix

    def flow_shop_based_on_index_list(self,num_machines,dataframe,list_index):
        matrix = self.build_blank_matrix(num_machines)

        for i in list_index:

            for column in range(num_machines):

                try:
                    same_machine = matrix[column][-1][2]
                except:
                    same_machine = 0

                if column != 0:
                    same_item = matrix[column-1][-1][2]
                else:
                    same_item = 0
                
                if same_item > same_machine:
                    beginning = same_item
                else:
                    beginning = same_machine

                time = dataframe.loc[i]['M{}'.format(column)]

                matrix[column].append((i,beginning,beginning+time))

        return matrix

    def flow_shop_initial_solution(self,num_machines,dataframe):
        matrix = self.build_blank_matrix(num_machines)
        list_index = [i for i in dataframe.index]
        random.shuffle(list_index)

        for i in list_index:

            for column in range(num_machines):

                try:
                    same_machine = matrix[column][-1][2]
                except:
                    same_machine = 0

                if column != 0:
                    same_item = matrix[column-1][-1][2]
                else:
                    same_item = 0
                
                if same_item > same_machine:
                    beginning = same_item
                else:
                    beginning = same_machine

                time = dataframe.loc[i]['M{}'.format(column)]

                matrix[column].append((i,beginning,beginning+time))

        return matrix,list_index


if __name__ == "__main__":

    constructor = Constructor()
    tool = Tools()
    data = CAR1()
    matrix = constructor.flow_shop_initial_solution(5,data.dataframe)
    for m in matrix:
        print(m)
    
    print(tool.evaluate(matrix))

