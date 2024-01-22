def wordCount(text):
    words = text.split()
    return len(words)


def letterCount(text):
    text_lower = text.lower()

    char_counts = {}

    for char in text_lower:
         
         if char.isalpha():
              char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


def print_report(file_contents, char_counts):
     num_words = wordCount(file_contents)

     print(f"{num_words} words found in the doc \n")

     print("Char counts:")
     for char, count in char_counts.items():
          print(f"the '{char}' character was found {count} times")


def main():
        path = input("enter path to file you want to read: \n")

        with open(path, 'r') as f:
            file_contents = f.read()
            print(file_contents)


            char_counts = letterCount(file_contents)

            print("--- Begin Report ---")
            print_report(file_contents, char_counts)
            print("--- End report ---")

#            num_words = wordCount(file_contents)
#            print(f"Number of words = {num_words}")
#            

#            char_list = letterCount(file_contents)
#
#            char_set = set(char_list)

#            sorted_chars = sorted(char_set)

#            print(f"Sorted list of chars:")
#            print(char_list)

#         char_counts = letterCount(file_contents)
#            print(f"Character counts:")
#            print(char_counts)

            return 0

if __name__ == "__main__":
    main()
