Polícia e Ladrão
O jogo "Polícia e Ladrão" consiste em dois grupos: o grupo da polícia e o grupo dos ladrões. Os ladrões devem se esconder e a polícia deve capturá-los. Caso a polícia consiga capturá-los e prendê-los, os ladrões perdem o jogo e caso a polícia não consiga capturá-los, os ladrões vencem o jogo.

Este programa resolve um problema relacionado a este jogo. Uma matriz 5x5 é usada para representar um labirinto em que o número 0 indica um espaço livre e o número 1 indica um espaço que deve ser evitado. Os ladrões sempre se escondem no último espaço do labirinto, e os policiais devem alcançar o último espaço para ganhar o jogo. Os policiais podem se mover apenas em espaços livres (0), e não podem se mover na diagonal.

A solução implementada usa busca em profundidade (DFS) para encontrar um caminho livre que conecte o início (posição 0,0) e o fim (posição 4,4) do labirinto. A função dfs é uma implementação recursiva da busca em profundidade. A função solve inicializa a matriz visited com False para todas as posições e chama dfs para procurar um caminho livre. Se um caminho livre for encontrado, a função retorna "COPS", caso contrário retorna "ROBBERS".

Como usar
O programa pode ser usado em linha de comando. Para isso, basta executar o arquivo police_and_thief.py passando como argumento um arquivo de entrada contendo a definição dos labirintos. Por exemplo:

python police_and_thief.py input.txt
O arquivo de entrada deve ter o seguinte formato:

Onde T é o número de labirintos a serem resolvidos, e a e b representam os elementos da matriz. Cada labirinto deve estar separado por uma linha em branco.

Testes Automatizados
Foram implementados testes automatizados para verificar a funcionalidade da função solve em diferentes situações:

Matriz com caminho livre (resultado esperado: "COPS")
Matriz sem caminho livre (resultado esperado: "ROBBERS")
Matriz com obstáculo na posição inicial (resultado esperado: "ROBBERS")
Matriz com obstáculo na posição final (resultado esperado: "ROBBERS")
Matriz com obstáculo no caminho (resultado esperado: "ROBBERS")
Os testes podem ser executados com o comando:

bash
Copy code
python test_police_and_thief.py
