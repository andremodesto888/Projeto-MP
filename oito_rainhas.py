class Solution:

    @staticmethod
    def solve(matrix):
        """
        Função que verifica se é solução
        """
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

        if len(rows) == len(cols) == tamanho and len(diags) == len(rev_diags):
            return 1
        return 0


def build(entrada):
    """
    Função que constroi a matriz
    """
    p = len(entrada)
    mat = [['0' for x in range(p)] for y in range(p)]
    lista = []
    lista1 = []
    cont_rainhas = 0
    line = 0
    for i in entrada:
        for kk in i:
            lista1.append(kk)
        lista.append(lista1)
        for jj in lista:
            for w in jj:
                if w == '1':
                    cont_rainhas += 1
                    indice = lista[0].index(w)
                    mat[line][indice] = '1'
                    line += 1
        lista = []
        lista1 = []
    if p != 8 or cont_rainhas != 8 or len(mat) != 8:
        return -1
    return Solution.solve(mat)
