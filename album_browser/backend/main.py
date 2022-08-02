from flask import Flask, request
from flask_cors import CORS

import music_data


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})


@app.route('/albums', methods=['GET'])
def get_albums():
    albums = music_data.fetch_albums()
    return({'albums': albums})


@app.route('/songs', methods=['GET'])
def get_songs():
    args = request.args
    songs = music_data.fetch_songs(args['link'])
    return({'songs': songs})



if __name__ == "__main__":
    app.run(debug=True)
