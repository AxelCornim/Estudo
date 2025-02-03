import pyautogui
import time

def main():
    print("=== Sistema de Repetição de Texto ===")

    # Etapa 1: Usuário insere o texto
    text = input("Digite o texto que deseja enviar: ")
    
    # Etapa 2: Escolher o número de repetições
    repetitions = int(input("Quantas vezes deseja repetir o texto?: "))
    
    # Etapa 3: Aguardar clique do usuário
    input("Posicione o cursor no local onde deseja enviar a mensagem e pressione ENTER...")
    x, y = pyautogui.position()
    print(f"Clique detectado na posição: ({x}, {y})")

    # Etapa 4: Confirmar envio
    confirm_chat = input("Deseja continuar e enviar a mensagem para o local clicado? (s/n): ").strip().lower()
    if confirm_chat != 's':
        print("Operação cancelada.")
        return

    print("Enviando mensagem...")
    for i in range(repetitions):
        pyautogui.click(x, y)
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        print(f"[{i + 1}] Mensagem enviada")
    print("Envio concluído!")

if __name__ == "__main__":
    main()
