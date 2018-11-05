class AuthenticateViews:
    def authenticate_product(self,name, qty, min_stock, price, units, category):
        
        if not name or not isinstance(name, str):
            return "product name missing or must be a string."
        if name.isspace() or not name.isalpha():
            return "product name should only be letters"
        if not qty or not isinstance(qty, int):
            return "product quantity missing or must be a number."
        if not min_stock or not isinstance(min_stock, int):
            return "product min_stock missing or must be a number."
        if not price or not isinstance(price, int):
            return "product price missing or must be a number."
        if not units or not isinstance(units, int):
            return "product units missing or must be a number."
        if not category or not isinstance(category, str):
            return "product category missing or must be a string."