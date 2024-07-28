class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        M=len(matrix[0])
        for i in range (N):
            for j in range (i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                print(matrix)
        print(matrix)
        for i in range(N):
            for j in range(int(N/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][N-j-1]
                matrix[i][N-j-1] = temp
        