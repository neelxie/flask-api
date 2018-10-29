class AuthenticateViews:
    def authenticate_product(self,name, qty, min_stock, price, units, category):
        
        if not name:
            return "product name missing."
        if  not isinstance(name, str):
            return "product name must be a string."
        if name.isspace():
            return "product name is missing"
        if not qty:
            return "product quantity missing."
        if  not isinstance(qty, int):
            return "product quantity must be a number."
        if not min_stock:
            return "product min_stock missing."
        if  not isinstance(min_stock, int):
            return "product min_stock must be a number."
        if not price:
            return "product price missing."
        if  not isinstance(price, int):
            return "product price must be a number."
        if not units:
            return "product units missing."
        if  not isinstance(units, int):
            return "product units must be a number."
        if not category:
            return "product category missing."
        if  not isinstance(category, str):
            return "product category must be a string."        