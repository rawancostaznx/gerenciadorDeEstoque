Sistema de Gestão de Peças, Qualidade e Armazenamento

SOBRE O PROJETO

Este projeto foi desenvolvido como parte do Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento, da disciplina de Algoritmos e Lógica de Programação.

O objetivo é desenvolver um protótipo de sistema em Python capaz de auxiliar no controle de qualidade e armazenamento de peças produzidas em uma linha industrial.

O sistema recebe os dados de cada peça, verifica automaticamente se ela atende aos critérios de qualidade definidos, separa as peças aprovadas das reprovadas, organiza as peças aprovadas em caixas com capacidade limitada e gera um relatório final com os resultados do processo.

OBJETIVO

O sistema busca representar uma solução simples de automação para um processo que normalmente poderia ser realizado manualmente.

A partir dos dados informados pelo usuário, o programa consegue:

- Cadastrar novas peças;
- Avaliar automaticamente a qualidade das peças;
- Separar peças aprovadas e reprovadas;
- Informar os motivos de reprovação;
- Armazenar peças aprovadas em caixas;
- Fechar uma caixa quando ela atingir 10 peças;
- Remover peças cadastradas;
- Reorganizar as caixas após a remoção de uma peça aprovada;
- Listar caixas fechadas e a caixa atual;
- Gerar um relatório final do processo.

CRITÉRIOS DE QUALIDADE

Cada peça cadastrada é avaliada de acordo com três critérios:

Peso: entre 95g e 105g
Cor: azul ou verde
Comprimento: entre 10cm e 20cm

Para ser considerada aprovada, a peça precisa atender aos três critérios.

Caso um ou mais critérios não sejam atendidos, a peça é classificada como reprovada, e o sistema registra os respectivos motivos.

Exemplos

Peça aprovada:

Peso: 100g
Cor: azul
Comprimento: 15cm
Resultado: Aprovado

Peça reprovada:

Peso: 110g
Cor: vermelho
Comprimento: 15cm
Resultado: Reprovado

Motivos:
- Peso fora do padrão
- Cor fora do padrão

FUNCIONAMENTO DO SISTEMA

O programa é organizado em diferentes funções, cada uma responsável por uma etapa do processo.

1. Cadastro de peças

A função cadastrar_peca() recebe:

- ID da peça;
- Peso;
- Comprimento;
- Cor.

Essas informações são organizadas em um dicionário e enviadas para a função de avaliação.

2. Avaliação da qualidade

A função avaliar_peca() verifica os três critérios de qualidade.

Caso algum critério não seja atendido, o motivo é adicionado a uma lista de motivos.

A avaliação retorna um dos seguintes resultados:

Aprovado

ou

Reprovado

junto com os motivos encontrados, quando houver.

3. Armazenamento em caixas

As peças aprovadas são encaminhadas para a função adicionar_na_caixa().

A caixa atual possui capacidade máxima de 10 peças.

Quando a quantidade chega a 10:

1. A caixa é considerada fechada;
2. Ela é armazenada na lista de caixas fechadas;
3. A caixa atual é limpa;
4. Uma nova caixa pode começar a ser preenchida.

4. Remoção de peças

O sistema também permite remover uma peça utilizando seu ID.

A peça pode estar na lista de aprovadas ou na lista de reprovadas.

Quando uma peça aprovada é removida, as caixas são reorganizadas para manter a organização das peças restantes.

Essa reorganização é realizada pela função reorganizar_caixas().

5. Listagem de peças

A opção de listagem apresenta separadamente:

- Peças aprovadas;
- Peças reprovadas;
- Dados de cada peça;
- Motivos das reprovações.

6. Listagem de caixas

O sistema permite visualizar:

- Caixas que já foram fechadas;
- Quantidade de peças em cada caixa;
- Dados das peças presentes em cada caixa;
- Caixa atual e sua quantidade de peças.

7. Relatório final

A função gerar_relatorio() apresenta:

- Total de peças aprovadas;
- Total de peças reprovadas;
- Total geral de peças cadastradas;
- Quantidade de caixas utilizadas;
- Motivos das reprovações.

MENU INTERATIVO

O programa possui um menu principal para facilitar a utilização:

========================================
       GERENCIADOR DE ESTOQUE
========================================
1 - Cadastrar peça
2 - Listar peças
3 - Remover peça
4 - Listar caixas
5 - Gerar relatório
0 - Sair
========================================

Opções disponíveis

1 - Cadastrar peça
Permite inserir uma nova peça no sistema e realizar automaticamente sua avaliação.

2 - Listar peças
Exibe as peças aprovadas e reprovadas, incluindo os motivos das reprovações.

3 - Remover peça
Permite remover uma peça através do seu ID.

4 - Listar caixas
Exibe as caixas fechadas e a caixa que está atualmente sendo preenchida.

5 - Gerar relatório
Apresenta um resumo geral dos resultados do processo.

0 - Sair
Encerra a execução do programa.

CONCEITOS DE PROGRAMAÇÃO UTILIZADOS

Durante o desenvolvimento foram utilizados conceitos fundamentais de lógica de programação em Python, incluindo:

- Variáveis para armazenar informações;
- Listas para organizar peças e caixas;
- Dicionários para representar os dados de cada peça;
- Funções para dividir o sistema em diferentes responsabilidades;
- Estruturas condicionais (if/else) para tomar decisões;
- Estruturas de repetição (for e while);
- match/case para controlar as opções do menu;
- Entrada de dados com input();
- Saída de informações com print().

A divisão do programa em funções também facilita a organização, manutenção e compreensão do código.

COMO EXECUTAR

Pré-requisito

É necessário possuir o Python 3 instalado no computador.

Para verificar a instalação, execute no terminal:

python3 --version

ou:

python --version

Executando o programa

1. Baixe ou clone este repositório;
2. Abra o terminal na pasta do projeto;
3. Execute o arquivo Python:

python3 "Gerenciador de Estoque Final.py"

Caso o arquivo tenha outro nome, utilize o nome correspondente ao arquivo .py.

Após a execução, o menu principal será exibido no terminal.

ESTRUTURA DO PROJETO

projeto-gestao-pecas
|-- Gerenciador de Estoque Final.py
|-- README.md

O arquivo Python contém toda a lógica do sistema, enquanto este README apresenta as informações necessárias para compreender e executar o projeto.

POSSÍVEIS MELHORIAS FUTURAS

Em um cenário industrial real, o sistema poderia ser expandido para trabalhar com sensores, permitindo que informações como peso e dimensões fossem coletadas automaticamente.

Também seria possível utilizar Inteligência Artificial e visão computacional para auxiliar na identificação de características ou possíveis defeitos das peças.

Outra possibilidade seria integrar o sistema a equipamentos e sistemas industriais, permitindo que os dados fossem coletados e processados automaticamente durante a linha de produção.

USO DE INTELIGÊNCIA ARTIFICIAL

A Inteligência Artificial foi usada como apoio para estudar conceitos de programação, organizar e revisar partes do código e preparar a documentação e a parte teórica. O código foi analisado, adaptado e testado pelo aluno, que acompanhou e compreendeu o funcionamento da solução e permaneceu responsável pelas decisões e pela apresentação do projeto.


AUTOR

Rawan Silva da Costa.

Projeto desenvolvido para a disciplina de Algoritmos e Lógica de Programação — UniFECAF / Rocketseat.
