import numpy as np
import pandas as pd

class Data():
    def convert_text_to_list_of_lists(self,text,size_each_list):
        # print(len(text.split()))
        n = size_each_list
        megalist = []
        littlelist = []
        for i in text.split():
                littlelist.append(i)
                if len(littlelist) == n:
                        megalist.append(littlelist)
                        littlelist = []
        return megalist
    
    def convert_text_to_list(self,text):
        return text.split()

# class TEMPLATE(Data):
#     def __init__(self):
#         self.name_data = ""

#         self.weights = """"""
        
#         self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

#         self.capacities = """"""
        
#         self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

#         self.rest = """"""

#         self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

#         self.optimum = 0

class CAR1(Data):
    def __init__(self):
        self.name_data = "car1"

        self.description = """11 5"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 375 1  12 2 142 3 245 4 412
                    0 632 1 452 2 758 3 278 4 398
                    0  12 1 876 2 124 3 534 4 765
                    0 460 1 542 2 523 3 120 4 499
                    0 528 1 101 2 789 3 124 4 999
                    0 796 1 245 2 632 3 375 4 123
                    0 532 1 230 2 543 3 896 4 452
                    0  14 1 124 2 214 3 543 4 785
                    0 257 1 527 2 753 3 210 4 463
                    0 896 1 896 2 214 3 258 4 259
                    0 532 1 302 2 501 3 765 4 988"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4'])



class ABZ5(Data):
    def __init__(self):
        self.name_data = "abz5"

        self.description = """10 10"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """4 88 8 68 6 94 5 99 1 67 2 89 9 77 7 99 0 86 3 92
                    5 72 3 50 6 69 4 75 2 94 8 66 0 92 1 82 7 94 9 63
                    9 83 8 61 0 83 1 65 6 64 5 85 7 78 4 85 2 55 3 77
                    7 94 2 68 1 61 4 99 3 54 6 75 5 66 0 76 9 63 8 67
                    3 69 4 88 9 82 8 95 0 99 2 67 6 95 5 68 7 67 1 86
                    1 99 4 81 5 64 6 66 8 80 2 80 7 69 9 62 3 79 0 88
                    7 50 1 86 4 97 3 96 0 95 8 97 2 66 5 99 6 52 9 71
                    4 98 6 73 3 82 2 51 1 71 5 94 7 85 0 62 8 95 9 79
                    0 94 6 71 3 81 7 85 1 66 2 90 4 76 5 58 8 93 9 97
                    3 50 0 59 1 82 8 67 7 56 9 96 6 58 4 81 5 59 2 96"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

class ABZ6(Data):
    def __init__(self):
        self.name_data = "abz6"

        self.description = """10 10"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """7 62 8 24 5 25 3 84 4 47 6 38 2 82 0 93 9 24 1 66
                    5 47 2 97 8 92 9 22 1 93 4 29 7 56 3 80 0 78 6 67
                    1 45 7 46 6 22 2 26 9 38 0 69 4 40 3 33 8 75 5 96
                    4 85 8 76 5 68 9 88 3 36 6 75 2 56 1 35 0 77 7 85
                    8 60 9 20 7 25 3 63 4 81 0 52 1 30 5 98 6 54 2 86
                    3 87 9 73 5 51 2 95 4 65 1 86 6 22 8 58 0 80 7 65
                    5 81 2 53 7 57 6 71 9 81 0 43 4 26 8 54 3 58 1 69
                    4 20 6 86 5 21 8 79 9 62 2 34 0 27 1 81 7 30 3 46
                    9 68 6 66 5 98 8 86 7 66 0 56 3 82 1 95 4 47 2 78
                    0 30 3 50 7 34 2 58 1 77 5 34 8 84 4 40 9 46 6 44"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

