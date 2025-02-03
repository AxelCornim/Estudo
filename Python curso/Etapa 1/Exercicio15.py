import os
os.system("cls")

Dias = float(input("\033[36mQualtos dias alugou veiculo?\033[m "))
Km = float(input("\033[36mQualtos Km rodados com veiculo?\033[m "))
Tot = (Dias * 60) + (Km * 0.15)
print('\033[3m\033[1;35m-=-\033[m\033[m' *15)
print(f"\033[36mO total a pagar e \033[4;36mR${Tot:.2f}reais.\033[m") 