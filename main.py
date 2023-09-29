import csv
from extract_product_data import extract_product_info, extract_product_links_by_category, write_product_info_to_csv


# if __name__ == "__main__":
#     product_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
#     product_info = extract_product_info(product_url)
    
#     if product_info:
#         # Nom du fichier CSV dans lequel vous souhaitez enregistrer les données
#         csv_filename = f"{product_info['title']}.csv"
        
#         # Appel de la fonction pour écrire les données dans le fichier CSV
#         write_product_info_to_csv(product_info, csv_filename)
        
#         print(f"Données enregistrées dans {csv_filename}")

# -------------------------------------------------------------------------------

if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/category"
    
    # Demandez à l'utilisateur de choisir une catégorie
    category = input("Entrez le nom de la catégorie que vous souhaitez parcourir : ")
    
    # Obtenez les liens des pages produits pour la catégorie choisie
    product_links = extract_product_links_by_category(base_url, category)
    
    if product_links:
        csv_filename = f"{category}_products.csv"
        
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Écrire l'en-tête du fichier CSV
            header = [
                'product_page_url', 'universal_product_code', 'title',
                'price_including_tax', 'price_excluding_tax',
                'number_available', 'product_description',
                'category', 'review_rating', 'image_url'
            ]
            writer.writerow(header)
            
            # Parcourez tous les liens des pages produits
            for product_url in product_links:
                product_info = extract_product_info(product_url)
                if product_info:
                    # Écrire les données du produit dans le fichier CSV
                    data = list(product_info.values())
                    writer.writerow(data)
        
        print(f"Données enregistrées dans {csv_filename}")

