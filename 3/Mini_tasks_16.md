# Mini_tasks_16

+ [miniTasks](#miniTasks)

## miniTasks

 16 Tasks acomprehension, filter, map

```python

# 1. Найти все числа от 1 до 1000, которые делятся на 17(n)
import math


def divisible_1(n: int):
    result_list = [x for x in range(1, 1000) if x % n == 0]
    return result_list


# 2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2(n)
def number_consist_2(n: int):
    result_list = [x for x in range(1, 1000) if "2" in str(x)]
    return result_list


# 3. Найти все числа от 1 до 10000, которые являются палиндромом
def polindrom_3():
    result_list = [x for x in range(1, 10000) if str(x) == str(x)[::-1]]
    return result_list


# 4. Посчитать количество пробелов в строке
def spaces_count_4(string_to_count: str):
    return string_to_count.count(' ')


# 5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
def delete_vowels_5(string_to_delete: str):
    vowels = "eyuioa"
    return "".join(i for i in string_to_delete if i not in vowels)


# 6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
def find_words_6(string_to_find: str):
    return [x for x in string_to_find.split(" ") if not len(x) > 5]


# 7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.
def make_dictionary_7(string_to_make: str):
    return {x: len(x) for x in string_to_make.split(" ")}


# 8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.\
def get_unique(string_to_get: str):
    return {x.lower() for x in string_to_get if x.isalpha()}


# 9. На входе список чисел, получить список квадратов этих чисел / use map
def sqr_numbers(list_of_numbers):
    return list(map(lambda x: x ** 2, list_of_numbers))


# 10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2.
# На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
def coords_dist(coords):
    result_coords = [(x, y) for x, y in coords if y == 5 * x - 2]
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in result_coords]
    return dict(zip(result_coords, distances))


# 11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.
def task_11():
    return [x ** 2 for x in range(2, 27) if x % 2 == 0]


# 12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат
# (0, 0) в первой четверти
def most_distant_point_12(coords):
    return max([math.sqrt(x ** 2 + y ** 2) for x, y in coords if x > 0 and y > 0])


# 13. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат
# (0, 0) в первой четверти
def get_operations_list_13(first_list, second_list):
    return [(first + second, first - second) for first, second in zip(first_list, second_list)]


# 14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты
# этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать
# все четные квадраты.
def get_even_sqr_14(numbers_list):
    return [str(int(x) ** 2) for x in numbers_list if int(x) % 2 == 0]


# 15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит.
# Мы хотим получить нормальную таблицу, чтобы импортировать в csv
def get_converted_data_15(data: str):
    data = [x.split(',') for x in data.split()]
    result = [{} for i in range(len(data[0])-1)]
    for i in range(len(data)):
        for j in range(1, len(data[i])):
            result[j-1][data[i][0]] = data[i][j]

    return result


# 16. Получить сумму по столбцам у двумерного списка
def get_columns_sum(matrix):
    return [sum(x) for x in zip(*matrix)]

```
