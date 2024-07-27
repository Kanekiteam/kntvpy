import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# URL de la página de programación
url = 'https://programaciontv.cine.com/hbo-family/hoy'

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Crear el archivo XMLTV
tv = ET.Element('tv', version="1.0", xmlns="urn:xmltv:namespace")

# Ejemplo de datos del canal
channel = ET.SubElement(tv, 'channel', id='hbo-family')
ET.SubElement(channel, 'display-name', lang='es').text = 'HBO FAMILY'

# Buscar la información de los programas
programs = soup.find_all('div', class_='program-card')  # Ajusta según la estructura real de la web

for program in programs:
    title = program.find('h2').text.strip()  # Ajusta según la estructura real de la web
    description = program.find('p', class_='description').text.strip()  # Ajusta según la estructura real de la web
    
    # Extraer horario y convertirlo (ejemplo simple, ajustar según el formato real)
    start_time = datetime.now()  # Deberás ajustar esto según la hora de inicio real
    end_time = start_time + timedelta(hours=1)  # Ajustar duración del programa

    programme = ET.SubElement(tv, 'programme', start=start_time.strftime('%Y%m%d%H%M%S +0000'), stop=end_time.strftime('%Y%m%d%H%M%S +0000'), channel='hbo-family')
    ET.SubElement(programme, 'title', lang='es').text = title
    ET.SubElement(programme, 'desc', lang='es').text = description

# Guardar el archivo XMLTV
tree = ET.ElementTree(tv)
with open('epg.xml', 'wb') as fh:
    tree.write(fh, encoding='utf-8', xml_declaration=True)
