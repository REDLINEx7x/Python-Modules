import sys

def sorting(items_list):
    i = 0
    while i < len(items_list):
        j = i + 1
        while j < len(items_list):
            if items_list[j][1] > items_list[i][1]:
                temp = items_list[i]
                items_list[i] = items_list[j]
                items_list[j] = temp
            j += 1
        i += 1
    #return (items_list)

items = sys.argv
if len(sys.argv) > 1:
    inventory = {}
    for i in sys.argv[1:]:
        item = i.split(":")
        key = item[0]
        value = int(item[1])
        inventory.update({key: value})
    print(inventory)
    values_count = 0
    for i in inventory.values():
        values_count += i
print(f"Total items in inventory: {values_count}")
print(f"Unique item types: {len(inventory)}")

print("=== Inventory Statistics ===")

items_list = list(inventory.items())
sorting(items_list)
for item in items_list:
    percent = (item[1] / values_count) * 100
    if(item[1] > 1):
        print(f"{item[0]}: {item[1]} units ({percent})")
    else:
         print(f"{item[0]}: {item[1]} unit ({percent})")

#categories = {
#    "Moderate": {},
#    "Scarce": {}
#}
#i = 0
#while i < len(items_list):
#    name = items_list[i][0]
#    qty = items_list[i][1]
#    if qty >= 4:
#        categories["Moderate"].update({name: qty})
#    else:
#        categories["Scarce"].update({name: qty})
#    i += 1

#print(categories)
## 1. Jib ga' l-keys (Moderate, Scarce) f-list
#category_keys = list(categories.keys())
#i = 0

#while i < len(category_keys):
#    cat_name = category_keys[i]
#    # Sta'mel .get() bash t-jib d-dictionary li westo
#    val = categories.get(key)
#    print(f"{key}: {val}")

#    i += 1
#print
#print(i)

