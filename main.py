import json

def filter_users_by_field(field, value):
    with open("users.json", "r") as file:
        users = json.load(file)

    if field == "age":
        try:
            value = int(value)
        except ValueError:
            print("Only numbers allowed.")
            return

    filtered_users = [
        user for user in users
        if (user.get(field, "").lower() == value.lower() if isinstance(value, str) else user.get(field) == value)
    ]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No user with {field} = {value}")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name, age or email): ").strip().lower()
    if filter_option in ["name", "email", "age"]:
        value_to_search = input(f"Enter {filter_option} to filter users: ").strip()
        filter_users_by_field(filter_option, value_to_search)
    else:
        print("Filtering by that option is not yet supported.")
