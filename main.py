import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return(content)

from stats import word_count

from stats import character_count

from stats import report

def main():
    
    total_count = 0
    total_count = word_count(get_book_text(file_path))
    #print(f"Found {total_count} total words")
    char_count = character_count(get_book_text(file_path))
    report(total_count,char_count,file_path)

main()
