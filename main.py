def main():
    bookName = "frankenstein"
    book_path = f"books/{bookName}.txt"
    text = get_book_text(book_path)
    numWords = get_word_count(text)
    character_dict = get_character_appearance(text)
    list_of_dictionary_characters = get_list_of_dict(character_dict)
    list_of_dictionary_characters.sort(reverse=True, key=sort_on)
    print(f"---Begin report of books/frankenstein.txt---")
    print(f"{numWords} words were found in the document called: {bookName}\n")
    for i in list_of_dictionary_characters:
        print(f"The '{i["letter"]}' character was found {i["appearance"]} times")
    print("---End of report.---")

    # print(numWords)
    # print(character_dict)
    #print(list_of_dictionary_characters)


def get_character_appearance(text):
    charsDict = {}
    for word in text.split():
        for letter in word:
            if letter.lower() in charsDict.keys():
                charsDict[letter.lower()] += 1
            else:
                charsDict[letter.lower()] = 1

    return charsDict


def get_list_of_dict(dict):
    listOfDicts = []
    for i in dict:
        listOfDicts.append({"letter": i, "appearance": dict[i]})
    return listOfDicts


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["appearance"]


if __name__ == "__main__":
    main()
