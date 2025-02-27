def get_num_words(book_content):
    words = book_content.split()
    word_count = len(words)
    return word_count

def char_count(book_content):
    book_letters = []
    letters_count = {}

    book_content_low = book_content.lower()
    words = book_content_low.split()
    for word in words:
        for letters in word:
            book_letters.append(letters)

    for letter in book_letters:
        counter = 0
        if letter not in letters_count:
            letters_count[letter] = 1
        else:
            letters_count[letter] += 1

    return letters_count

def sort_letters(letter_count):
    output = []
    
    for key, value in letter_count.items():
        output.append({key:value})

    output.sort(key = lambda x: list(x.values())[0], reverse=True)

    return output