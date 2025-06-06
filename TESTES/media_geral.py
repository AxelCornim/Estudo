import pytesseract
from PIL import Image
import re

# --- Função para extrair texto da imagem ---
def extrair_texto(imagem_path):
    imagem = Image.open(imagem_path)
    texto = pytesseract.image_to_string(imagem, lang='por')
    return texto

# --- Função para encontrar valores financeiros ---
def extrair_valores(texto):
    padroes = {
        'patrimonio': r'PATRIM[\w\s]+?R\$ ([\d\.]+,\d+)',
        'divida_bruta': r'D[IÍ]VIDA BRUTA\s+R\$ ([\d\.]+,\d+)',
        'valor_mercado': r'VALOR DE MERCADO\s+R\$ ([\d\.]+,\d+)',
        'lucro_liquido': r'LUCRO L[\w\s]+?R\$ ([\d\.]+,\d+)',
        'ativos': r'ATIVOS\s+R\$ ([\d\.]+,\d+)',
        'divida_liquida': r'D[IÍ]VIDA L[\w\s]+?R\$ ([\d\.]+,\d+)',
        'numero_acoes': r'N\u00ba TOTAL DE PAP[\w\s]+?([\d\.]+)',
        'disponibilidade': r'DISPONIBILIDADE\s+R\$ ([\d\.]+,\d+)',
    }

    dados = {}
    for chave, padrao in padroes.items():
        resultado = re.search(padrao, texto)
        if resultado:
            dados[chave] = float(resultado.group(1).replace('.', '').replace(',', '.'))
        else:
            dados[chave] = None

    return dados

# --- Função para calcular indicadores ---
def calcular_indicadores(dados):
    indicadores = {}

    try:
        # VPA
        indicadores['VPA'] = dados['patrimonio'] / dados['numero_acoes']

        # Preço da ação
        preco_acao = dados['valor_mercado'] / dados['numero_acoes']

        # P/L (se lucro informado)
        if dados['lucro_liquido']:
            indicadores['P/L'] = preco_acao / (dados['lucro_liquido'] / dados['numero_acoes'])

        # ROE
        if dados['lucro_liquido']:
            indicadores['ROE'] = dados['lucro_liquido'] / dados['patrimonio']

        # ROA
        if dados['lucro_liquido'] and dados['ativos']:
            indicadores['ROA'] = dados['lucro_liquido'] / dados['ativos']

        # LP (Patrimônio / Total de ativos)
        if dados['ativos']:
            indicadores['LP'] = dados['patrimonio'] / dados['ativos']

    except Exception as e:
        print("Erro ao calcular indicadores:", e)

    return indicadores

# --- Uso ---
# texto_extraido = extrair_texto("caminho/da/imagem.png")
# dados_financeiros = extrair_valores(texto_extraido)
# indicadores = calcular_indicadores(dados_financeiros)

# for chave, valor in indicadores.items():
#     print(f"{chave}: {valor:.2f}")
