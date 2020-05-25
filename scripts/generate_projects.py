import configparser
import json
import os
import pathlib

import github

projects = {

    'EZPZ Plotting': {
        'tags': ['Featured', 'Python'],
        'image': 'img/ezpz-plotting.png',
        'links': {
            'github': 'ezpz-plotting',
        },
    },

    'EZPZ Reducer': {
        'tags': ['Python'],
        'image': '',
        'links': {
            'github': 'ezpz-reducer',
        },
    },
    
    'GeoPhotos': {
        'tags': ['Python'],
        'image': '',
        'links': {
            'github': 'geophotos',
        },
    },
    
    'Reddit Downloader': {
        'tags': ['Featured', 'Python'],
        'image': 'img/reddit-downloader.png',
        'links': {
            'github': 'reddit-downloader',
        },
    },
    
    'Drawing Epicycler': {
        'tags': ['Featured', 'JavaScript'],
        'image': 'img/drawing-epicycler.png',
        'links': {
            'github': 'drawing-epicycler',
            'preview': '/epicycler/',
        },
    },

    'Portfolio Website': {
        'tags': ['Python', 'HTML/CSS'],
        'image': '',
        'links': {
            'github': 'personal-website-v2',
            'preview': '/',
        },
    },

    'Cage Discord Bot': {
        'tags': ['Featured', 'Python'],
        'image': '',
        'links': {
            'github': 'cage-discord-bot',
        },
    },

    'Bother Me Not': {
        'tags': ['Arduino'],
        'image': '',
        'links': {
            'github': 'bother-me-not',
        },
    },

    'Tooner': {
        'tags': ['Python'],
        'image': '',
        'links': {
            'github': 'tooner',
        },
    },

    'MultiTooner': {
        'tags': ['Featured', 'Python'],
        'image': '',
        'links': {
            'github': 'multitooner',
        },
    },

}

if __name__ == '__main__':
    SCRIPTS_FOLDER = pathlib.Path(__file__).resolve().parent
    PROJECT_FOLDER = SCRIPTS_FOLDER.parent
    STATIC_FOLDER = os.path.join(PROJECT_FOLDER, 'static')
    PROJECTS_FILE = os.path.join(STATIC_FOLDER, 'projects.json')

    DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
    CONFIG_FILE = os.path.join(DATA_FOLDER, 'config.ini')

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    g = github.Github(config['github']['token'])
    user = g.get_user()
    for project, info in projects.items():
        if 'links' in info and 'github' in info['links']:
            try:
                repository = user.get_repo(info['links']['github'])
                description = repository.description
            except github.GithubException:
                description = None
            info['description'] = description

    with open(PROJECTS_FILE, 'w') as output:
        json.dump(projects, output, indent=4)
