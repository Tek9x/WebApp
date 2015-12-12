from flask import Flask, render_template , request
import requests
app = Flask(__name__)

@app.route("/")
def main():
     return render_template('index.html')

@app.route("/seasons/1")
def seasons():
     return render_template('seasons.html')


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)