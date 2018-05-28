#!/usr/local/bin/python3


def shortest_path(path):
    paths = []
    if path[0] == '/': #preserve root
        paths.append('/')

    for p in path.split('/'):
        if p == '.' or p == '':
            continue
        elif p == '..':
            if p[-1] == '/':
                raise ValueError('Invalid Path')
            paths.pop()
        else:
            paths.append(p)

    # return '/' + '/'.join(paths[1:]) if paths[0] == '/' else '/'.join(paths)
    res = '/'.join(paths)
    return res[res.startswith('//'):]


if __name__ == '__main__':
    print('Find shortest equivalen path')
    path = '/usr/local/awk/../bin/../../local/bin/python3'
    print('shortest_path({}) -> {}'.format(path, shortest_path(path)))
