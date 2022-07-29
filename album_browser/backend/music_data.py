import requests
import bs4

def fetch_albums()->list[dict]:
    """Fetch the top 100 albums"""

    resp = requests.get(
        'https://itunes.apple.com/us/rss/topalbums/limit=100/json')

    albums = _parse_albums_reponse(resp.json())
    return albums

def _parse_albums_reponse(json: dict)->list[dict]:
    """Extract relevant info from response object"""

    albums = []
    entries = json['feed']['entry']
    for index, entry in enumerate(entries, 1):
        album_info = {
            'index' : index,
            'albumName': entry['im:name']['label'], 
            'albumLink': entry['link']['attributes']['href'],
            'albumId' : entry['id']['attributes']['im:id'],
            'artistName': entry['im:artist']['label'],
            'imgSrcSmall': entry['im:image'][1]['label'],
            'imgSrcLarge' : entry['im:image'][2]['label'],
            'price' : entry['im:price']['label'],
            'category' : entry['category']['attributes']['label'],
            'releaseDate' : entry['im:releaseDate']['attributes']['label'],
            'favorited': False,
        }
        try:
            album_info['artistLink'] = entry['im:artist']['attributes']['href']
        except KeyError:
            album_info['artistLink'] = ''

        albums.append(album_info)
    return albums
    
fetch_albums()

def fetch_songs(url: str = 'https://music.apple.com/us/album/entering-heaven-alive/1624743251?uo=2')->list[dict]:
    """Fetch all songs and their durations for a given album"""
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    songs = _parse_songs_reponse(soup)
    return songs


def _parse_songs_reponse(soup: bs4.BeautifulSoup)->list[dict]:
    """Extract the relevant song info from the bs4 soup object"""

    song_names = [item.text for item in soup.select(
        '.songs-list-row__song-name')]

    song_lengths = [item.text.strip() for item in soup.select(
        '.songs-list-row__length')]

    song_info = []
    for index, (name, length) in enumerate(zip(song_names, song_lengths),1):
        info_dict = {
            'index' : index,
            'songName' : name,
            'duration' : length,
        }
        song_info.append(info_dict)

    return song_info