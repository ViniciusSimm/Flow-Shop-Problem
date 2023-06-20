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

        self.limit_x_axis = 10000


class CAR2(Data):
    def __init__(self):
        self.name_data = "car2"

        self.description = """13 4"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 654 1 147 2 345 3 447
                    0 321 1 520 2 789 3 702
                    0  12 1 147 2 630 3 255
                    0 345 1 586 2 214 3 866
                    0 678 1 532 2 275 3 332
                    0 963 1 145 2 302 3 225
                    0  25 1  24 2 142 3 589
                    0 874 1 517 2  24 3 996
                    0 114 1 896 2 520 3 541
                    0 785 1 543 2 336 3 234
                    0 203 1 210 2 699 3 784
                    0 696 1 784 2 855 3 512
                    0 302 1 512 2 221 3 345"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3'])

        self.limit_x_axis = 10000

class CAR3(Data):
    def __init__(self):
        self.name_data = "car3"

        self.description = """12 5"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 456 1 537 2 123 3 214 4 234
                    0 789 1 854 2 225 3 528 4 123
                    0 876 1 632 2 588 3 896 4 456
                    0 543 1 145 2 669 3 325 4 789
                    0 210 1 785 2 966 3 147 4 876
                    0 123 1 214 2 332 3 856 4 543
                    0 456 1 752 2 144 3 321 4 210
                    0 789 1 143 2 755 3 427 4 123
                    0 876 1 698 2 322 3 546 4 456
                    0 543 1 532 2 100 3 321 4 789
                    0 210 1 145 2 114 3 401 4 876
                    0 124 1 247 2 753 3 214 4 543"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4'])

        self.limit_x_axis = 10000


class CAR4(Data):
    def __init__(self):
        self.name_data = "car4"

        self.description = """14 4"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 456 1 856 2 963 3 696
                    0 789 1 930 2  21 3 320
                    0 630 1 214 2 475 3 142
                    0 214 1 257 2 320 3 753
                    0 573 1 896 2 124 3 214
                    0 218 1 532 2 752 3 528
                    0 653 1 142 2 147 3 653
                    0 214 1 547 2 532 3 214
                    0 204 1 865 2 145 3 527
                    0 785 1 321 2 763 3 536
                    0 696 1 124 2 214 3 214
                    0 532 1  12 2 257 3 528
                    0  12 1 345 2 854 3 888
                    0 457 1 678 2 123 3 999"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3'])

        self.limit_x_axis = 12000


class CAR5(Data):
    def __init__(self):
        self.name_data = "car5"

        self.description = """10 6"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 333 1 991 2 996 3 123 4 145 5 234
                    0 333 1 111 2 663 3 456 4 785 5 532
                    0 252 1 222 2 222 3 789 4 214 5 586
                    0 222 1 204 2 114 3 876 4 752 5 532
                    0 255 1 477 2 123 3 543 4 143 5 142
                    0 555 1 566 2 456 3 210 4 698 5 573
                    0 558 1 899 2 789 3 124 4 532 5  12
                    0 888 1 965 2 876 3 537 4 145 5  14
                    0 889 1 588 2 543 3 854 4 247 5 527
                    0 999 1 889 2 210 3 632 4 451 5 856"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4','M5'])

        self.limit_x_axis = 10000


