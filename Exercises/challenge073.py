times = ("Palmeiras", "Santos", "Flamengo", "Internacional", "Atlético-MG"
     "Goiás", "Botafogo", "Bahia", "São Paulo", "Corinthians",
          "Grêmio", "Athletico-PR", "Ceará", "Fortaleza", "Vasco",
          "Fluminense", "Chapecoense", "Cruzeiro", "CSA", "Avaí")
def lin():
    print("-=" * 12)


lin()
print(" == BRASILEIRÃO 2019 == ")
lin()

print(f"Cinco primeiros times: {times[0:5]}")
print(f"Quatro últimos times: {times[16:21]}")
print(f"Ordem de times, em ordem alfabética: {sorted(times)}")
print("Posição do Chapecoense: {}° Lugar".format(times.index("Chapecoense")+2))
