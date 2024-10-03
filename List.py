# Create a list
my_list = []

# Function to create and print a list
def create_list(elements):
    global my_list
    my_list = elements
    print(f"List created: {my_list}")

# Function to append an item to the list
def append_to_list(item):
    my_list.append(item)
    print(f"Appended {item} to the list: {my_list}")

# Function to remove an item from the list
def remove_from_list(item):
    if item in my_list:
        my_list.remove(item)
        print(f"Removed {item} from the list: {my_list}")
    else:
        print(f"Item {item} not found in the list.")

# Example usage
# Creating a list
create_list([1, 2, 3])

# Appending an item to the list
append_to_list(4)

# Removing an item from the list
remove_from_list(2)

# Trying to remove an item not in the list
remove_from_list(10)
