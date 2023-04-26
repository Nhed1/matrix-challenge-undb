def searchAlgorithm(matrix, visited, currentRow, currentColumn):
    # verifica se a matriz está fora das limitações, caso verdadeira a função retorna falso e não executa a busca
    if currentRow < 0 or currentRow >= 5 or currentColumn < 0 or currentColumn >= 5:
        return False
    
    # verifica se já a celula da matriz está bloqueada (número 1) ou já foi visitada
    if matrix[currentRow][currentColumn] == 1 or visited[currentRow][currentColumn]:
        return False
    
    # indica que a célula já foi visitada
    visited[currentRow][currentColumn] = True
    
    # a posição (4,4) é a ultima da matriz, onde os robbers estão, logo significa que os cops chegaram aos robbers
    if currentRow == 4 and currentColumn == 4:
        return True
    
    # aqui acontece a busca de forma recursiva em todas as possiveis direções, até parar na seção anterior que é quando chega ao final na posição (4,4)
    positionDown = searchAlgorithm(matrix, visited, currentRow+1, currentColumn) 
    positionUp = searchAlgorithm(matrix, visited, currentRow-1, currentColumn) 
    positionRight = searchAlgorithm(matrix, visited, currentRow, currentColumn+1) 
    positionLeft = searchAlgorithm(matrix, visited, currentRow, currentColumn-1) 
    return positionDown or positionUp or positionRight or positionLeft


def solve(matrix):
    visited = [[False for _ in range(5)] for _ in range(5)]
    
    if searchAlgorithm(matrix, visited, 0, 0):
        return "COPS"
    else:
        return "ROBBERS"


testsCase = int(input("digite o número de casos de teste: "))

for _ in range(testsCase):
    matrix = []
    for i in range(5):
        row = list(map(int, input("digite a linha " + str(i) + " da matriz: ").split()))
        matrix.append(row)
    
    print(solve(matrix))
