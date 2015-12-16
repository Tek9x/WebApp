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
    elif season == '11':
        with open('static/data/Season_11.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '12':
        with open('static/data/Season_12.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '13':
        with open('static/data/Season_13.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '14':
        with open('static/data/Season_14.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '15':
        with open('static/data/Season_15.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '16':
        with open('static/data/Season_16.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '17':
        with open('static/data/Season_17.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '18':
        with open('static/data/Season_18.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '19':
        with open('static/data/Season_19.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '20':
        with open('static/data/Season_20.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '21':
        with open('static/data/Season_21.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '22':
        with open('static/data/Season_22.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '23':
        with open('static/data/Season_23.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '24':
        with open('static/data/Season_24.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '25':
        with open('static/data/Season_25.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '26':
        with open('static/data/Season_26.json') as f:
           db = json.load(f)
        return render_template('seasons.html', dict=db['Episodes'])
    elif season == '27':
        with open('static/data/Season_27.json') as f:
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
