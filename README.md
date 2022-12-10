# Equation of Drake Simulator
 
Este projeto foi desenvolvido em `Python` para a disciplina de `Estruturas de Dados`, lecionada pelo professor `Ernesto Trajano de Lima Neto`. O trabalho consiste em encontrar uma problemática presente no canal `Ciência todo dia` e realizar um algoritmo que ajude a resolver! O algoritmo deve utilizar alguma `Estrutura de Dados` que auxilie na resolução do problema e algum dos algoritmos aprendidos na disciplina.

![UI do Simulador Equacao de Drake](https://user-images.githubusercontent.com/86852231/206710842-3f8b8996-5ef3-465c-8876-3e43836e02ad.png)

## O problema
O problema escolhido foi baseado na pergunta, `Quais as possibilidades de haver vida inteligente no sistema solar?` Devido o consumo de filmes, livros e quadrinhos de `cultura pop` sobre aliens e viagens espaciais, eu achei esse questionamento super interessante e fiquei curioso para saber se havia algum `método` utilizado para fazer essas suposições!

_Se existe um Thanos lá fora, precisamos saber logo, não acha! rs_
## A solução
A solução encontrada foi a `Equação de Drake`, a qual é um `argumento probabilístico` usado para estimar o número de civilizações extraterrestres ativas em nossa galáxia com as quais poderíamos ter chances de estabelecer comunicação. Para implementar esta equação de forma a encontrar as mais `variadas possibilidades`, pensou-se em um `simulador da equação` que armazenasse as variáveis nos cenários otimistas quanto nos cenários pessimistas, de forma a retornar todas as possibilidades!

## A estrutura de Dados
A equação de Drake fornece variáveis que são multiplicadas para se chegar a um valor, entretanto, não existem valores exatos para algumas dessas variáveis, sendo sempre estipulado `cenários pessimistas e otimistas` com base em estudos de especialistas. Devido essa ambiguidade de valores para cada uma dessas variáveis, `existem diversas possibilidades, ou caminhos que podem ser traçados` para se obter um valor dentre os muitos.

Assim, tendo em vista os diversas possibilidades e caminhos que podem ser trilhados, pensou-se em uma `estrutura de dados` que além de armazenar essas variáveis `estabelecesse as conexões entre elas de forma a possibilitar variados caminhos` e a diferenciação entre caminhos otimistas e pessimistas. Assim, optou-se pelo a utilização do `grafo`, uma vez que esta estrutura possui nós que podem armazenar os valores bem como suas conexões, inclusive podendo atribuir pesos as arestas que podem separar os cenários otimistas dos pessimistas, além de possibilitar percorrer o grafo de diversas formas, o que é útil para realizar as possibilidades de resultados da `Equação de Drake`.
