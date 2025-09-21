# filter in int

nums = [ 2,3,5,6,7,9,12,34,45]

even_list = filter(lambda x:x % 2 == 0, nums)
print(list(even_list))

#filter with str

text = ["python", "java", "c", "go", "rust"]

word_greater_than_two = filter(lambda x:len(x) > 2, text)
print(list(word_greater_than_two))