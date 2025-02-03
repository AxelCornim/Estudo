def analisar_pintura(pintura):
    # Verifica a presença de assinatura
    if "assinatura" in pintura.lower():
        return "Provavelmente obra humana (assinatura presente)."
    
    # Verifica estilo e técnica
    estilo = input("Informe o estilo da pintura (Renascimento, Impressionismo, etc.): ")
    if estilo.lower() in ["renascimento", "impressionismo", "cubismo"]:
        return "Provavelmente obra humana (estilo consistente)."
    
    # Análise visual (simplificada)
    # Aqui você pode adicionar mais critérios específicos
    if "pinceladas" in pintura.lower() or "texturas" in pintura.lower():
        return "Provavelmente obra humana (detalhes visuais)."
    
    # Se não encontrou evidências claras, assume que é IA
    return "Possivelmente obra de IA."

# Exemplo de uso
pintura_usuario = input("Insira uma descrição da pintura: ")
resultado = analisar_pintura(pintura_usuario)
print(resultado)
