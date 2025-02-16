def calcular_salario():
    # Informações básicas
    salario_base = 1940.00
    horas_mensais = 220  # Jornada mensal considerando escala 6x1
    
    # Solicita informações ao usuário
    horas_trabalhadas = float(input("Quantas horas foram trabalhadas? "))
    horas_extras = float(input("Quantas horas extras foram feitas no total? "))
    bonus_extra = float(input("Informe o valor de bônus extra (se houver): "))
    
    # Cálculo do salário proporcional
    salario_proporcional = salario_base * (horas_trabalhadas / horas_mensais)
    
    # Cálculo da quebra de caixa (25%)
    quebra_de_caixa = salario_proporcional * 0.25
    
    # Cálculo das horas extras
    valor_hora = salario_base / horas_mensais
    valor_hora_extra = valor_hora * 1.5  # 50%
    total_horas_extras = horas_extras * valor_hora_extra
    
    # Cálculo do DSR sobre horas extras
    dsr_horas_extras = total_horas_extras / 6
    
    # Cálculo do salário bruto
    salario_bruto = salario_proporcional + quebra_de_caixa + total_horas_extras + dsr_horas_extras + bonus_extra
    
    # Cálculo do INSS
    if salario_bruto <= 1412.00:
        inss = salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        inss = (1412.00 * 0.075) + ((salario_bruto - 1412.00) * 0.09)
    elif salario_bruto <= 4000.03:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario_bruto - 2666.68) * 0.12)
    else:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario_bruto - 4000.03) * 0.14)
    
    # Base do IRRF
    base_irrf = salario_bruto - inss
    
    # Cálculo do IRRF
    if base_irrf <= 2112.00:
        irrf = 0
    elif base_irrf <= 2826.65:
        irrf = (base_irrf * 0.075) - 158.40
    elif base_irrf <= 3751.05:
        irrf = (base_irrf * 0.15) - 370.40
    elif base_irrf <= 4664.68:
        irrf = (base_irrf * 0.225) - 651.73
    else:
        irrf = (base_irrf * 0.275) - 884.96
    
    # Salário líquido
    salario_liquido = salario_bruto - inss - irrf
    
    # Exibe os resultados
    print("\n========= RESUMO DO SALÁRIO =========")
    print(f"Salário Base Proporcional: R$ {salario_proporcional:.2f}")
    print(f"Quebra de Caixa (25%): R$ {quebra_de_caixa:.2f}")
    print(f"Horas Extras: R$ {total_horas_extras:.2f}")
    print(f"DSR sobre Horas Extras: R$ {dsr_horas_extras:.2f}")
    print(f"Bônus Extra: R$ {bonus_extra:.2f}")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print("====================================")

# Executa o programa
calcular_salario()
