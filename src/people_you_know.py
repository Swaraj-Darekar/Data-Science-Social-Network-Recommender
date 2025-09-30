def people_you_may_know(user_id, data):
    """
    Suggest people the user may know based on mutual friends.
    
    """

    # Build dictionary: user_id -> set of friends
    user_friends = {user['id']: set(user['friends']) for user in data['users']}

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}

    # Count mutual friends
    for friend in direct_friends:
        for mutual in user_friends.get(friend, []):
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    # Sort by number of mutual friends (descending)
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)

    # Convert IDs to names
    id_to_name = {user['id']: user['name'] for user in data['users']}
    suggested_names = [id_to_name[user_id] for user_id, _ in sorted_suggestions]

    return suggested_names
