
nested_dict = {
    "Person_1": {
        "Name": "Benjamin",
        "age": 26,
        "city": "Puente Alto"
    },
    "Person_2": {
            "Name": "Ana",
            "age": 56,
            "city": "Pichidegua"
        },
    "Person_3": {
            "Name": "Patricio",
            "age": 60,
            "city": "Pichidegua"
        }
}

for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f"{sub_key}: {sub_value}")