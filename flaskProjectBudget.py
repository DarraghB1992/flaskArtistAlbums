from flask import Flask, render_template

app = Flask(__name__)

artists = [{
    'id': 1,
    'name': 'Gandolf',
    'genre': 'Wizard pop',
},
    {
        'id': 2,
        'name': 'Barry Trotter',
        'genre': 'Reggae',
    },
    {
        'id': 3,
        'name': 'Boyzone',
        'genre': 'Awful',
    }
]

albums = [{
    'id': 1,
    'artists': 1,
    'title': 'The Lonely Shire',

},
    {
        'id': 2,
        'artists': 1,
        'title': 'Its a long way to Mt.Doom',

    },
    {
        'id': 3,
        'artists': 2,
        'title': 'Reggae reggae sauce',

    },
    {
        'id': 4,
        'artists': 3,
        'title': 'Greatest hits',

    }
]


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/albums')
def get_albums():
    return render_template("albums.html", albums=albums)


@app.route('/artists')
def get_artists():
    return render_template("artists.html", artists=artists)


@app.route('/artists/<id>')
def get_artist_details(id):
    return render_template('artist_details.html', artist=artists[int(id) - 1])


if __name__ == '__main__':
    app.run()
