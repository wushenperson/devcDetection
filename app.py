from flask import Flask
from pathlib import Path
import os

App = Flask(__name__)
cur_dir_path = Path(os.path.abspath(__file__)).parent


@App.route("/js/<path:lpath>")
def source_map_test(lpath: str):
    print(lpath)
    with open(cur_dir_path.joinpath(lpath), "r", encoding="utf8") as fp:
        return fp.read()


@App.route("/")
def index():

    with open(cur_dir_path.joinpath("index.html"), "r", encoding="utf8") as fp:
        return fp.read()


App.run()
