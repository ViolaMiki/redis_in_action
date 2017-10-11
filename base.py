import os

class Base():
    flask_dir = ''
    def __init__(self):
        self.flask_dir = os.path.dirname(os.path.abspath(__file__))

base = Base()