class ABZ7(Data):
    def __init__(self):
        self.name_data = "abz7"

        self.description = """20 15"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """2 24  3 12  9 17  4 27  0 21  6 25  8 27  7 26  1 30  5 31 11 18 14 16 13 39 10 19 12 26
                    6 30  3 15 12 20 11 19  1 24 13 15 10 28  2 36  5 26  7 15  0 11  8 23 14 20  9 26  4 28
                    6 35  0 22 13 23  7 32  2 20  3 12 12 19 10 23  9 17  1 14  5 16 11 29  8 16  4 22 14 22
                    9 20  6 29  1 19  7 14 12 33  4 30  0 32  5 21 11 29 10 24 14 25  2 29  3 13  8 20 13 18
                    11 23 13 20  1 28  6 32  7 16  5 18  8 24  9 23  3 24 10 34  2 24  0 24 14 28 12 15  4 18
                    8 24 11 19 14 21  1 33  7 34  6 35  5 40 10 36  3 23  2 26  4 15  9 28 13 38 12 13  0 25
                    13 27  3 30  6 21  8 19 12 12  4 27  2 39  9 13 14 12  5 36 10 21 11 17  1 29  0 17  7 33
                    5 27  4 19  6 29  9 20  3 21 10 40  8 14 14 39 13 39  2 27  1 36 12 12 11 37  7 22  0 13
                    13 32 11 29  8 24  3 27  5 40  4 21  9 26  0 27 14 27  6 16  2 21 10 13  7 28 12 28  1 32
                    12 35  1 11  5 39 14 18  7 23  0 34  3 24 13 11  8 30 11 31  4 15 10 15  2 28  9 26  6 33
                    10 28  5 37 12 29  1 31  7 25  8 13 14 14  4 20  3 27  9 25 13 31 11 14  6 25  2 39  0 36
                    0 22 11 25  5 28 13 35  4 31  8 21  9 20 14 19  2 29  7 32 10 18  1 18  3 11 12 17  6 15
                    12 39  5 32  2 36  8 14  3 28 13 37  0 38  6 20  7 19 11 12 14 22  1 36  4 15  9 32 10 16
                    8 28  1 29 14 40 12 23  4 34  5 33  6 27 10 17  0 20  7 28 11 21  2 21 13 20  9 33  3 27
                    9 21 14 34  3 30 12 38  0 11 11 16  2 14  5 14  1 34  8 33  4 23 13 40 10 12  6 23  7 27
                    9 13 14 40  7 36  4 17  0 13  5 33  8 25 13 24 10 23  3 36  2 29  1 18 11 13  6 33 12 13
                    3 25  5 15  2 28 12 40  7 39  1 31  8 35  6 31 11 36  4 12 10 33 14 19  9 16 13 27  0 21
                    12 22 10 14  0 12  2 20  5 12  1 18 11 17  8 39 14 31  3 31  7 32  9 20 13 29  4 13  6 26
                    5 18 10 30  7 38 14 22 13 15 11 20  9 16  3 17  1 12  2 13 12 40  6 17  8 30  4 38  0 13
                    9 31  8 39 12 27  1 14  5 33  3 31 11 22 13 36  0 16  7 11 14 14  4 29  6 28  2 22 10 17"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

class ABZ8(Data):
    def __init__(self):
        self.name_data = "abz8"

        self.description = """20 15"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 19  9 33  2 32 13 18 10 39  8 34  6 25  4 36 11 40 12 33  1 31 14 30  3 34  5 26  7 13
                    9 11 10 22 14 19  5 12  4 25  6 38  0 29  7 39 13 19 11 22  1 23  3 20  2 40 12 19  8 26
                    3 25  8 17 11 24 13 40 10 32 14 16  5 39  9 19  0 24  1 39  4 17  2 35  7 38  6 20 12 31
                    14 22  3 36  2 34 12 17  4 30 13 12  1 13  6 25  9 12  7 18 10 31  0 39  5 40  8 26 11 37
                    12 32 14 15  1 35  7 13  8 32 11 23  6 22  4 21  0 38  2 38  3 40 10 31  5 11 13 37  9 16
                    10 23 12 38  8 11 14 27  9 11  6 25  5 14  4 12  2 27 11 26  7 29  3 28 13 21  0 20  1 30
                    6 39  8 38  0 15 12 27 10 22  9 27  2 32  4 40  3 12 13 20 14 21 11 22  5 17  7 38  1 27
                    11 11 13 24 10 38  8 15  9 19 14 13  5 30  0 26  2 29  6 33 12 21  1 15  3 21  4 28  7 33
                    8 20  6 17  5 26  3 34  9 23  0 16  2 18  4 35 12 24 10 16 11 26  7 12 14 13 13 27  1 19
                    1 18  7 37 14 27  9 40  5 40  6 17  8 22  3 17 10 30  0 38  4 21 12 32 11 24 13 24  2 30
                    11 19  0 22 13 36  6 18  5 22  3 17 14 35 10 34  7 23  8 19  2 29  1 22 12 17  4 33  9 39
                    6 32  3 22 12 24  5 13  4 13  1 11  0 11 13 25  8 13  2 15 10 33 11 17 14 16  9 38  7 24
                    14 16 13 16  1 37  8 25  2 26  3 11  9 34  4 14  0 20  6 36 12 12  5 29 10 25  7 32 11 12
                    8 20 10 24 11 27  9 38  5 34 12 39  7 33  4 37  2 31 13 15 14 34  3 33  6 26  1 36  0 14
                    8 31  0 17  9 13  1 21 10 17  7 19 13 14  3 40  5 32 11 25  2 34 14 23  6 13 12 40  4 26
                    8 38 12 17  3 14 13 17  4 12  1 35  6 35  0 19 10 36  7 19  9 29  2 31  5 26 11 35 14 37
                    14 20  3 16  0 33 10 14  5 27  7 31  8 16  6 31 12 28  9 37  4 37  2 29 11 38  1 30 13 36
                    11 18  3 37 14 16  6 15  8 14 12 11 13 32  5 12  1 11 10 29  7 19  4 12  9 18  2 26  0 39
                    11 11  2 11 12 22  9 35 14 20  7 31  4 19  3 39  5 28  6 33 10 34  1 38  0 20 13 17  8 28
                    2 12 12 25  5 23  8 21  6 27  9 30 14 23 11 39  3 26 13 34  7 17  1 24  4 12  0 19 10 36"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)



if __name__ == "__main__":

    data = CAR1()
    for i in data.dataframe.columns:
        print(i)
    