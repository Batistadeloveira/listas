def conversor_moeda():
    try:
        valor = float(input("Digite o valor em Reais (R$): "))
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite um número válido.")
        return  # Sai da função se erro
    
    try:
        taxa_cambio = float(input("Digite a taxa de câmbio para a moeda desejada: "))
        if taxa_cambio <= 0:
            raise ValueError("A taxa de câmbio deve ser maior que zero.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite um número válido.")
        return  # Sai da função se erro
    
    valor_convertido = valor * taxa_cambio
    print(f"Valor convertido: {valor_convertido:.2f}")

conversor_moeda()
