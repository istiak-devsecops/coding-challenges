# Add two lists element-wise using zip() and map()

a = [1, 2, 3]
b = [4, 5, 6]

zip_obj  = zip(a,b)

sum_of_two_list_element_wise = []

for obj in zip_obj:
        sum_of_two_list_element_wise.append(sum(obj))

print(sum_of_two_list_element_wise)


sum_of_two_list_2 = [a + b for a,b in zip(a,b)] # doing the same thing with list comprehention
print(sum_of_two_list_2)



