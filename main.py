import os
from extract_product_data import download_and_save_image, extract_product_info, extract_product_links_by_category, get_category_names, write_product_info_to_csv


if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/"
    base_category_url = "http://books.toscrape.com/index.html"
    
    category_names = get_category_names(base_category_url)
    
    if category_names:
        for selected_category in category_names:
            # Retirez le numéro du nom de la catégorie
            category_name_cleaned = selected_category.split('_')[0]
            category_dir = f"data/{category_name_cleaned}"
            
            product_links = extract_product_links_by_category(base_url, selected_category)
            
            # Vérifiez si product_links est vide avant de créer le dossier
            if product_links is not None and len(product_links) > 0:
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                
                # Retirez également le suffixe du nom de fichier CSV
                csv_filename = f"{category_name_cleaned}.csv"
                csv_path = os.path.join(category_dir, csv_filename)
                
                product_info_list = []
                
                for product_url in product_links:
                    product_info = extract_product_info(product_url)
                    if product_info:
                        image_url = product_info.get('image_url', '')
                        alt_text = product_info.get('title', '')
                        
                        if image_url:
                            download_and_save_image(image_url, category_dir, alt_text)
                        
                        product_info_list.append(product_info)
                
                if product_info_list:
                    write_product_info_to_csv(product_info_list, csv_path)
                    print(f"Données enregistrées dans {csv_path}")
    print("Terminé !")