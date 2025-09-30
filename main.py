from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.people_you_know import people_you_may_know
from src.pages_you_may_like import pages_you_might_like

def main():
    """
    Main program:
    1. Load and clean data
    2. Ask for user ID
    3. Show 'People You May Know' and 'Pages You May Like' suggestions
    """

    # Load and clean data
    data = load_data("data/data2.json")
    data = clean_data(data)

    # Ask for user ID
    try:
        user_id = int(input("Enter your user ID: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Suggest people the user may know
    suggested_people = people_you_may_know(user_id, data)
    if suggested_people:
        print(f"\nPeople you may know for User {user_id}:")
        print(" ")
        for name in suggested_people:
            print(f"- {name}")
    else:
        print(f"\nNo 'people you may know' suggestions found for User {user_id}.")

    # Suggest pages the user may like (only pages with score >= 1)
    suggested_pages = pages_you_might_like(user_id, data, min_score=1)
    if suggested_pages:
        print(f"\nPages you may like for User {user_id}:")
        print(" ")
        for page in suggested_pages:
            print(f"- {page}")
        print(" ")    
    else:
        print(f"\nNo 'pages you may like' suggestions found for User {user_id}.")


if __name__ == "__main__":
    main()
