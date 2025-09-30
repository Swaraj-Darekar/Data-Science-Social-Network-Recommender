def pages_you_might_like(user_id, data, min_score=1):
    """
    Suggest pages a user might like based on mutual interests.
    Only suggest pages with score >= min_score.
    
  
    """

    # Build dictionary: user_id -> set of liked pages
    user_pages = {user['id']: set(user['liked_pages']) for user in data['users']}

    if user_id not in user_pages:
        return []

    user_liked_pages = user_pages[user_id]
    page_suggestions = {}

    # Compare with other users
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
            for page_id in pages:
                if page_id not in user_liked_pages:
                    # Score = number of shared pages with this user
                    page_suggestions[page_id] = page_suggestions.get(page_id, 0) + len(shared_pages)

    # Only keep pages with score >= min_score
    filtered_pages = {pid: score for pid, score in page_suggestions.items() if score >= min_score}

    # Sort pages by score descending
    sorted_pages = sorted(filtered_pages.items(), key=lambda x: x[1], reverse=True)

    # Convert page IDs to names
    id_to_name = {page['id']: page['name'] for page in data['pages']}
    suggested_page_names = [id_to_name[page_id] for page_id, _ in sorted_pages]

    return suggested_page_names
