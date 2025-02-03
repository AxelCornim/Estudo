import requests
from bs4 import BeautifulSoup
import json
import os

# Define a consulta de pesquisa
search_query = "agencia de modelo em criciuma instagram"

# Define a localização (Criciúma, Santa Catarina, Brasil)
location = "Criciuma, Santa Catarina, Brazil"

# Define o raio de pesquisa (80 km)
search_radius = 80

# Define o número máximo de resultados
max_results = 40

# Inicializa a lista para armazenar os resultados
results = []

# Realiza a pesquisa
url = f"https://www.google.com/search?q={search_query} {location}&num={max_results}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extrai os resultados da pesquisa
for result in soup.find_all("div", class_="tF2Cxc"):
    title = result.find("h3").text
    link = result.find("a")["href"]
    snippet = result.find("span", class_="aCOpRe").text
    results.append({"title": title, "link": link, "snippet": snippet})

# Salva os resultados em um arquivo de texto
output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "1")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "agencia_modelo_results.txt")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Resultados da pesquisa salvos em {output_file}")