class CAR6(Data):
    def __init__(self):
        self.name_data = "car6"

        self.description = """8 9"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0 887 1 447 2 234 3 159 4 201 5 555 6 463 7 456 8 753
                    0 799 1 779 2 567 3 267 4 478 5 444 6 123 7 789 8  21
                    0 999 1 999 2 852 3 483 4 520 5 120 6 456 7 630 8 427
                    0 666 1 666 2 140 3 753 4 145 5 142 6 789 7 258 8 520
                    0 663 1  25 2 222 3 420 4 699 5 578 6 876 7 741 8 142
                    0 333 1 558 2 558 3 159 4 875 5 965 6 543 7  36 8 534
                    0 222 1 886 2 965 3  25 4 633 5 412 6 210 7 985 8 157
                    0 114 1 541 2 412 3 863 4 222 5  25 6 123 7 214 8 896"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4','M5','M6','M7','M8'])

        self.limit_x_axis = 12000


class HEL1(Data):
    def __init__(self):
        self.name_data = "hel1"

        self.description = """100  10"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0  1  1  1  2  1  3  4  4  3  5  5  6  5  7  7  8  6  9  4
                    0  2  1  5  2  4  3  3  4  1  5  9  6  5  7  4  8  7  9  0
                    0  5  1  6  2  8  3  4  4  4  5  2  6  5  7  6  8  7  9  5
                    0  4  1  1  2  5  3  6  4  5  5  7  6  9  7  2  8  6  9  2
                    0  4  1  4  2  2  3  7  4  3  5  6  6  5  7  2  8  4  9  1
                    0  7  1  6  2  2  3  5  4  4  5  1  6  4  7  7  8  5  9  5
                    0  8  1  5  2  8  3  7  4  9  5  5  6  3  7  5  8  1  9  5
                    0  4  1  2  2  5  3  8  4  9  5  9  6  4  7  7  8  5  9  8
                    0  2  1  7  2  4  3  2  4  5  5  4  6  5  7  8  8  4  9  3
                    0  6  1  5  2  1  3  9  4  4  5  4  6  7  7  6  8  5  9  1
                    0  5  1  4  2  7  3  3  4  9  5  1  6  4  7  7  8  3  9  2
                    0  2  1  4  2  9  3  2  4  4  5  5  6  2  7  1  8  4  9  2
                    0  4  1  0  2  1  3  2  4  2  5  3  6  1  7  4  8  2  9  8
                    0  1  1  2  2  5  3  7  4  8  5  6  6  2  7  1  8  4  9  8
                    0  6  1  4  2  5  3  1  4  2  5  4  6  5  7  6  8  2  9  9
                    0  4  1  5  2  3  3  1  4  8  5  7  6  0  7  1  8  4  9  6
                    0  7  1  3  2  1  3  4  4  7  5  0  6  4  7  1  8  5  9  6
                    0  5  1  2  2  4  3  1  4  2  5  7  6  5  7  3  8  2  9  3
                    0  8  1  6  2  8  3  5  4  7  5  4  6  2  7  5  8  9  9  5
                    0  4  1  5  2  3  3  5  4  7  5  9  6  2  7  4  8  5  9  8
                    0  3  1  5  2  7  3  9  4  6  5  2  6  4  7  4  8  7  9  3
                    0  0  1  2  2  4  3  5  4  4  5  7  6  4  7  5  8  4  9  8
                    0  4  1  2  2  5  3  7  4  4  5  5  6  3  7  2  8  8  9  5
                    0  7  1  8  2  2  3  1  4  9  5  6  6  7  7  8  8  4  9  1
                    0  4  1  8  2  5  3  2  4  6  5  8  6  9  7  5  8  8  9  5
                    0  4  1  5  2  7  3  2  4  3  5  7  6  3  7  6  8  5  9  4
                    0  4  1  2  2  1  3  5  4  1  5  3  6  5  7  6  8  5  9  5
                    0  5  1  8  2  5  3  7  4  8  5  2  6  5  7  8  8  3  9  5
                    0  5  1  4  2  5  3  4  4  5  5  7  6  6  7  2  8  5  9  9
                    0  8  1  2  2  1  3  5  4  5  5  6  6  5  7  8  8  7  9  5
                    0  8  1  3  2  5  3  9  4  5  5  4  6  5  7  2  8  4  9  2
                    0  8  1  5  2  2  3  5  4  7  5  6  6  2  7  8  8  9  9  5
                    0  3  1  7  2  4  3  6  4  8  5  2  6  4  7  5  8  2  9  3
                    0  5  1  5  2  4  3  7  4  9  5  8  6  2  7  5  8  2  9  5
                    0  5  1  2  2  5  3  2  4  5  5  4  6  8  7  2  8  1  9  3
                    0  5  1  5  2  9  3  5  4  4  5  9  6  8  7  5  8  3  9  5
                    0  2  1  1  2  2  3  1  4  4  5  3  6  3  7  5  8  2  9  6
                    0  8  1  8  2  4  3  7  4  2  5  6  6  8  7  6  8  3  9  5
                    0  9  1  7  2  5  3  8  4  5  5  6  6  5  7  8  8  9  9  4
                    0  5  1  6  2  9  3  6  4  5  5  3  6  1  7  8  8  7  9  4
                    0  6  1  4  2  7  3  4  4  3  5  6  6  1  7  4  8  5  9  8
                    0  4  1  3  2  7  3  5  4  1  5  9  6  2  7  4  8  2  9  5
                    0  4  1  2  2  8  3  7  4  3  5  4  6  9  7  8  8  7  9  4
                    0  2  1  5  2  9  3  4  4  2  5  5  6  3  7  0  8  4  9  7
                    0  9  1  5  2  4  3  2  4  3  5  7  6  0  7  2  8  1  9  6
                    0  2  1  3  2  2  3  5  4  1  5  0  6  8  7  9  8  5  9  3
                    0  5  1  2  2  7  3  9  4  4  5  3  6  6  7  2  8  5  9  0
                    0  7  1  8  2  2  3  1  4  4  5  7  6  5  7  8  8  9  9  4
                    0  1  1  4  2  2  3  3  4  6  5  8  6  2  7  4  8  7  9  5
                    0  2  1  5  2  4  3  5  4  6  5  8  6  4  7  1  8  7  9  5
                    0  8  1  3  2  0  3  2  4  5  5  6  6  8  7  2  8  9  9  4
                    0  7  1  2  2  4  3  3  4  6  5  2  6  9  7  4  8  1  9  8
                    0  3  1  5  2  7  3  5  4  3  5  8  6  6  7  4  8  8  9  1
                    0  5  1  0  2  5  3  6  4  0  5  0  6  2  7  4  8  7  9  8
                    0  1  1  9  2  5  3  2  4  4  5  7  6  5  7  0  8  2  9  5
                    0  0  1  2  2  9  3  6  4  1  5  4  6  0  7  0  8  5  9  2
                    0  0  1  2  2  5  3  8  4  3  5  6  6  9  7  1  8  2  9  4
                    0  7  1  9  2  6  3  3  4  5  5  1  6  7  7  5  8  4  9  5
                    0  4  1  3  2  5  3  2  4  1  5  4  6  9  7  7  8  4  9  1
                    0  0  1  3  2  5  3  2  4  4  5  9  6  4  7  7  8  5  9  4
                    0  7  1  8  2  5  3  6  4  3  5  9  6  8  7  7  8  4  9  6
                    0  1  1  9  2  6  3  7  4  0  5  2  6  4  7  8  8  3  9  6
                    0  6  1  1  2  2  3  0  4  3  5  5  6  4  7  1  8  7  9  3
                    0  6  1  5  2  1  3  4  4  9  5  7  6  3  7  5  8  6  9  4
                    0  1  1  8  2  2  3  6  4  9  5  4  6  7  7  5  8  8  9  4
                    0  0  1  1  2  6  3  2  4  9  5  4  6  8  7  5  8  7  9  6
                    0  4  1  2  2  5  3  6  4  8  5  5  6  6  7  4  8  1  9  4
                    0  3  1  4  2  5  3  8  4  4  5  1  6  2  7  3  8  6  9  8
                    0  9  1  8  2  2  3  3  4  1  5  4  6  0  7  2  8  4  9  5
                    0  4  1  3  2  2  3  5  4  6  5  4  6  1  7  8  8  9  9  2
                    0  5  1  7  2  1  3  2  4  6  5  8  6  2  7  3  8  4  9  7
                    0  2  1  1  2  4  3  3  4  8  5  4  6  6  7  2  8  4  9  5
                    0  6  1  7  2  9  3  2  4  4  5  3  6  2  7  5  8  6  9  7
                    0  2  1  4  2  0  3  2  4  5  5  3  6  4  7  7  8  8  9  6
                    0  2  1  7  2  5  3  4  4  3  5  1  6  5  7  6  8  0  9  2
                    0  3  1  5  2  7  3  0  4  2  5  4  6  5  7  2  8  5  9  7
                    0  2  1  4  2  5  3  3  4  4  5  7  6  8  7  3  8  2  9  4
                    0  9  1  9  2  1  3  4  4  5  5  7  6  6  7  5  8  3  9  2
                    0  8  1  2  2  5  3  2  4  2  5  5  6  1  7  5  8  7  9  8
                    0  4  1  5  2  2  3  4  4  7  5  9  6  5  7  4  8  2  9  4
                    0  5  1  5  2  1  3  2  4  4  5  2  6  3  7  8  8  5  9  1
                    0  0  1  2  2  9  3  5  4  4  5  2  6  5  7  9  8  6  9  5
                    0  1  1  2  2  3  3  5  4  6  5  2  6  4  7  0  8  2  9  5
                    0  4  1  2  2  3  3  5  4  4  5  2  6  3  7  5  8  4  9  2
                    0  4  1  4  2  5  3  8  4  9  5  8  6  5  7  2  8  8  9  3
                    0  4  1  2  2  3  3  3  4  2  5  5  6  8  7  8  8  1  9  2
                    0  5  1  3  2  6  3  2  4  5  5  6  6  4  7  7  8  9  9  3
                    0  4  1  2  2  3  3  6  4  8  5  5  6  3  7  4  8  7  9  2
                    0  5  1  8  2  8  3  3  4  5  5  6  6  5  7  6  8  5  9  2
                    0  5  1  6  2  4  3  2  4  5  5  4  6  6  7  5  8  8  9  4
                    0  2  1  1  2  4  3  7  4  4  5  5  6  9  7  8  8  5  9  6
                    0  2  1  1  2  4  3  6  4  5  5  8  6  6  7  1  8  3  9  5
                    0  9  1  5  2  1  3  3  4  5  5  7  6  9  7  1  8  2  9  5
                    0  3  1  5  2  4  3  9  4  7  5  2  6  6  7  5  8  2  9  1
                    0  2  1  5  2  0  3  3  4  2  5  4  6  7  7  8  8  9  9  5
                    0  5  1  3  2  5  3  7  4  9  5  2  6  4  7  5  8  5  9  8
                    0  6  1  3  2  1  3  5  4  0  5  1  6  4  7  8  8  9  9  8
                    0  3  1  0  2  4  3  3  4  7  5  2  6  6  7  9  8  4  9  1
                    0  1  1  7  2  4  3  2  4  2  5  4  6  5  7  0  8  6  9  9
                    0  1  1  7  2  8  3  4  4  6  5  5  6  4  7  8  8  5  9  2"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4','M5','M6','M7','M8','M9'])

        self.limit_x_axis = 150


