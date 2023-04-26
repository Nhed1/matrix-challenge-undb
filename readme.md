# Curso: Engenharia de Software - UNDB

## Disciplina: ESTRUTURA DE DADOS AVANÇADAS

## Desafio 4.0

## Alunos: Leonardo Garreto, Lucas Melonio, Sergio Passinho

### Algoritimo Polícia e Ladrão

- Este programa resolve um problema relacionado ao jogo de policia e ladrão. Uma matriz 5x5 é usada para representar um labirinto em que o número 0 indica um espaço livre e o número 1 indica um espaço que deve ser evitado. Os ladrões sempre se escondem no último espaço do labirinto, e os policiais devem alcançar o último espaço para ganhar o jogo. Os policiais podem se mover apenas em espaços livres (0), e não podem se mover na diagonal.

- A solução implementada usa busca em profundidade (DFS) para encontrar um caminho livre que conecte o início (posição 0,0) e o fim (posição 4,4) do labirinto. A função dfs é uma implementação recursiva da busca em profundidade. A função 'solve` inicializa a matriz 'visited' com 'False' para todas as posições e chama dfs para procurar um caminho livre. Se um caminho livre for encontrado, a função retorna "COPS", caso contrário retorna "ROBBERS".

- Como usar:

O programa pode ser usado em linha de comando. Para isso, basta executar o arquivo matrix.py

```
python matrix.py
```

Testes Automatizados
Foram implementados testes automatizados para verificar a funcionalidade da função 'solve' em diferentes situações:

- Matriz com caminho livre (resultado esperado: "COPS")
- Matriz sem caminho livre (resultado esperado: "ROBBERS")

Como executar os testes

```
python test_matrix.py
```
