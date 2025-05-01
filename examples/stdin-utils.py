def read_file(filename: str) -> None:
    with open(filename, 'r') as f:
        for s in f:
            print(s.strip())


if __name__ == '__main__':
    read_file('/Users/w/old.txt')
    print('Hello')
