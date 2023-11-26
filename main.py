with open('books/frankenstein.txt', 'r') as f:
    #text = f.read()
    file_contents = f.read()
    print(file_contents)
    words_count = len(file_contents.split())
    print(words_count)

def count_characters(file_contents):
    file_contents = file_contents.lower()
    counts = {}
    for character in file_contents:
        if character.isalpha():
            if character in counts:
                counts[character] += 1
            else:
                counts[character] = 1
    return counts

results = count_characters(file_contents)
print(results)