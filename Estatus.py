import requests

def check_page_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"La pagina {url} esta disponible (200 OK).")
        else:
            print(f"La pagina {url} respondio con codigo {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"No se pudo conectar a {url}: {e}")

def check_resource_status(url, resource):
    try:
        response = requests.get(url + resource)
        if response.status_code == 200:
            print(f"Recurso {resource} cargado correctamente.")
        else:
            print(f"Error al cargar el recurso {resource}: Codigo {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al cargar el recurso {resource}: {e}")

if __name__ == "__main__":
    # URL base de mi aplicacion web
    url_base = "http://127.0.0.1:8081" 

    # Verificar la pagina principal
    check_page_status(url_base)

    # Verificar recursos clave (CSS, imagenes)
    recursos = [
        "/style.css", 
        "/Imagenes/PortadaPagina.jpeg",
        "/Imagenes/TopersAzules.png",
        "/script.js"
    ]
    
    for recurso in recursos:
        check_resource_status(url_base, recurso)
