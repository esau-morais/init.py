#Fatiamento
string = "Programação em Python"
print("A letra de número 15 é o: ",string[15])
print(string[:21])

#Análise
print(len(string),"caracteres;")
print(string.count("P"),"letras 'P';")
print(string.count("o",0,21),"letras 'o'")
print("Iniciou no caracter",string.find('Python'))
print("Não existe, portanto está no carater",string.find('Android'))
print("Existe o caracter Python?","Python" in string)
print(string.replace("Python","C++"))

#Transformação 1: Upper, lower, capitalize e title
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())

#Transformação 2: Strip, lstrip e rstrip
string2 = "  Olimpíada Brasileira de Informática  "
print(string2.strip())
print(string2.lstrip())
print(string2.rstrip())

#Transformação 3: Split
print(string.split())
print("|".join(string))

#Dica: Como fazer um programa que leia um texto longo:
print("""and – I have a dog and a cat. (Eu tenho um cão e um gato.)
also – I also have a bird (Eu também tenho um pássaro.)
too – I like chocolate and vanilla too. (Eu gusto de chocolate e baunilha também.)
then – I was calling, then she showed up. (Eu estava ligando, então ela apareceu.)""")