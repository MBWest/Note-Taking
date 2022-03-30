# ----------Dictionaries----------
# Dictionaries {"key":"value"}
my_dict = {"Name": "Matthew", "Age": 27, "Hobby": "Code"}
f"The name value stored in is: {my_dict['Name']}"  # You call on dictionary values by referencing the key

# Add a value to the dictionary
my_dict["New Key"] = "New Value"

# Remove a key and value from the dictionary
del my_dict["New Key"]

# Print the keys
print(my_dict.keys())

# Print the Values
print(my_dict.values())
      
# Print the items
print(my_dict.items())

# For Loop through dictionary (This is the default return even without the .keys)
for key in my_dict.keys()
      print(key)

# Extract both the key and value
for key, value in my_dict.items()
      print(key, value)

# Check to see if a value is part of a dictionary
"Matthew" in my_dict.value()