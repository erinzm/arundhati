import re
from flask import render_template
from . import app

LIPSUM = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

def wordify(data):
    texts = data.split()
    desymbolify = re.compile('[^a-zA-Z]')
    words = [desymbolify.sub('', t).lower() for t in texts]

    return list(zip(texts, words))

LIPSUM_WORDS = wordify(LIPSUM)

@app.route('/query/<appid>/<arm>')
def test(appid, arm):
    return render_template('display_query.html', words=LIPSUM_WORDS)

@app.route('/choose/<appid>')
def choose_initial(appid):
    return render_template('select_initial.html')
