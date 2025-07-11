import json


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)
    try:
        age = int(age)
    except ValueError:
        print("Only numbers allowed.")
        return
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' and 'age' is supported): ").strip().lower()

    if filter_option == "age":
        age_to_search = input("Enter a age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
