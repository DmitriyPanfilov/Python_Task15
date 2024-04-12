# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров


import logging

logging.basicConfig(filename='Log.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()": {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def transpose(matrix):

    trans_matrix = matrix
    temp = True
    line_length = (len(matrix[0]))
    for i in trans_matrix:
        if line_length != (len(i)):
            temp = False

    if temp == True:
        trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        logger.info(f'Транспорирование исходной матрицы {matrix} в матрицу {trans_matrix}')
        return trans_matrix
    else:
        logger.error(f'Невозможно провести транспорирование матрицы {IndexError} Количество индексов матрицы не совпадает')
        return IndexError("Работа завершина по причине не соовтветствия количества элементов матрицы")



if __name__ == '__main__':

    print(transpose(matrix = [[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9],
                              [3, 2, 1]]))


