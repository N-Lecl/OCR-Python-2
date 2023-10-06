def books_urls_from_category(cat_url):
    si pas de bouton next
        	return [livres de la page]
    
    si bouton next
        url+_page suivante
        return [ livres de la page ] + books_urls_from_category(lien de la page suivante)