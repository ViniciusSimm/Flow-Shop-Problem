import random
from csv import writer
import time
import numpy as np

from constructor import Constructor
from tools import Tools


class Model():
    def __init__(self,data):
        self.data = data
        self.tools = Tools()
        self.constructor = Constructor()
        # self.heuristic = Heuristic()

    def GRASP(self):
        start_time = time.time()

        df = self.data.dataframe
        num_machines = len(data.dataframe.columns)
        list_index = list(data.dataframe.index)

        
        matrix = self.constructor.flow_shop_based_on_index_list(self,num_machines,df,list_index)
        highest_finish = self.tools.evaluate(matrix)


        final_time = time.time()

        with open('GRASP.csv', 'a') as f_object:
            writer_object = writer(f_object)
            List = []
            print(List)
            writer_object.writerow(List)
            f_object.close()    

    # def genetic(self,n_solutions,alpha,parts,n_genetic_output,chance_of_mutation):
    #     start_time = time.time()

    #     genetic_solutions = []
    #     print(self.data.name_data)
    #     solution_list = self.constructor.random_constructor(n_solutions=n_solutions,alpha=alpha)

    #     end_indicator = True
    #     while end_indicator:
    #         # print(solution_list)
    #         solution_list_results = [(i,self.tools.evaluate(i)) for i in solution_list]
    #         best_current_solution = self.constructor.tuple_ordering(solution_list_results)[-1]
    #         # print(best_current_solution)
    #         genetic_solutions = self.heuristic.create_neighbors_genetic(n_solutions=n_solutions,solution_list=solution_list,parts=parts,tool=self.tools)
    #         genetic_solutions = [self.heuristic.prob_mutation(vec=i,tool=self.tools,chance_of_mutation=chance_of_mutation) for i in genetic_solutions]
    #         genetic_solutions_results = [(i,self.tools.evaluate(i)) for i in genetic_solutions]
    #         genetic_solutions_results = self.constructor.tuple_ordering(genetic_solutions_results)
    #         # print(genetic_solutions_results)
            
    #         if genetic_solutions_results[-1][1] <= best_current_solution[1]:
    #             end_indicator = False
    #             best_vector = best_current_solution[0]
    #             best_score = best_current_solution[1]
    #         else:
    #             results = genetic_solutions_results[-1*n_genetic_output:]
    #             results = [np.array(i[0]) for i in results]
    #             rand = random.choices(solution_list,k=n_solutions-n_genetic_output)
    #             for cel in rand:
    #                 results.append(cel)
    #             solution_list = results.copy()

    #     final_time = time.time()

    #     with open('genetic.csv', 'a') as f_object:
    #         writer_object = writer(f_object)
    #         List = [self.data.name_data,n_solutions,alpha,best_vector,best_score,(self.data.optimum-best_score)/self.data.optimum,final_time-start_time,parts,n_genetic_output,chance_of_mutation]
    #         writer_object.writerow(List)
    #         f_object.close()

if __name__ == "__main__":

    for data in ...:
        for i in range(3):
            data = data
            N_SOLUTIONS = 1 # number of vectors
            ALPHA = 0.8 # proportion of 0s

            model = Model(data)
            model.GRASP(n_solutions=N_SOLUTIONS,alpha=ALPHA)


    # model = Model(WEING1())
    # model.genetic(n_solutions=10,alpha=0.6,parts=2,n_genetic_output=5,chance_of_mutation=0.5)

    # for data in hp:
    #     for i in range(5):
    #         data = data
    #         N_SOLUTIONS = 30 # number of vectors
    #         ALPHA = 0.8 # proportion of 0s
    #         PARTS = 2 # split gene
    #         N_GENETIC_OUTPUT = 15 # many vectors kept from genetic approach
    #         CHANCE_OF_MUTATION = 0.8 # probability of mutating a vector

    #         model = Model(data)
    #         model.genetic(n_solutions=N_SOLUTIONS,alpha=ALPHA,parts=PARTS,n_genetic_output=N_GENETIC_OUTPUT,chance_of_mutation=CHANCE_OF_MUTATION)

