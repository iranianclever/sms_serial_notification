from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    '''main function for start'''
    return 'Hello, World!'
