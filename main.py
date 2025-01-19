def sort_on(letters):
    return letters['count']

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    words_count = len(words)

    characters_count = {}
    lower_characters = file_contents.lower()
    for character in lower_characters:
        if character not in characters_count:
            characters_count[character] = 1
        else:
            characters_count[character] += 1

    letters = []
    for key, value in characters_count.items():
        if key.isalpha():
            letters.append({"character": key, "count": value})

    letters.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    for item in letters:
        print(f"The {item['character']} character was found {item['count']} times")

main()
