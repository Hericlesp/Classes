class Funcionario():
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo 
    
class Gerente(Funcionario):
    def __init__(self, setor):
        self.setor = setor
        
class Dev(Funcionario):
    def __init__(self, linguagem):
        self.linguagem = linguagem
        
class Estag(Funcionario):
    def __init__(self, supervisor):
        self.supervisor = supervisor
        
        
print('='*50)
print('COMPLETE SEUS DADOS'.center(50))
print('='*50)

nome = str(input('QUAL SEU NOME:  \n'.center(50)))
cargo = str(input('QUAL CARGO DESEJADO:  \n'.center(50)))
setor = str(input('QUAL SETOR DESEJADO:  \n'.center(50)))
linguagem = str(input('QUAL LINGUAGEM SABES:  \n'.center(50)))
supervisor = str(input('QUAL SUPERVISOR CONHECE:  \n'.center(50)))