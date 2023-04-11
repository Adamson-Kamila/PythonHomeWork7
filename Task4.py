# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков)  для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22           3 5 32              3 5 8 3
# 37 43           2 4 6
# 51 86           -1 64 -8            8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

from random import randint


class Matrix:

    def __init__(self, arr):
        self.matrix = arr

    def len_rows(self):
        return len(self.matrix)

    def len_columns(self):
        return len(self.matrix[0])

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        return '\n'.join(' '.join(str(element) for element in row_elements) for row_elements in self.matrix)

    def __add__(self, other):
        rows_length = self.len_rows()
        columns_length = self.len_columns()
        if not isinstance(other, Matrix):
            raise TypeError('Допускается складывать матрицу только с другой матрицей!')
        elif rows_length != other.len_rows() or columns_length != other.len_columns():
            raise ValueError('Складывать допускается только матрицы одинаковой размерности!')
        else:
            result_matrix = [[self[r][c] + other[r][c] for c in range(columns_length)] for r in range(rows_length)]
            return Matrix(result_matrix)


arr = [[randint(1, 5) for _ in range(3)] for _ in range(3)]


arr = Matrix(arr)
print(arr)
