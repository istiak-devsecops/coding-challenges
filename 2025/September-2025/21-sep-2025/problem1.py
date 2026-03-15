# using map function with int

nums = [2,5,7,9]

result = list(map(lambda x:x**2, nums))
print(result)


# using map with sting
text = "python"

text_transformation = list(map(str.upper,text))
print(text_transformation)