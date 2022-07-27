import requests

def fetch_albums()->list[dict]:
    resp = requests.get('https://itunes.apple.com/us/rss/topalbums/limit=100/json')
    albums = _parse_json_reponse(resp.json())
    return albums

def _parse_json_reponse(json: dict)->list[dict]:
    albums = []
    entries = json['feed']['entry']
    for index, entry in enumerate(entries, 1):
        album_info = {
            'index' : index,
            'albumName': entry['im:name']['label'], 
            'albumLink': entry['link']['attributes']['href'],
            'artistName': entry['im:artist']['label'],
            'artistLink': "entry['im:artist']['attributes']['href']",
            'imgSrcSmall': entry['im:image'][1]['label'],
            'imgSrcLarge' : entry['im:image'][2]['label'],
            'price' : entry['im:price']['label'],
            'category' : entry['category']['attributes']['label'],
            'releaseDate' : entry['im:releaseDate']['attributes']['label'],
            'favorited': False,
        }
        albums.append(album_info)
    return albums
    

fetch_albums()

