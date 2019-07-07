from typing import Callable
from os import path
from livereload import Server, shell


def prefix_matcher(str: str) -> Callable[[str], bool]:
    return lambda target: target.startswith(str)


if __name__ == '__main__':
    server = Server()
    cmd = shell('pipenv run doc')
    dir = path.dirname(path.abspath(__file__))
    server.watch(dir, cmd, ignore=prefix_matcher(path.join(dir, '_build')))
    server.watch('structural_calculator', cmd)
    server.serve(root=path.join(dir, '_build', 'html'))
