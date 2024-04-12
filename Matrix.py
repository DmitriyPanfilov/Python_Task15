# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров




def transpose(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(f'Исходная матрица: \n {matrix}\n результат: \n {trans_matrix}')




if __name__ == '__main__':

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


    transposed_matrix = transpose(matrix)