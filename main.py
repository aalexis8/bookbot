with open('books/frankenstein.txt', 'r') as f:
    #text = f.read()
    file_contents = f.read()
    print(file_contents)
    words_count = len(file_contents.split())
    print(words_count)

