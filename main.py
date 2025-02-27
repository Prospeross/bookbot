from stats import get_num_words
from stats import char_count
from stats import sort_letters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    book_string = get_book_text(file_path)
    words_count = get_num_words(book_string)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    letters_count = char_count(book_string)
    dict_sorted = sort_letters(letters_count)
    for data in dict_sorted:
        for char, count in data.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")

main()