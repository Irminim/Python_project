from flask import Flask

app = Flask(__name__)


@app.route('/HipHop')
def Music():
    songName = 'Take me to the Moon'
    return songName


if __name__ == "__main__":
    app.run(debug=True)
