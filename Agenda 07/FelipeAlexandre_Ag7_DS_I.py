# ==========================================
# Sistema de Classificação de Consumo de Água
# Aluno: Felipe Alexandre
# Curso: Desenvolvimento de Sistemas - Etec
# Agenda 7 - DS I
# ==========================================

def classificar_consumo():
    print("=== Companhia de Saneamento - Sistema de Classificação de Consumo ===")
    
    # Solicitar o tipo de imóvel
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
    
    # Validação do tipo de imóvel
    while tipo_imovel not in ["comercial", "casa", "apartamento"]:
        print("Tipo de imóvel inválido! Por favor, digite 'comercial', 'casa' ou 'apartamento'.")
        tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

    # Solicitar o consumo mensal de água em metros cúbicos (m3)
    try:
        consumo = float(input("Digite o consumo mensal de água em metros cúbicos (m³): "))
        if consumo < 0:
            print("O consumo não pode ser negativo.")
            return
    except ValueError:
        print("Entrada inválida! Por favor, digite um número decimal válido para o consumo.")
        return

    print("\n--- Resultado da Análise ---")
    
    # Regras de Negócio
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo <= 25):
        print("Consumo moderado – dentro do padrão residencial.")
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()
