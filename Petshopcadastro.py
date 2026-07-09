class Animal:
    def __init__(self, nome, idade, especie, tutor):
        self.__nome = nome
        self.__idade = idade
        self.__especie = especie
        self.__tutor = tutor
    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getEspecie(self):
        return self.__especie

    def getTutor(self):
        return self.__tutor.getNome()

    def setNome(self, novoNome):
        self.__nome = novoNome

    def setIdade(self, novaIdade):
        self.__idade = novaIdade

    def setEspecie(self, novaEspecie):
        self.__especie = novaEspecie

    def setTutor(self, novoTutor):
        self.__tutor = novoTutor

    def emitir_som(self):
        return "Som Qualquer"

    def cadastrarPet(self):
        # cadastro é tratado diretamente no menu.
        print("Método cadastrarPet da classe Animal chamado.")

    def atualizarPet(self):
        print("Método atualizarPet da classe Animal chamado.")

    def listarPet(self):
        print("Método listarPet da classe Animal chamado.")

    def removerPets(self, listaPets):#Remove o animal

        nome_busca = input("Digite o nome do animal que deseja remover: ")

        busca = False
        for pet in listaPets:
            if pet.getNome() == nome_busca:
                listaPets.remove(pet)
                print("Animal removido com sucesso!")
                busca = True
                break
        if not busca:
            print(f"Animal com nome '{nome_busca}' não encontrado.")


    def listarPet_petshop(listaPets):
        if not listaPets:
            print("Nenhum animal cadastrado ainda.")
        else:
            print("--- Lista de Animais ---")
            for pet in listaPets:
                print(f"Nome: {pet.getNome()}, Idade: {pet.getIdade()}, Espécie: {pet.getEspecie()}, Tutor: {pet.getTutor()}, Som: {pet.emitir_som()}")
            print("------------------------")

#Classe para cachorro
class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.getNome()} diz: Au Au"

#Classe para gato
class Gato(Animal):
    def emitir_som(self):
        return f"{self.getNome()} diz: Miau"

#Classe para tutor do animal
class Tutor:
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    #Redefinindo o tutor
    def setNome(self, novoNome):
        self.__nome = novoNome

#Lista de animais a ser preenchida
listaPets = []

print("Bem vindo ao Pet Shop!")

while True:
  #Menu
   print("\nEscolha uma opção:")
   print("1. Cadastrar um novo animal")
   print("2. Listar todos os animais")
   print("3. Atualizar Pet")
   print("4. Remover Pet")
   print("5. Sair")
   escolha = input()


   match escolha:
      case "1":
        # cadastrar o pet
          nome = input("Digite o nome do animal: ")
          idade = input("Digite a idade do animal: ")
          especie = input("Digite a especie do animal (Cachorro/Gato): ")
          nome_tutor = input("Digite o nome do tutor do animal: ")

          novo_tutor = Tutor(nome_tutor)

          #Pedindo a especie
          if especie.lower() == "cachorro":
              novo_animal = Cachorro(nome, idade, especie, novo_tutor)
          elif especie.lower() == "gato":
              novo_animal = Gato(nome, idade, especie, novo_tutor)
          else:
              print("Espécie não reconhecida. Cadastrando como animal genérico.")
              novo_animal = Animal(nome, idade, especie, novo_tutor)

          listaPets.append(novo_animal)
          print("Animal cadastrado com sucesso!")

      case "2":
        # listar animais
        Animal.listarPet_petshop(listaPets)

      case "3":
        # atualizar pet
        nome_busca = input("Digite o nome do animal que deseja atualizar: ")
        encontrado = False
        #Buscar nome na lista para atualizar
        for pet in listaPets:
          if pet.getNome() == nome_busca:
            nova_idade = input("Digite a nova idade do animal: ")
            pet.setIdade(nova_idade)
            print("Animal atualizado com sucesso!")
            encontrado = True
            break
        #caso animal não esteja na lista
        if not encontrado:
            print(f"Animal com nome '{nome_busca}' não encontrado.")

      case "4":

          if listaPets:
            #remove animais
            remove_animal = Animal("remove", 0, "remove", Tutor("remove"))
            remove_animal.removerPets(listaPets)
          else:
            print("Nenhum animal cadastrado para remover.")

      case "5":
        #sair
        print("Saindo...")
        break
      case _:
        print("Opção inválida. Tente novamente.")
