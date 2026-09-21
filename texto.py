import requests
from bs4 import BeautifulSoup
import pandas as pd
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
paises = texto.find_all("div", class_="col-md-4 country")


# 4. Iterar sobre cada tarjeta de país para extraer los datos
for pais in paises:
   # Extraer el nombre del país
   nombre_pais = pais.find("h3", class_="country-name").text.strip()

   # Extraer la capital
   capital = pais.find("span", class_="country-capital").text.strip()

   # Extraer la población
   poblacion = pais.find("span", class_="country-population").text.strip()

   # Extraer el área
   area = pais.find("span", class_="country-area").text.strip()

   datos.append({
       "Pais": nombre_pais,
       "Capital": capital,
       "Poblacion": poblacion,
       "Area_km2": area
   })


# 5. Convertir la lista de diccionarios a un DataFrame (Estructura Tidy Data)
df = pd.DataFrame(datos)
df.to_csv("paises_info.csv", index=False)
print("Scraping exitoso y archivo paises_info.csv creado.")
"""


with open("texto.py", "w", encoding="utf-8") as f:
f.write(script_code)
