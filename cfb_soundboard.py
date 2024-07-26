from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Directory where your sound files are stored
SOUND_DIRECTORY = 'static/sounds'

@app.route('/')
def index():
    # Get all MP3 files from the sound directory
    sound_files = [f for f in os.listdir(SOUND_DIRECTORY) if f.endswith('.mp3')]
    return render_template('index.html', sound_files=sound_files)

@app.route('/play/<filename>')
def play_sound(filename):
    return send_from_directory(SOUND_DIRECTORY, filename)

if __name__ == '__main__':
    app.run("0.0.0.0", 5013, debug=True)