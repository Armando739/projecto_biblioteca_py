class Livro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor


class TabelaHashBiblioteca:
    def __init__(self, tamanho=100):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.contador = 0

    def hash_function(self, isbn):
        return hash(isbn) % self.tamanho

    def inserir_livro(self, livro):
        indice = self.hash_function(livro.isbn)

        # Verificar se livro já existe
        for l in self.tabela[indice]:
            if l.isbn == livro.isbn:
                print(f"Livro com ISBN {livro.isbn} já existe!")
                return False

        self.tabela[indice].append(livro)
        self.contador += 1
        print(f"Livro '{livro.titulo}' inserido com sucesso!")
        return True

    def buscar_livro(self, isbn):
        indice = self.hash_function(isbn)

        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                return livro

        return None

    def remover_livro(self, isbn):
        indice = self.hash_function(isbn)

        for i, livro in enumerate(self.tabela[indice]):
            if livro.isbn == isbn:
                removed = self.tabela[indice].pop(i)
                self.contador -= 1
                print(f"Livro '{removed.titulo}' removido!")
                return True

        print(f"Livro com ISBN {isbn} não encontrado!")
        return False

    def mostrar_estatisticas(self):
        print(f"\n=== ESTATÍSTICAS DA BIBLIOTECA ===")
        print(f"Total de livros: {self.contador}")
        print(f"Tamanho da tabela: {self.tamanho}")
        print(f"Fator de carga: {self.contador / self.tamanho:.2f}")

        # Mostrar colisões
        colisoes = sum(1 for lista in self.tabela if len(lista) > 1)
        print(f"Número de colisões: {colisoes}")


# Exemplo de uso
if __name__ == "__main__":
    biblioteca = TabelaHashBiblioteca(10)

    # Inserir livros
    biblioteca.inserir_livro(Livro("12345", "Python para Iniciantes", "João Silva"))
    biblioteca.inserir_livro(Livro("67890", "Algoritmos Avançados", "Maria Santos"))
    biblioteca.inserir_livro(Livro("54321", "Estruturas de Dados", "Carlos Oliveira"))

    # Buscar livro
    livro = biblioteca.buscar_livro("12345")
    if livro:
        print(f"\nLivro encontrado: {livro.titulo} por {livro.autor}")

    # Mostrar estatísticas
    biblioteca.mostrar_estatisticas()
