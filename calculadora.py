temp_str = input("Digite a temperatura: ")
escala = input("Digite a escala (C para Celsius, F para Fahrenheit): ").upper()

try:
    temperatura = float(temp_str)  # Tenta converter para número decimal
    
    if escala == "C":
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {resultado}°F")
    elif escala == "F":
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {resultado:.2f}°C")
    else:
        print("Erro: escala inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
except ValueError:
    print("Erro: você deve digitar um número válido para a temperatura.")
