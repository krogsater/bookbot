def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")

        words = file_contents.split()
        word_count = len(words)
        print(f"Number of words: {word_count}")

        lowered_string = file_contents.lower()

        char_count = {}

        for char in lowered_string:
            if char.isalpha():
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1

        # Convert char_count dictionary to a list of dictionaries
        char_list = [{"char": char, "num": count} for char, count in char_count.items()]

        # Define the function to sort by the "num" key
        def sort_on(item):
            return item["num"]

        # Sort the list of dictionaries by count
        char_list.sort(reverse=True, key=sort_on)

        # Print the sorted report
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")

main()
