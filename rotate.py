def rotate_matrix(m):
    N = len(m)
    for x in range(N / 2):
        for y in range(x, N - x - 1):
            temp = m[x][y]
            m[x][y] = m[N - y - 1][x]
            m[N - y - 1][x] = m[N - x - 1][N - y - 1]
            m[N - x - 1][N - y - 1] = m[x][N - y - 1]
            m[N - y - 1][x] = temp


def print_matrix(m):
    N = len(m)
    for i in range(N):
        for j in range(N):
            print m[i][j],

        print "\n"
    print "\n"

test_m = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          ]

print_matrix(test_m)
rotate_matrix(test_m)
print_matrix(test_m)
