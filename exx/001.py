'''

Conversor de medidas

O usuário irá digitar o numeral em metros e o programa fará
a conversão

'''

medida = float(input('Digite um numero em metros para conversão: '))

km = medida*.001
hm = medida*.01
dam = medida*.1
m = medida 
dm = medida*10
cm = medida*100
mm = medida*1000

print(f' Km = {km}')
print(f' hm = {hm}')
print(f' dam = {dam}')
print(f' m = {m}')
print(f' dm = {dm}')
print(f' cm = {cm}')
print(f' mm = {mm}')