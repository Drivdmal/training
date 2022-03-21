# диагонали квадратных матриц

matrix_5x5 = [
        [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25] ] 

n = len(matrix_5x5)
diagonal_main = []
diagonal_not_main = []

for i in range(5):
    for j in range(5):
        if i == j:
            diagonal_main.append(matrix_5x5[i][i])
        if (n == i + j + 1) or (j == n - i - 1):
            diagonal_not_main.append(matrix_5x5[i][j])

print(diagonal_main, diagonal_not_main)
# --------------------------------------------------------------------------

# make matrix n_x_m

n = 4 		# index
m = 6		# column

lst = []
matrix = []

for i in range(n):
    for j in range(m):
       lst.append()
    matrix.append(lst[:])
    lst.clear()
