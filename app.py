from flask import Flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    jogos = [
        {
    'Playstation': ['Castlevania', 'Final Fantasy Tactics'],
    'SNES': ['Super Metroid', 'Super Mario World'],
    'Saturn': ['Nights', 'Guardian Heroes'],
    'Xbox': ['Halo', 'Gears of War'],
}
    ]
    return (jogos)
if __name__ == "__main__":
    app.run()
    