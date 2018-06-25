import re


def main():
    file_name = './.git/config'
    file_name = './tmp'
    name_before = 'aaaaa'
    name_after = 'aaaaa2'
    pattern = re.compile(r'https://github.com/[a-zA-Z0-9_\-]+/')
    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, 'w') as f:
        for l in lines:
            if pattern.match(l):
                print(pattern.sub(f'https://githum.com/{name_after}/', l),
                      end='')
            else:
                print(l, end='')
            f.write(l)


if __name__ == '__main__':
    main()
