from flask import Flask
from get_links import get_links_file

app = Flask(__name__)
app.register_blueprint(get_links_file, url_prefix="")

@app.route('/2')
def index():
    return "<h1>hello</h1>"
    

if __name__ == '__main__':
    app.run(debug=True) 