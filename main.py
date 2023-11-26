with open('books/frankenstein.txt', 'r') as f:
    #text = f.read()
    file_contents = f.read()
    # print(file_contents)
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


def report_character_counts(counts):
    counts = list(counts.items())
    counts.sort(key=lambda tup: tup[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    for character, count in counts:
        print(f"The '{character}' character was found {count} times.")

    print("--- End report of books/frankenstein.txt ---")

report_character_counts(results)
