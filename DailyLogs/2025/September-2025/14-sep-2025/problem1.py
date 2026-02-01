# Write a function that takes a list and returns a new list with only unique elements (no duplicates), keeping the original order.

def unique_order(lst):
    uniq_items = set()
    uniq_items_list = []
    for iteam in lst:
        if iteam not in uniq_items:
            uniq_items.add(iteam)
            uniq_items_list.append(iteam)
    return uniq_items_list

num_list = [1,2,4,5,3,5,2,5,7,9,0,10]

result = unique_order(num_list)
print(f"Unique iteams in order: {result}")
