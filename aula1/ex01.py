# Dado (i) O ano atual, (ii) o nome de uma pessoa, e (iii) o ano do nascimento desta pessoa, mostre quantos anos esta pessoa tem no ano atual (ignore informações do dia e mês).
ano_atual = int(input("Digite o ano atual"))
nome = input("Digite o seu nome")
ano_nascimento = int(input("Digite o seu ano de nascimento"))

print(f"{nome}, você completa {ano_atual - ano_nascimento} neste ano.")