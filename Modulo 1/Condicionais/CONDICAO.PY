nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
carteira = input("Possue carteira de motorista? (1-sim | 2-não)")
if idade >= 18:
    print("Maior de idade")
    if carteira == "1": 
        print("Permitido dirigir ✔️")
    else:
        print("Não permitido dirigir ✖️")
    print("--------------------------")
else:
    print("Menor de idade")
    print("--------------------------")
print(f"Seu nome é:  {nome}")
print(f"Sua idade é: {idade}")
