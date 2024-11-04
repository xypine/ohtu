from typing import List


class Project:
    def __init__(self, name: str, description: str, authors: List[str], dependencies: List[str], dev_dependencies: List[str]):
        self.name = name
        self.description = description
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, lst: List):
        stringified = ""
        for item in lst:
            stringified += f"\n- {item}"
        return stringified

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\n"
            f"\nAuthors: {self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies: {self._stringify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
