#2D Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])

#Print the array as it is 

for a in range(rows):                              # 1  2  3
    for b in range(cols):                          # 4  5  6
        print(matrix[a][b], end="  ")              # 7  8  9
    print()    

print()
print()

#1. Print Upper triangle of the matrix
# jth index is always equal or greater than ith index in case of upper triangle
# j >= i

for c in range(rows):
    for d in range(cols):
        if(c >= d):
            print(matrix[c][d], end="  ")
        else:
            print("*", end="  ")
    print()

print()
print()

#2. Print the lower trianle of the matrix 
# ith index will be greater than or equal to jth index
# i >= j

for e in range(rows):
    for f in range(cols):
        if (e >= f):
            print(matrix[e][f], end="  ")
        else:
            print("*", end="  ")
    print()

print()
print()
#3. Print Diagonal of the matrix
# ith index == j index

for i in range(rows):
    for j in range(cols):
        if(i == j):
            print(matrix[i][j], end="  ")
        else:
            print("*", end = "  ")
    print()
