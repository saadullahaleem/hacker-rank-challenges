import sys
from collections import deque

# Solved through the following approach:
# # Get number of loops
# # Reduce number of rotations by taking round_trip % number_of_rotations
# # Rotate each loop by number_of_rotations

# Passes all test cases. 


def matrixRotation(matrix):
    # Complete this function
    rt = n*2+((m-2)*2)
    nl = int(min(m/2, n/2)) if (m/2 > 2 and n/2 > 2) or min(m/2, n/2) == 1 else 2
    nr = r % rt
    sh = rt-nr if nr > rt/2 else -nr
    
    if not nr:
        return matrix
    
    l = []
    i = m
    j = n
    ii, jj = m, n
    
    for _ in range(nl):
        rt = jj*2+((ii-2)*2)
        nl = int(min(ii/2, jj/2)) if (ii/2 > 2 and jj/2 > 2) or min(ii/2, jj/2) == 1 else 2
        nr = r % rt
        sh = rt-nr if nr >= rt/2 else -nr
        x1, y1 = i-1, j-1
        x0, y0 = m-i, n-j
        ld = deque([])
        
        for idx in range(x0, x1):
            ld.append(matrix[idx][y0])
            
        for idx in range(y0, y1):
            ld.append(matrix[x1][idx])
        
        for idx in range(x1, x0, -1):
            ld.append(matrix[idx][y1])
        
        for idx in range(y1, y0, -1):
            ld.append(matrix[x0][idx])
        
        ld.rotate(-sh)
        
        
        for idx in range(x0, x1):
            matrix[idx][y0] = ld.popleft()
            
        for idx in range(y0, y1):
            matrix[x1][idx] = ld.popleft()
        
        for idx in range(x1, x0, -1):
            matrix[idx][y1] = ld.popleft()
        
        for idx in range(y1, y0, -1):
            matrix[x0][idx] = ld.popleft()
            
        i, j = i-1, j-1
        ii, jj = ii-2, jj-2
        
            
    for row in matrix:
        print(" ".join([str(c) for c in row]))

if __name__ == "__main__":
    m, n, r = input().strip().split(' ')
    m, n, r = [int(m), int(n), int(r)]
    matrix = []
    for matrix_i in range(m):
       matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
       matrix.append(matrix_t)
    matrixRotation(matrix)
