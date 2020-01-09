from apps.front import front


@front.route('/')
def index():
    return 'front index'