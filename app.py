from flask import Flask, render_template, request
import requests
from Episodes import *

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/tabletest")
def table():
    return render_template('tabletest.html', dict=Season3)


@app.route("/seasons/<season>")
def seasons(season):
    if season == '1':
        return render_template('seasons.html', dict=Season1)
    elif season == '2':
        return render_template('seasons.html', dict=Season2)
    elif season == '3':
        return render_template('seasons.html', dict=Season3)
    elif season == '4':
        return render_template('seasons.html', dict=Season4)
    elif season == '5':
        return render_template('seasons.html', dict=Season5)
    elif season == '6':
        return render_template('seasons.html', dict=Season6)
    elif season == '7':
        return render_template('seasons.html', dict=Season7)


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
