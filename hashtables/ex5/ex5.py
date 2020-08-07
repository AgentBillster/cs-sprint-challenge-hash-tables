# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # put both arrays in own dictionary
    # cross check dictionary keys to that contain queries
    # add thsoe queries to arr
    cache = {}
    for name in files:
        cache[name] = name.rsplit('/', 1)[-1]

    result = []

    for q in queries:
        result = result + [k for k, v in cache.items() if v == q]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
