from random import randint

print('2-мерный массив. A[n][m]. Количество элементов n * m')
n = int(input())
class PrintMatrix():
    def __init__(self, n, massiv):
        self.n = n
        self.massiv = massiv
        self.massiv = [[0 for i in range(self.n)] for j in range(self.n)]  # задали матрицу из 0-вых элементов

    def add_matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                self.massiv[i][j] = randint(1,9)#заполнение матрицы случ. числами

    def printfirstmatrix(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.massiv[i][j], end=' ')
            print()#вывод матрицы
        print()#табуляция

    def zamena(self):
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.massiv[i][j] = 20#на главной диагонали меняем элемент
            print()
        print()

    def printsecondmassiv(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.massiv[i][j], end=' ')
            print()#опять выводим новый массив

    def zamenax2(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.massiv[i][j] % 7 == 0:
                    self.massiv[i][j] = 100  # замена 7-ок на 100
            print()
        print()

    def summa(self):
        s = 0
        for i in range(self.n):
            for j in range(self.n):
                s += self.massiv[i][j]
        print(s)  # сложение всех элементов матрицы
    def get_matrix(self):
        self.get_matrix()
        return self