class HEL2(Data):
    def __init__(self):
        self.name_data = "hel2"

        self.description = """20  10"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0  1  1  1  2  1  3  4  4  3  5  5  6  5  7  7  8  6  9  4
                    0  2  1  5  2  4  3  3  4  1  5  9  6  5  7  4  8  7  9  0
                    0  5  1  6  2  8  3  4  4  4  5  2  6  5  7  6  8  7  9  5
                    0  4  1  1  2  5  3  6  4  5  5  7  6  9  7  2  8  6  9  2
                    0  4  1  4  2  2  3  7  4  3  5  6  6  5  7  2  8  4  9  1
                    0  7  1  6  2  2  3  5  4  4  5  1  6  4  7  7  8  5  9  5
                    0  8  1  5  2  8  3  7  4  9  5  5  6  3  7  5  8  1  9  5
                    0  4  1  2  2  5  3  8  4  9  5  9  6  4  7  7  8  5  9  8
                    0  2  1  7  2  4  3  2  4  5  5  4  6  5  7  8  8  4  9  3
                    0  6  1  5  2  1  3  9  4  4  5  4  6  7  7  6  8  5  9  1
                    0  5  1  4  2  7  3  3  4  9  5  1  6  4  7  7  8  3  9  2
                    0  2  1  4  2  9  3  2  4  4  5  5  6  2  7  1  8  4  9  2
                    0  4  1  0  2  1  3  2  4  2  5  3  6  1  7  4  8  2  9  8
                    0  1  1  2  2  5  3  7  4  8  5  6  6  2  7  1  8  4  9  8
                    0  6  1  4  2  5  3  1  4  2  5  4  6  5  7  6  8  2  9  9
                    0  4  1  5  2  3  3  1  4  8  5  7  6  0  7  1  8  4  9  6
                    0  7  1  3  2  1  3  4  4  7  5  0  6  4  7  1  8  5  9  6
                    0  5  1  2  2  4  3  1  4  2  5  7  6  5  7  3  8  2  9  3
                    0  8  1  6  2  8  3  5  4  7  5  4  6  2  7  5  8  9  9  5
                    0  4  1  5  2  3  3  5  4  7  5  9  6  2  7  4  8  5  9  8"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4','M5','M6','M7','M8','M9'])

        self.limit_x_axis = 300


class REC17(Data):
    def __init__(self):
        self.name_data = "REC17"

        self.description = """20 15"""
        
        self.description = np.array(self.convert_text_to_list(self.description)).astype(int)

        self.jobs = """0  59  1  11  2   4  3  79  4  94  5  31  6  74  7  82  8  53  9  51 10  19 11  31 12  46 13  47 14  10
                    0  72  1  54  2  36  3   3  4  59  5  23  6  40  7  59  8  89  9  37 10  85 11  67 12  39 13  65 14  60
                    0  92  1  26  2  15  3  81  4  86  5  56  6  92  7  47  8  93  9  21 10  40 11  77 12  84 13  10 14  91
                    0  49  1  27  2  99  3  64  4  30  5  51  6  26  7  89  8  40  9  64 10  60 11  67 12  67 13 100 14   3
                    0  42  1  12  2  55  3  62  4  37  5  24  6  24  7  42  8  41  9  88 10  14 11  33 12  85 13   4 14  20
                    0  21  1  61  2  52  3  49  4  44  5  98  6  26  7  68  8  61  9  25 10   6 11  46 12  75 13  37 14   5
                    0  80  1  99  2  88  3  83  4  11  5  93  6  47  7  80  8 100  9  87 10  84 11  17 12  43 13  93 14  58
                    0   4  1  54  2  43  3  63  4  44  5  78  6  44  7  39  8  76  9  99 10  29 11  38 12  14 13  75 14  25
                    0  46  1  23  2  54  3  77  4  60  5  53  6  42  7  72  8  90  9  11 10  22 11  68 12  94 13  24 14  14
                    0  23  1  84  2  92  3  94  4   8  5  10  6  77  7  58  8  64  9  95 10  55 11  15 12  19 13  62 14  67
                    0  53  1  91  2  80  3   8  4  41  5  89  6   3  7  87  8  57  9  75 10  37 11   8 12  23 13  88 14  65
                    0  72  1  17  2  53  3  36  4   9  5  24  6  80  7   9  8  28  9  60 10  94 11  99 12  67 13  10 14  44
                    0   5  1  44  2  96  3  37  4  21  5  44  6  49  7  13  8  86  9  74 10  89 11   3 12  82 13  85 14  61
                    0  80  1  19  2  73  3  95  4  78  5  78  6  31  7  13  8  50  9  93 10  98 11  80 12  46 13   9 14  37
                    0   7  1  16  2  46  3  82  4  97  5  82  6  41  7  21  8  11  9  50 10   5 11  28 12  95 13  84 14  45
                    0  68  1  73  2  57  3   4  4  66  5  71  6  87  7  43  8  60  9  56 10  30 11  21 12  14 13  37 14  61
                    0  77  1   2  2   1  3  82  4   2  5  49  6  89  7  27  8  34  9  52 10  85 11  26 12  80 13  87 14  58
                    0  17  1  86  2  32  3  35  4   6  5  50  6  53  7  39  8  94  9  89 10  22 11  75 12  59 13  74 14  27
                    0  61  1  14  2  70  3  58  4  24  5  36  6  70  7  57  8  31  9 100 10  21 11  76 12  54 13  94 14  57
                    0  29  1   6  2   6  3  12  4  78  5  28  6  40  7  13  8  61  9  19 10  39 11  98 12  69 13  14 14   3"""

        self.jobs = np.array(self.convert_text_to_list_of_lists(self.jobs,self.description[1]*2)).astype(int)

        self.dataframe = pd.DataFrame([i[1::2] for i in self.jobs],columns=['M0','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14'])

        self.limit_x_axis = 3000


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
    print(data.dataframe)
    print('Num Col:', len(data.dataframe.columns))
    print('List Index:', list(data.dataframe.index))