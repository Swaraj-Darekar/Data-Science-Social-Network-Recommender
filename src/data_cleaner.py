def clean_data(data):
    """
    Clean the social network data.
    Steps:
    1. Remove users with empty names
    2. Remove duplicate friends for each user
    3. Remove inactive users (no friends & no liked pages)
    4. Remove duplicate pages by keeping only the last one
    """

    # Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Remove inactive users
    data["users"] = [
        user for user in data["users"] if user["friends"] or user["liked_pages"]
    ]

    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())

    return data
