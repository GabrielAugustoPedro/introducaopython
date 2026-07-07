import uuid

class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, novoTitulo):
        self.__titulo = novoTitulo

    def getAutor(self):
        return self.__autor

    def setAutor(self, novoAutor):
        self.__autor = novoAutor

    def getDisponivel(self):
        return self.__disponivel

    def __setDisponivel(self):
        self.__disponivel = not(self.__disponivel)


    def emprestar(self):
        if self.__disponivel:
            self.__setDisponivel()
        else:
            print("Este livro está indisponível!")

    def devolver(self):
        if not self.__disponivel:
            self.__setDisponivel()
        else:
            print("Este livro está disponível!")

class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__idUsuario = uuid.uuid4()
        self.__livros_emprestados = []

    def getLivrosEmprestados(self):
        listaLivros = ""
        for livro in self.__livros_emprestados:
            listaLivros += f", {livro.getTitulo()}"
        return listaLivros

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome
        print("Nome alterado com sucesso!")

    def getId(self):
        return self.__idUsuario

    def setId(self):
        self.__idUsuario = uuid.uuid4()
        print("ID atualizado com sucesso!")

    def pegarLivro(self, livro):
        self.__livros_emprestados.append(livro)

    def devolverLivro(self, livro):
        self.__livros_emprestados.remove(livro)

livro1 = Livro("O Senhor dos Anéis", "Tolkien")
livro2 = Livro("O Código DaVinci", "Dan Brown")
livro3 = Livro("Don Casmurro", "Machado de Assis")

usuarioNovo1 = Usuario("Carlos Oliveira")
usuarioNovo2 = Usuario("Pedro Wilson")

print(livro1.getDisponivel())

if livro1.getDisponivel():
    usuarioNovo1.pegarLivro(livro1)
    livro1.emprestar()

if livro2.getDisponivel():
    usuarioNovo1.pegarLivro(livro2)
    livro2.emprestar()

if livro3.getDisponivel():
    usuarioNovo2.pegarLivro(livro3)
    livro3.emprestar()

usuarioNovo2.devolverLivro(livro3)
livro3.devolver()


if livro3.getDisponivel():
    usuarioNovo1.pegarLivro(livro3)
    livro3.emprestar()

print(f"O usuário {usuarioNovo1.getNome()} de ID {usuarioNovo1.getId()} tem emprestado {usuarioNovo1.getLivrosEmprestados()}")
print(f"O usuário {usuarioNovo2.getNome()} de ID {usuarioNovo2.getId()} tem emprestado {usuarioNovo2.getLivrosEmprestados()}")
