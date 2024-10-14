#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    '''
    Pascal triangle
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1]
        for j in range(1, len(triangle[-1])):
            temp.append(triangle[-1][j-1] + triangle[-1][j])
        temp.append(1)
        triangle.append(temp)

    return triangle
