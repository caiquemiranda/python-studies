Classe
Python é uma linguagem que suporta o paradigma de programação orientada a objetos. Como outras linguagens OOP, Python tem classes que são wireframes de objetos definidos. Python suporta herança de classe. Uma classe pode ter muitas subclasses, mas só pode herdar diretamente de uma superclasse.

Sintaxe

class NomeDaClasse(objeto):
    """Esta é uma aula"""
    variável_classe
    def _init_(self,*args):
        self.args = args
    def _repr_(self):
        return "Algo para representar o objeto como uma string"
    def other_method(self,*args):
        #faça outra coisa

Exemplo

class Cavalo(objeto):
    """Cavalo representa um Cavalo"""
    espécie = "Equus ferus caballus"
    def _init_(self,color,weight,wild=False):
        self.color = cor
        self.weight = peso
        self.wild = selvagem
    def _repr_(self):
        return "%s cavalo pesando %fe estado selvagem é %b" % (self.color,self.weight,self.wild)
    def make_sound(self):
        imprima "neighh"
    def movimento (auto):
        retornar "andar"

Sintaxe

class NomeDaClasse(SuperClasse):
    # o mesmo que acima
    # use a palavra-chave 'super' para obter de cima

Exemplo

class Cavalo de Corrida(Cavalo):
    """Um cavalo mais rápido que herda de Cavalo"""
    def movimento (auto):
        retornar "executar"
    def movimento_lento(self):
        return super(Cavalo,auto).movimento()
    def _repr_(self):
        return "%s cavalo de corrida pesando %fe status selvagem é %b" (self.color,self.weight,self.wild)

>> cavalo3 = RaceHorse("branco",200)
>> imprimir cavalo3.movement_slow()
"andar"
>> imprimir cavalo3.movimento()
"corre"

Comentários
Comentários de linha única
Aumentar o código com descrições legíveis por humanos pode ajudar a documentar as decisões de design.

Exemplo

# este é um comentário de linha única.

Comentários de várias linhas
Alguns comentários precisam abranger várias linhas, use isso se você tiver mais de 4 comentários de linha única em uma linha.

Exemplo

'''
isto é
uma multilinha
comentar, eu sou útil para comentar todo
pedaços de código muito rápido
'''

Dicionários
Os dicionários são o tipo de dados associativo integrado do Python. Um dicionário é feito de pares chave-valor onde cada chave corresponde a um valor. Assim como os conjuntos, os dicionários não são ordenados. Algumas notas sobre chaves e valores: A chave deve ser imutável e passível de hash, enquanto o valor pode ser de qualquer tipo. Exemplos comuns de chaves são tuplas, strings e números. Um único dicionário pode conter chaves de vários tipos e valores de vários tipos.

Sintaxe

dict() #cria um novo dicionário vazio
{} #cria um novo dicionário vazio

Exemplo

>> my_dict = {}
>> content_of_value1 = "abcd"
>> content_of_value2 = "wxyz"
>> my_dict.update({"key_name1":content_of_value1})
>> my_dict.update({"key_name2":content_of_value2})
>> meu_dict
{'key_name1':"abcd", 'key_name2':"wxyz"}
>> my_dict.get("key_name2")
"W x y Z"

Sintaxe

{chave1:valor1,chave2:valor2}

Exemplo

>> my_dict = {"key1":[1,2,3],"key2":"Sou uma string",123:456}
>> my_dict["key1"] #[1,2,3]
>> my_dict[123] #456
>> my_dict["new key"] = "Novo valor"
>> imprimir meu_dict
{"key2":"Sou uma string", "new key":"Novo valor", "key1":[1,2,3],123:456}

Funções
As funções do Python podem ser usadas para abstrair pedaços de código para usar em outro lugar.

Sintaxe

def nome_da_função(parâmetros):
  # Algum código aqui

Exemplo

def add_two(a, b):
  c = a + b
  retornar c

# ou sem a atribuição provisória a c
def add_two(a, b):
  retornar a + b

Sintaxe

def function_name(parâmetros, named_default_parameter=valor):
  # Algum código aqui

Exemplo

def shout(exclamation="Ei!"):
  imprimir exclamação

shout() # Exibe "Ei!"

shout("Cuidado!") # Exibe "Cuidado!"

Objetos de função
As funções Python são objetos de primeira classe, o que significa que podem ser armazenadas em variáveis ​​e listas e podem até ser retornadas por outras funções.

Exemplo

# Armazenando objetos de função em variáveis:

def diga_olá(nome):
  return "Olá," + nome

foo = say_hello("Alice")
# Agora o valor de 'foo' é "Olá, Alice"

divertido = diga_olá
# Agora o valor de 'fun' é um objeto de função que podemos usar como a função original:
bar = diversão("Bob")
# Agora o valor de 'bar' é "Hello, Bob"

Exemplo

# Retornando funções de funções

# Uma função simples
def say_hello(saudável, saudado):
  return "Olá, " + saudação + ", sou " + saudação + "."

# Podemos usar assim:
print say_hello("Alice", "Bob") # Exibe "Olá, Bob, eu sou Alice."

# Também podemos usá-lo em uma função:
def Produce_greeting_from_alice(saudado):
  return say_hello("Alice", saudado)

print Produce_greeting_from_alice("Bob") # Exibe "Olá, Bob, sou Alice."

# Também podemos retornar uma função de uma função aninhando-as:
def Produce_greeting_from(greeter):
  def saudar (cumprimento):
    return say_hello(cumprimento, saudado)
  retorno saudar

# Aqui criamos uma função de saudação para Eva:
Produce_greeting_from_eve = Produce_greeting_from("Eve")
# 'produce_greeting_from_eve' agora é uma função:
print Produce_greeting_from_eve("Alice") # Exibe "Olá, Alice, eu sou Eve."

# Você também pode invocar a função diretamente se quiser:
print Produce_greeting_from("Bob")("Eve") # Exibe "Olá, Eve, eu sou Bob."

Exame