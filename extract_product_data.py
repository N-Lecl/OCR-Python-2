import csv
import requests
from bs4 import BeautifulSoup


def extract_product_info(product_url):
    # Envoyer une requête GET pour obtenir la page HTML
    response = requests.get(product_url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraire les informations nécessaires
        product_info = {}
        
        # URL de la page produit
        product_info['product_page_url'] = product_url
        
        # Universal Product Code (UPC)
        product_info['universal_product_code'] = soup.find('th', text='UPC').find_next('td').text
        
        # Titre du produit
        product_info['title'] = soup.find('h1').text
        
        # Prix TTC
        product_info['price_including_tax'] = soup.find('th', text='Price (incl. tax)').find_next('td').text
        
        # Prix HT
        product_info['price_excluding_tax'] = soup.find('th', text='Price (excl. tax)').find_next('td').text
        
        # Quantité disponible
        product_info['number_available'] = soup.find('th', text='Availability').find_next('td').text
        
        # Description du produit
        product_info['product_description'] = soup.find('meta', attrs={'name': 'description'})['content']
        
        # Catégorie du produit
        product_info['category'] = soup.find('ul', class_='breadcrumb').find_all('li')[-2].text.strip()
        
        # Note de l'évaluation
        product_info['review_rating'] = soup.find('p', class_='star-rating')['class'][1]
        
        # URL de l'image
        product_info['image_url'] = soup.find('img')['src']
        
        return product_info
    else:
        print(f"Échec extract_product_info. Code d'erreur : {response.status_code}")
        return None


def write_product_info_to_csv(product_info, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Écrire l'en-tête du fichier CSV
        header = product_info[0].keys()  # Utilisez les clés du premier dictionnaire comme en-tête
        writer.writerow(header)
        
        # Écrire les données de chaque produit
        for info in product_info:
            data = info.values()
            writer.writerow(data)


    
def extract_product_links_by_category(base_url, category):
    category_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    response = requests.get(category_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_links = []
        
        # Trouver tous les liens des pages produits dans la catégorie
        product_elements = soup.find_all('h3')
        for element in product_elements:
            href = element.a['href']
            cleaned_href = href.replace('../../../', '')
            product_links.append(f"{base_url}{cleaned_href}")
        
        print(product_links)
        return product_links
    
    else:
        print(f"Échec extract_product_links_by_category. Code d'erreur : {response.status_code}")
        return None