def read_text_file(filename: str) -> None:
    """
    Read text file line by line. Can also use open(0) to read from stdin.
    """
    with open(filename, 'r') as f:
        for s in f:
            print(s.rstrip())


def read_stdin() -> None:
    """
    This can be used for creating programs which you can pipe data into,
    e.g. "cat file.txt | python3 file-utils.py"
    """
    from sys import stdin
    for s in stdin:
        print(s.rstrip())


if __name__ == '__main__':
    read_stdin()
