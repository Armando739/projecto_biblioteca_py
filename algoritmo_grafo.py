from collections import deque, defaultdict

class GrafoRecomendacao:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_livro(self, livro_id):
        if livro_id not in self.grafo:
            self.grafo[livro_id] = []
    
    def adicionar_conexao(self, livro1, livro2):
        self.grafo[livro1].append(livro2)
        self.grafo[livro2].append(livro1)
    
    def recomendar_livros(self, livro_inicial, max_recomendacoes=5):
        """Usa BFS para recomendar livros relacionados"""
        if livro_inicial not in self.grafo:
            return []
        
        visitados = set()
        fila = deque([livro_inicial])
        recomendacoes = []
        
        while fila and len(recomendacoes) < max_recomendacoes:
            atual = fila.popleft()
            
            if atual not in visitados:
                visitados.add(atual)
                
                # Adicionar vizinhos à fila
                for vizinho in self.grafo[atual]:
                    if vizinho not in visitados and vizinho != livro_inicial:
                        fila.append(vizinho)
                        
                        # Adicionar à lista de recomendações
                        if vizinho not in recomendacoes:
                            recomendacoes.append(vizinho)
        
        return recomendacoes
    
    def encontrar_caminho(self, inicio, fim):
        """Encontra conexão entre dois livros usando BFS"""
        if inicio not in self.grafo or fim not in self.grafo:
            return None
        
        fila = deque([(inicio, [inicio])])
        visitados = set([inicio])
        
        while fila:
            atual, caminho = fila.popleft()
            
            if atual == fim:
                return caminho
            
            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))
        
        return None

# Exemplo de uso
if __name__ == "__main__":
    sistema = GrafoRecomendacao()
    
    # Adicionar livros (IDs)
    livros = ["Python", "Algoritmos", "Matemática", "Física", "Programação", "IA"]
    for livro in livros:
        sistema.adicionar_livro(livro)
    
    # Criar conexões (livros relacionados)
    conexoes = [
        ("Python", "Programação"),
        ("Python", "Algoritmos"),
        ("Algoritmos", "Matemática"),
        ("Matemática", "Física"),
        ("Programação", "IA"),
        ("IA", "Matemática")
    ]
    
    for livro1, livro2 in conexoes:
        sistema.adicionar_conexao(livro1, livro2)
    
    # Testar recomendações
    print("=== SISTEMA DE RECOMENDAÇÃO DE LIVROS ===")
    livro_base = "Python"
    recomendacoes = sistema.recomendar_livros(livro_base)
    print(f"Livros recomendados a partir de '{livro_base}': {recomendacoes}")
    
    # Testar caminho entre livros
    caminho = sistema.encontrar_caminho("Python", "Física")
    print(f"\nCaminho de Python para Física: {' -> '.join(caminho) if caminho else 'Não encontrado'}")