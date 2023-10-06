from extract_product_data import extract_product_info, extract_product_links_by_category, get_category_urls, write_product_info_to_csv


if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/"
    base_category_url = "http://books.toscrape.com/index.html"
    
    
    # Demandez à l'utilisateur de choisir une catégorie
    category = input("Entrez le nom du fichier CSV que vous souhaitez créer : ")
    
    # Obtenez les liens des pages produits pour la catégorie choisie
    product_links = extract_product_links_by_category(base_url, category)

    
    if product_links:
        csv_filename = f"{category}_products.csv"
        
        # Créez une liste pour stocker les informations de chaque produit
        product_info_list = []
        
        # Parcourez tous les liens des pages produits
        for product_url in product_links:
            product_info = extract_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
        
            # Utilisez la fonction write_product_info_to_csv pour écrire les données dans le fichier CSV
            for product_info in product_info_list:
                write_product_info_to_csv(product_info_list, csv_filename)   
                print(f"Données enregistrées dans {csv_filename}")
                
        # Utilisez la fonction get_category_urls pour obtenir les URLs des catégories
        category_urls = get_category_urls(base_category_url)
        print(category_urls)