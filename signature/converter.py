import json

# Example JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string to Python object
python_object = json.loads(json_string)

# Now you can access the data as a Python dictionary
print(python_object['name'])  # Output: John
print(python_object['age'])   # Output: 30
print(python_object['city'])  # Output: New York