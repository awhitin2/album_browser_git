from flask import Flask, jsonify
from flask_cors import CORS

import album_data


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})

# albums= {
#     'albums':
#     [
#         { 
#             'albumName': 'Album 1', 
#             'artistName': 'Artist 1',
#             'favorited': True,
#             'imgSrc': 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',

#         },
#         { 
#             'albumName': 'Album 2', 
#             'artistName': 'Artist 2',
#             'favorited': False,
#             'imgSrc': 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',
#         },
#         { 
#             'albumName': 'Album 3', 
#             'artistName': 'Artist 3',
#             'favorited': False,
#             'imgSrc': 'https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/9a/37/93/9a379323-ac8e-766d-0dec-f19d95a54766/810074421287.jpg/60x60bb.png',
#         },
#     ]       
# }

@app.route('/', methods=['GET'])
def greetings():
    return('Hello, world!')

@app.route('/albums', methods=['GET'])
def get_albums():
    albums = album_data.fetch_albums()
    return({'albums': albums})



if __name__ == "__main__":
    app.run(debug=True)


'''
sudo lsof -i:5000
'''