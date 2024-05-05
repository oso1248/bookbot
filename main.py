def CountLetters(text):
    lower_text = text.lower()
    letter_count = {}
    lst = []
    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for item in letter_count:
        lst.append({"name": item, "count": letter_count[item]})

    return lst

def CountWords(text):
    words = text.split()

    return len(words)

def CreateList(lst):
    result = []
    sorted_list = sorted(lst, key=lambda x: x["count"], reverse=True)
    for item in sorted_list:
        if item["name"].isalpha():
            result.append(f"The {item["name"]} character was found {item["count"]} times")
    
    return result 

def PrintReport(lst, count, f_path):
    print(f"--- Begin report of {f_path}---")
    print(f"{count} words found in the document\n")
    for item in lst:
        print(item)
    print("--- End report ---")

def main():
    f_path = "books/frankenstein.txt"
    with open(f_path) as f:
        file_contents = f.read()

    count = CountWords(file_contents)
    lst = CountLetters(file_contents)
    lst = CreateList(lst)
    PrintReport(lst, count, f_path)

main()
