# Projeto Biblioteca Py

Este projeto implementa um sistema de biblioteca digital utilizando estruturas de dados e algoritmos eficientes para gerenciamento de livros e recomendações.

## Visão Geral

O projeto é composto por dois módulos principais:

1. **Tabela Hash para Gerenciamento de Livros** (`tabelha_hash.py`)
2. **Algoritmo de Grafo para Recomendações** (`algoritmo_grafo.py`)

## Módulo 1: Tabela Hash para Gerenciamento de Livros (`tabelha_hash.py`)

Este módulo implementa uma tabela hash personalizada para armazenar, buscar e gerenciar informações sobre livros em uma biblioteca.

### Estrutura:

- **Classe `Livro`**: Representa um livro com ISBN, título e autor.
- **Classe `TabelaHashBiblioteca`**: Implementa uma tabela hash com tratamento de colisões por encadeamento.

### Funcionalidades:

- **Inserção de livros**: Adiciona novos livros à biblioteca com verificação de duplicatas.
- **Busca de livros**: Localiza livros rapidamente usando o ISBN como chave.
- **Remoção de livros**: Remove livros da biblioteca.
- **Estatísticas**: Fornece informações sobre o uso da tabela hash, como número total de livros, fator de carga e colisões.

### Algoritmo:

A tabela hash utiliza uma função de hash baseada no ISBN do livro para determinar o índice onde o livro será armazenado. O tratamento de colisões é feito por encadeamento (cada posição da tabela contém uma lista de livros).

## Módulo 2: Algoritmo de Grafo para Recomendações (`algoritmo_grafo.py`)

Este módulo implementa um sistema de recomendação de livros usando estruturas de grafos e algoritmos de busca.

### Estrutura:

- **Classe `GrafoRecomendacao`**: Representa um grafo não direcionado onde os vértices são livros e as arestas representam relações entre livros.

### Funcionalidades:

- **Adição de livros**: Adiciona livros ao grafo como vértices.
- **Criação de conexões**: Estabelece relações entre livros (ex: livros da mesma categoria, tema ou autor).
- **Recomendação de livros**: Utiliza busca em largura (BFS) para encontrar livros relacionados a um livro inicial.
- **Encontrar caminho**: Usa BFS para encontrar o caminho mais curto entre dois livros no grafo.

### Algoritmos:

- **Busca em Largura (BFS)**: Utilizado tanto para recomendações quanto para encontrar caminhos entre livros.
- **Representação de grafo**: Utiliza lista de adjacência com defaultdict para eficiência.

## Uso

Ambos os módulos incluem exemplos de uso na seção `if __name__ == "__main__":` que demonstram como utilizar as funcionalidades implementadas.

## Benefícios

- **Eficiência**: A tabela hash permite operações de busca, inserção e remoção em tempo médio O(1).
- **Recomendações inteligentes**: O sistema de grafos permite encontrar livros relacionados de forma eficiente.
- **Escalabilidade**: Ambas as estruturas podem lidar com grandes quantidades de dados.
- **Organização**: Os livros podem ser explorados e navegados por relações temáticas ou de conteúdo.

## Aplicações

Este sistema pode ser usado em:
- Bibliotecas digitais
- Plataformas de leitura
- Sistemas de recomendação de livros
- Catálogos de livros em instituições educacionais

https://github.com/Armando739/projecto_biblioteca_py.git
