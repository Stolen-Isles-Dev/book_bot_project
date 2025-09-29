def word_count(get_book_text):
    words = get_book_text.split()
    return len(words)

def character_count(get_book_text):
    characters = {}
    for char in get_book_text:
        char = char.lower()  
        if char in characters:
            characters[char] += 1
        else:                
            characters[char] = 1
    return characters

def report(total_count,char_count,file_path):

    char_list =[]

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_path + "...")
    print("----------- Word Count -----------")
    print(f"Found {total_count} total words")
    print("-----------Character Count -----------")
    for c, n in char_count.items():
        char_list.append({"char": c, "num": n})
        char_list.sort(key=lambda item: item["num"], reverse=True)
    for item in char_list:
         if item['char'].isalpha(): 
             print(f"{item['char']}: {item['num']}")     
         else:
             continue

    
    print("============= END ===============")

