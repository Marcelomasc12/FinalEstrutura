class Node:
    def __init__(self, content): 
        self.content = content
        self.left = None
        self.right = None

    def __str__(self):
        return self.content

class ArvoreDiagnostico:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def iniciarDiagnostico(self, node):
        while node.left is not None or node.right is not None:
            print(node.content)
            resposta = input("(s/n): ")

            if resposta == "s":
                node = node.left
            elif resposta == "n":
                node = node.right
            else:
                print("Por favor, responda apenas com 's' ou 'n'.")
        
        print("\nDiagnóstico provável:", node.content)

    def construirArvore(self):
        self.root = Node("Está com febre?")

        febre_sim = Node("Está com dor de cabeça?")
        febre_nao = Node("Está com coriza?")
        self.root.left = febre_sim
        self.root.right = febre_nao

        febre_sim.left = Node("Está com manchas vermelhas no corpo?")
        febre_sim.right = Node("Está com tosse?")
        febre_nao.left = Node("Está com dor de garganta?")
        febre_nao.right = Node("Está se sentindo muito cansado?")

        febre_sim.left.left = Node("Pode ser dengue.")
        febre_sim.left.right = Node("Pode ser virose.")

        febre_sim.right.left = Node("Está com dor muscular?")
        febre_sim.right.right = Node("Pode ser infecção leve.")

        febre_sim.right.left.left = Node("Pode ser gripe forte.")
        febre_sim.right.left.right = Node("Pode ser resfriado.")  # único resfriado

        febre_nao.left.left = Node("Pode ser rinite.")            # novo diagnóstico
        febre_nao.left.right = Node("Pode ser alergia.")

        febre_nao.right.left = Node("Pode ser estresse.")
        febre_nao.right.right = Node("Pode ser apenas fadiga leve.")

# Execução
arvore = ArvoreDiagnostico()
arvore.construirArvore()
arvore.iniciarDiagnostico(arvore.getRoot())

