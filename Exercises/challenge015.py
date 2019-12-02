km=float(input('Digite o números de km rodados:'))
dias=int(input('Digite por quantos dias foi alugado:'))
pk= (0.15) * (km)
pd= (60) * (dias)
pt= pk + pd
print('O preço a ser pago por {} km rodado(s) e durante {} dia(s) será: {:.5} reais' .format (km,dias,pt))
