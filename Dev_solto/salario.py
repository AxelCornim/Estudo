def calcular_salario():
    # Informações básicas
    salario_base = 1940.00
    horas_mensais = 220  # Jornada mensal considerando escala 6x1

    # Solicita informações ao usuário
    horas_trabalhadas = float(input("Quantas horas normais foram trabalhadas? "))
    horas_extras_50 = float(input("Quantas horas extras 50% foram feitas? "))
    horas_extras_100 = float(input("Quantas horas extras 100% foram feitas? "))
    horas_faltas = float(input("Quantas horas de faltas? "))
    horas_afastamento = float(input("Quantas horas de afastamento? "))
    bonus_extra = float(input("Informe o valor de bônus extra (se houver): "))

    # Cálculo do salário proporcional
    salario_proporcional = salario_base * ((horas_trabalhadas + horas_afastamento) / horas_mensais)

    # Cálculo das horas extras
    valor_hora = salario_base / horas_mensais
    valor_hora_extra_50 = valor_hora * 1.5
    valor_hora_extra_100 = valor_hora * 2.0
    total_horas_extras = (horas_extras_50 * valor_hora_extra_50) + (horas_extras_100 * valor_hora_extra_100)

    # Cálculo do DSR sobre horas extras
    dsr_horas_extras = total_horas_extras / 6

    # Cálculo do salário bruto
    salario_bruto = salario_proporcional + total_horas_extras + dsr_horas_extras + bonus_extra

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
    print(f"Horas Extras 50%: R$ {horas_extras_50 * valor_hora_extra_50:.2f}")
    print(f"Horas Extras 100%: R$ {horas_extras_100 * valor_hora_extra_100:.2f}")
    print(f"DSR sobre Horas Extras: R$ {dsr_horas_extras:.2f}")
    print(f"Bônus Extra: R$ {bonus_extra:.2f}")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print("====================================")

# Executa o programa
calcular_salario()
