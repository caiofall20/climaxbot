import os
from flask import Flask, request
token = os.environ.get('FB_ACCESS_TOKEN')
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def webhook():
    return 'Nothing'
if __name__ == '__main__':
    app.run(debug=True)
