from storeapp import myapp

@myapp.route('/')
@myapp.route('/index')
def index():
    return "we win"