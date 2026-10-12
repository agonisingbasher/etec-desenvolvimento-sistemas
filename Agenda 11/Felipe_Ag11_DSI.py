from colorama import init, Fore, Style
import time

# Inicializa a biblioteca colorama
init()

# Lista armazenando as mensagens dos níveis do reservatório
# O índice 0 corresponde ao Nível 1, o índice 1 ao Nível 2, e assim por diante.
mensagens_alerta = [
    "Muito baixo (crítico)", # Nível 1
    "Baixo",                 # Nível 2
    "Médio",                 # Nível 3
    "Alto",                  # Nível 4
    "Muito alto (alerta)"    # Nível 5
]

def definir_cor(nivel):
    """
    Função responsável por definir a cor da mensagem conforme o nível informado.
    """
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE # Cor padrão para níveis fora do esperado

def exibir_status_reservatorio(nivel):
    """
    Exibe a mensagem com a cor correspondente e restaura o estilo padrão em seguida.
    """
    # Subtrai 1 do nível para acessar o índice correto na lista
    mensagem = mensagens_alerta[nivel - 1]
    cor = definir_cor(nivel)
    
    # Imprime a cor, o texto e garante que o terminal volte ao normal (Style.RESET_ALL)
    print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")

# --- Simulação de Monitoramento ---
def simular_monitoramento():
    print("Iniciando o sistema de monitoramento do reservatório...\n")
    
    # Simula a leitura dos 5 níveis sequencialmente
    for nivel_atual in range(1, 6):
        exibir_status_reservatorio(nivel_atual)
        time.sleep(1) # Pausa de 1 segundo entre as leituras para simular o sistema trabalhando
        
    print("\nMonitoramento concluído.")

if __name__ == "__main__":
    simular_monitoramento()
