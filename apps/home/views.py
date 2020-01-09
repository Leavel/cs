from apps.home import home


@home.route('/')
def index():
    return 'home index'

