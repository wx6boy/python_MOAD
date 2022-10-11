#Matrices

+ [ diagonalSum](# diagonalSum)

## diagonalSum

 An algorithm counting diagonal sum of matrix.

```python
def diagonalSum(mat):

    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j:
                sum += mat[i][j]

    return sum
```
