from myapp.api import bp
def Users():
    users = [
        {
            'username': 'admin',
            'name': 'Derrick',
            'password': 'dfdgsas'
        },
        {
            'username': 'neelxie',
            'name': 'Derek',
            'password': 'vbvbsas'
        },
        {
            'username': 'matama',
            'name': 'Viola',
            'password': 'prwtuasfs'
        }
    ]
    return users

@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users/<int:id>', methods=['GET'])
def get_one_user(id):
    pass

@bp.route('/users/<int:id>/sales', methods=['GET'])
def get_user_sales(id):
    pass

@bp.route('/users/<int:id>/sales/<int:id>', methods=['GET'])
def get_one_sale_of_user(id):
    pass