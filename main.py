from extract_product_data import extract_product_info, extract_product_links_by_category, get_category_names, write_product_info_to_csv
import datetime


if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/"
    base_category_url = "http://books.toscrape.com/index.html"
    
    # Obtenez la liste des noms de catégories
    category_names = get_category_names(base_category_url)
    
    if category_names:
        # Demandez à l'utilisateur de choisir une catégorie parmi la liste
        print("Choisissez une catégorie parmi les suivantes :")
        for i, category in enumerate(category_names, start=1):
            print(f"{i}. {category}")
        
        choice = int(input("Entrez le numéro de la catégorie que vous souhaitez : "))
        selected_category = category_names[choice - 1]
        
        # Générez un nom de fichier basé sur la catégorie et l'horodatage
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        csv_filename = f"{selected_category}_{timestamp}.csv"
        
        # Obtenez les liens des pages produits pour la catégorie choisie
        product_links = extract_product_links_by_category(base_url, selected_category)
        
        # Créez une liste pour stocker les informations de chaque produit
        product_info_list = []
        
        # Parcourez tous les liens des pages produits
        for product_url in product_links:
            product_info = extract_product_info(product_url)
            if product_info:
                product_info_list.append(product_info)
        
        # Utilisez la fonction write_product_info_to_csv pour écrire les données dans le fichier CSV
        if product_info_list:
            write_product_info_to_csv(product_info_list, csv_filename)
            print(f"Données enregistrées dans {csv_filename}")
                
