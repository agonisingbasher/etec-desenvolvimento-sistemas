# Programa de Pesquisa de Opinião - TudoWeb
# Desenvolvido para coletar e analisar o grau de satisfação dos clientes.

# Inicialização de contadores e acumuladores
qtd_excelente = 0
qtd_ruim = 0
total_entrevistados = 10  # Ajustado para 10 conforme os testes exigidos na instrução

print("=" * 45)
print("   BEM-VINDO À PESQUISA DE SATISFAÇÃO TUDOWEB")
print("=" * 45)

# Loop de repetição para coletar os dados dos entrevistados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado(a) {i} de {total_entrevistados}:")
    
    # Coleta de dados básicos
    nome = input("Digite o nome do entrevistado: ")
    
    # Tratamento básico para a idade (garantindo número inteiro)
    try:
        idade = int(input("Digite a idade do entrevistado: "))
    except ValueError:
        print("Idade inválida. Considerando 0 para prosseguir.")
        idade = 0

    # Coleta da opinião com validação
    print("Opiniões disponíveis:")
    print(" [1] - EXCELENTE")
    print(" [2] - BOM")
    print(" [3] - RUIM")
    
    opiniao = int(input("Digite o número correspondente à opinião: "))
    
    # Estrutura de decisão para contabilizar os votos
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    elif opiniao == 2:
        # Apenas para registrar que o voto foi computado, caso necessário
        pass
    else:
        print("Opção inválida! Este voto não será contabilizado nas categorias principais.")

# Exibição dos resultados finais consolidados
print("\n" + "=" * 45)
print("          RESULTADO FINAL DA PESQUISA")
print("=" * 45)
print(f"Total de entrevistados participantes: {total_entrevistados}")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("=" * 45)
