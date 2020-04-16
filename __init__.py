import json
import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    projects_filename = os.path.join(app.static_folder, 'projects.json')
    with open(projects_filename) as projects_json:
        projects = json.load(projects_json)
    languages = sorted({project['language'] for project in projects.values()})
    return render_template(
        'index.html',
        projects=projects,
        languages=languages,
        show_images=False,
    )

@app.route('/epicycler/')
def epicycler():
    return render_template('epicycler.html')

if __name__ == '__main__':
    app.run(debug=True)
