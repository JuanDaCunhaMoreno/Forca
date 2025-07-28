Jogo da Forca
---
Descrição
---
Este é um jogo da forca simples e interativo desenvolvido em Python. O jogo permite que o jogador escolha entre diferentes categorias de palavras e tente adivinhar a palavra oculta antes que o boneco da forca seja completamente desenhado.

Funcionalidades
---
•
Seleção de Categoria: Escolha entre diversas categorias de palavras (Frutas, Animais, Cores, Países, Objetos, Profissões).

•
Interface Visual: Exibição do boneco da forca progredindo a cada erro.

•
Validação de Entrada: Garante que o jogador insira apenas uma letra por vez e que seja um caractere alfabético.

•
Controle de Chances: O número de chances é dinâmico, baseado no tamanho da palavra.

•
Feedback de Letras Erradas: Mostra as letras que já foram tentadas e estão incorretas.

Como Jogar
---
1.
O jogo apresentará uma lista de categorias de palavras.

2.
Escolha uma categoria digitando o número correspondente.

3.
Tente adivinhar a palavra secreta, digitando uma letra por vez.

4.
Se a letra estiver na palavra, ela será revelada nas posições corretas.

5.
Se a letra não estiver na palavra, você perderá uma chance e uma parte do boneco da forca será desenhada.

6.
O jogo termina quando você adivinhar a palavra (vitória) ou quando suas chances acabarem e o boneco da forca estiver completo (derrota).

Estrutura do Projeto
---
O projeto é composto pelos seguintes arquivos Python:

•
main.py: O ponto de entrada do jogo. Inicia a função game().

•
jogo.py: Contém a lógica principal do jogo da forca, incluindo a seleção de categoria, o loop do jogo, a validação de entradas e a verificação de vitória/derrota.

•
palavras.py: Armazena as listas de palavras organizadas por categoria.

•
interface.py: Contém funções para limpar a tela do terminal e para exibir o desenho do boneco da forca de acordo com as chances restantes.

