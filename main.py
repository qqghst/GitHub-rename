import os
import re

import click


@click.command()
@click.option('f', '-f', '--from', help='Name to change from')
@click.option('t', '-t', '--to', prompt='New username', help='Name to change to')
@click.help_option('-h', '--help')
def main(f, t):
    print(f, t)
    name_before = f
    name_after = t
    file_name = './.git/config'
    file_name = './tmp'
    if name_before:
        pattern = re.compile(f'https://github.com/{name_before}/')
    else:
        pattern = re.compile(r'https://github.com/[a-zA-Z0-9_]+/')
    print(pattern)
    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name + '2', 'w') as f:
        matched = 0
        for l in lines:
            if pattern.search(l):
                print(l)
                matched += 1
                f.write(pattern.sub(f'https://githum.com/{name_after}/', l))
            else:
                f.write(l)
        print(f'Matched {matched} time(s).')


if __name__ == '__main__':
    main()
