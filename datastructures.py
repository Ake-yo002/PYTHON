# Initialize empty list
my_list = []

# Add numbers to list
my_list.append(10)  # Add 10 to end
my_list.append(20)  # Add 20 to end
my_list.append(30)  # Add 30 to end
my_list.append(40)  # Add 40 to end

# Insert 15 at position 1
my_list.insert(1, 15)

# Combine with another list
another_list = [50, 60, 70]
my_list.extend(another_list)  # Add all elements

# Remove last item
my_list.pop()

# Sort list (ascending)
my_list.sort()

# Find position of 30
index_of_30 = my_list.index(30)

# Print results
print(f"The index of 30 is: {index_of_30}")
print(f"The final list is: {my_list}")
