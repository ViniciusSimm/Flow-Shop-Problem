import numpy as np
import matplotlib.pyplot as plt
import cv2
from data import Data

class Tools():
    def __init__(self):
        self.colors = [
            (255, 0, 0),    # Vermelho
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 255, 0),  # Amarelo
            (255, 0, 255),  # Magenta
            (0, 255, 255),  # Ciano
            (255, 165, 0),  # Laranja
            (128, 0, 128),  # Roxo
            (0, 128, 0),    # Verde escuro
            (0, 0, 128),    # Azul escuro
            (255, 192, 203),  # Rosa
            (165, 42, 42),    # Marrom
            (255, 215, 0),    # Ouro
            (128, 128, 128),  # Cinza
            (0, 128, 128),    # Verde-azulado
            (128, 0, 0),      # Marrom escuro
            (128, 0, 128),    # Roxo escuro
            (128, 128, 0),    # Oliva
            (192, 192, 192),  # Prata
            (255, 255, 255)   # Branco
        ]

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
    
    def blank_image(self,matrix):
        size_x = self.evaluate(matrix)
        size_y = len(matrix)
        figure_size = (size_y * 50 + 100, size_x + 100, 3)
        img = np.zeros(figure_size, dtype = np.uint8)
        img = np.ones(figure_size, dtype = np.uint8)
        img = 255*img
        return img

    def create_graph(self,matrix):
        # size_x = self.evaluate(matrix)
        # size_y = len(matrix)
        # (Y,X,COLORS)

        img = self.blank_image(matrix)

        for machine in range(len(matrix)):
            for item in range(len(matrix[machine])):
                ind,start,finish = matrix[machine][item]
                cv2.rectangle(img, (start+50, 50*machine + 50), (finish+50, 50*(machine+1) + 50), self.colors[ind], -1)

        # cv2.rectangle(img, (250, 100), (250 + 200, 100 + 50), self.colors[0], 2)

        img = cv2.resize(img, (1280,720), interpolation = cv2.INTER_AREA)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return img


# if __name__ == "__main__":
#     tools = Tools()
#     tools.create_graph([[]])
#     data = Data.CAR1()
#     constructor = Constructor()

#     matrix = constructor.flow_shop_based_on_index_list(5,data.dataframe,[0,1,2,3,4,5,6,7,8,9,10])
#     tools.create_graph(data.matrix)