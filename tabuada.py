def tabuada():
    try:
        num = int(input("Digite um número inteiro para ver a tabuada: "))
    except ValueError:
        print("Erro: você precisa digitar um número inteiro válido.")
        return  # Sai da função se o input for inválido

    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
