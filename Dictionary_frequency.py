test_dictionary = {
    "Mingrui": "4",
    "Andrew": "4",
    "eeli":"5",
    "Ryan":"7",
    "Rehaan":"5"
}
item_for_test = input("Enter the item you want to check the frequency of: ").lower().strip()
frequency_of_item = 0
for key, value in test_dictionary.items():
    if test_dictionary[key] == item_for_test:
        frequency_of_item += 1
    print(key)
    
print(f"There are {frequency_of_item} occurences of {item_for_test}.")
