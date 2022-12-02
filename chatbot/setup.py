#!/usr/bin/env python

from os.path import join, dirname, abspath
from runpy import run_path
from setuptools import setup


version = run_path(join(abspath(dirname(__file__)), 'chatbot', 'version.py'))
constants = run_path(join(abspath(dirname(__file__)), 'chatbot', 'constants.py'))
LANGUAGE_SUPPORT = constants['LANGUAGE_SUPPORT']
package_data = ["media/send.png", "media/robot.png", "media/user.png"]

with open("README.md", "r") as fh:
    long_description = fh.read()

for language in LANGUAGE_SUPPORT:
    package_data.extend([
        "local/%s/default.template" % language,
        "local/%s/words.txt" % language,
        "local/%s/substitutions.json" % language
    ])
package_dir = {
        'chatbot': 'chatbot',
        'chatbot.spellcheck': 'chatbot/spellcheck',
        'chatbot.substitution': 'chatbot/substitution',
        'chatbot.chat_gui': 'chatbot/chat_gui'
    }
    install_requires=[
          'requests',
      ]
)
