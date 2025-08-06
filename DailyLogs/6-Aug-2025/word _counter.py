# Take a string and count how many times each word appears.

user_input = input("Write down the messages: ").lower().split()

word_count = {}
distinct_word_count = 0

for word in user_input:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        distinct_word_count += 1

print(f"Total number of Distinct word: {distinct_word_count}")

for word, count in word_count.items():
    print(f"{word}: {count}")

