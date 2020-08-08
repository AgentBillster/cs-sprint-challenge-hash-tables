# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """

    my_dict = {}

    result = []

    for path in files:

        file_item = path.split('/')[-1]

        if file_item in my_dict:

            my_dict[file_item].append(path)
        else:

            my_dict[file_item] = [path]

    for q in queries:
        if q in my_dict:
            results = my_dict[q]

            for path in results:
                result.append(path)

    return result


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
