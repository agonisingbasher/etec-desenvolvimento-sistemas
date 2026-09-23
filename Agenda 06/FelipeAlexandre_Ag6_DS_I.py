# Arquivo: FelipeAlexandre_Ag6_DS_I.py
# Sistema de Desconto Progressivo para Loja Online

def calcular_desconto():
    print("=== Sistema de Caixa ===")
    
    try:
        # Solicita ao usuário que insira o valor total da compra
        # A função float() permite que o usuário digite números decimais
        valor_compra = float(input("Digite o valor total da compra (R$): "))

        # Validação básica para evitar valores negativos ou zerados
        if valor_compra <= 0:
            print("Valor inválido. A compra deve ser maior que zero.")
            return

        # Estrutura de decisão (if/elif/else) para aplicar a regra de desconto
        # A ordem lógica evita redundâncias (ex: não é preciso testar se é >= 200 no elif)
        if valor_compra < 200.00:
            porcentagem_desconto = 5
        elif valor_compra < 300.00:
            porcentagem_desconto = 10
        else:
            porcentagem_desconto = 15

        # Calcula o valor financeiro do desconto e o preço final
        valor_desconto = valor_compra * (porcentagem_desconto / 100)
        valor_final = valor_compra - valor_desconto

        # Exibe o cupom fiscal formatado com duas casas decimais (.2f)
        print("\n--- Resumo da Compra ---")
        print(f"Valor da compra: R$ {valor_compra:.2f}")
        print(f"Desconto aplicado: {porcentagem_desconto}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {valor_final:.2f}")
        print("------------------------\n")

    except ValueError:
        # Tratamento de erro caso o usuário digite texto em vez de números
        print("Erro: Por favor, insira apenas valores numéricos válidos.")

# Chama a função para executar o programa
if __name__ == "__main__":
    calcular_desconto()
