class Solution:

    @staticmethod
    def solve(matrix):
        tamanho = len(matrix)
        rows = set()
        cols = set()
        diags = set()
        rev_diags = set()

        for linha in range(tamanho):
            for coluna in range(tamanho):
                if matrix[linha][coluna] == '1':
                    rows.add(linha)
                    cols.add(coluna)
                    diags.add(linha - coluna)
                    rev_diags.add(linha + coluna)

        return len(rows) == len(cols) == tamanho and len(diags) == len(rev_diags)

"""
ob = Solution()
N = 8
mat = [['0' for x in range(N)] for y in range(N)]
lista = []
lista1 = []
LINHA = 0
entrada = input()

while entrada != 'stop':
    for i in entrada:
        lista1.append(i)
    lista.append(lista1)
    for jj in lista:
        for w in jj:
            if w == '1':
                indice = lista[0].index(w)
                mat[LINHA][indice] = '1'
                LINHA += 1
    lista = []
    lista1 = []
    entrada = input()
for ii in mat:
    print(ii)

if ob.solve(mat):
    print('1')
else:
    print('0')
"""