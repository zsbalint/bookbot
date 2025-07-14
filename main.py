from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_to_check = sys.argv[1]

    text = get_book_text(book_to_check)
    count = count_words(text)
    characters = count_characters(text)
    sorted_char_count = sort_dict(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_check}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()