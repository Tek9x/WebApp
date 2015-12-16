import json

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/seasons/<season>")
def seasons(season):
    if season == '1':
        with open('static/data/Season_1.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '2':
        with open('static/data/Season_2.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '3':
        with open('static/data/Season_3.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '4':
        with open('static/data/Season_4.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '5':
        with open('static/data/Season_5.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '6':
        with open('static/data/Season_6.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '7':
        with open('static/data/Season_7.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '8':
        with open('static/data/Season_8.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '9':
        with open('static/data/Season_9.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '10':
        with open('static/data/Season_10.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])


@app.route("/playback")
def playback():
    url = request.args['url']
    if 'cdn.php?ref=' in url:
        print url
        return render_template('video.html', url=url)
    else:
        return render_template('video.html', url='')


@app.route('/video_download')
def user_download():
    url = request.args['url']  # user provides url in query string
    r = requests.get(url)

    # write to a file in the app's instance folder
    # come up with a better file name
    with app.open_instance_resource('downloaded_file', 'wb') as f:
        f.write(r.content)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
