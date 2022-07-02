'''
5. Quais estruturas de laço o Python suporta? 
Dê um exemplo simples de uso apropriado para cada tipo
de laço.
'''

# sabe o numero de iterações
# for (range)
# tamaho de lista
lista = [1, 10, 100, 1_000, 10_000]
for i in range(len(lista)):
    print(i)

# intervalo 0->5
for i in range(0, 5):
    print(i)

# não sabe o numero de iterações
# while (conditions)
n=0
while (n <= 5):
    print(n)
    n +=1
