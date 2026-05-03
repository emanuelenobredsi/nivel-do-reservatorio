from colorama import Fore, Style, init

init(autoreset=True)

niveis_reservatorio = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
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
        return Fore.WHITE

def exibir_status():
    print("Monitoramento do Reservatório:\n")
    
    for i in range(len(niveis_reservatorio)):
        nivel = i + 1
        cor = definir_cor(nivel)
        mensagem = niveis_reservatorio[i]
        
        print(cor + mensagem + Style.RESET_ALL)

exibir_status()