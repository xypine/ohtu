from urllib import request
from project import Project
from tomlkit import parse


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        structured = parse(content)
        tool = structured["tool"]
        poetry = tool["poetry"]
        name = poetry["name"]
        description = poetry["description"]
        authors = poetry["authors"]
        dependencies = poetry["dependencies"]
        dependencies_dev = poetry["group"]["dev"]["dependencies"]
        return Project(name, description, authors, dependencies, dependencies_dev)
