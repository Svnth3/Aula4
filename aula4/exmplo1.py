valor_compra = float(input("Insira o valor da compra: "))
valor_desconto = float(0.16)

if valor_compra > 250:
    valor_compra = valor_compra - (valor_compra * valor_desconto)
    print(f'O valor será de R${valor_compra:.2f}')
else:
    print(f"O valor será de R${valor_compra:.2f}")
