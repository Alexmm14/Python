import requests
import json

def get_first_contentful_paint(url, api_key):
    # Construir la URL de la API de PageSpeed Insights
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}"

    # Realizar la solicitud a la API
    response = requests.get(api_url)
    data = response.json()

    # Obtener el valor de FIRST_CONTENTFUL_PAINT_MS
    try:
        fcp_value = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]
        fcp_value_s = fcp_value / 1000
        return fcp_value_s
    except KeyError:
        print("------------------")
        print("La clave FIRST_CONTENTFUL_PAINT_MS no se encuentra en la respuesta.")
        print("------------------")
        return None

def print_first_contentful_paint(url, api_key):
    fcp_value = get_first_contentful_paint(url, api_key)

    if fcp_value is not None:
        print("********************")
        print(f"First Contentful Paint (FCP): {fcp_value} segundos")
        print("********************")

def get_technology_info_formatted(url, api_key):
    api_url = 'https://whatcms.org/API/Tech'
    params = {'key': api_key, 'url': url}

    response = requests.get(api_url, params=params)
    tech_info_raw = response.text

    print("Entre en la funcion")
    try:
        hostname_json = json.loads(tech_info_raw)
        for result in hostname_json["results"]:
            nombre = result["name"]
            version = result["version"] if "version" in result else "N/A"
            categorias = result["categories"] if "categories" in result else ["N/A"]

            print("********************")
            print(f"Nombre: {nombre}")
            print(f"Version: {version}")
            print("Categorias:")
            
            for categoria in categorias:
                print(f" - {categoria}")
                print("-" * 20)

    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        print("\nRespuesta JSON (en bruto):")
        print("------------------")
        print(tech_info_raw)

def getHostsThisSite(url, api_key):
    api_url = 'https://www.who-hosts-this.com/API/Host'
    params = {'key': api_key, 'url': url}

    response = requests.get(api_url, params=params)
    tech_info_raw = response.text

    try:
        hostname_json = json.loads(tech_info_raw)
        for result in hostname_json["results"]:
            nombre = result["isp_name"]

            print("********************")
            print(f"Nombre: {nombre}")
            print("********************")

    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        print("\nRespuesta JSON (en bruto):")
        print("------------------")
        print(tech_info_raw)

if __name__ == "__main__":
    # URL que deseas analizar
    url = input("Ingresa la URL que deseas analizar: ")

    # Clave de API de PageSpeed Insights
    api_key_psi = "AIzaSyAL67F5ZAG1eCWeoG5hAOwf2CYO_EfumAE"

    # Clave de API de WhatCMS
    api_key_whatcms = "wm7tcnsm0tnautuld4kavikzryopxnesezlda3eim14ved490bfejc6s7xds5mkfk5bseo"

    # Obtener información de tecnología a través de la API en formato JSON formateado
    get_technology_info_formatted(url, api_key_whatcms)
    
    
    # Imprimir el valor de FIRST_CONTENTFUL_PAINT_MS
    print_first_contentful_paint(url, api_key_psi)

    getHostsThisSite(url, api_key_whatcms)

