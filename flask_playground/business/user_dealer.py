from flask_playground.services import github_graphql_api


def is_eligible(username: str) -> bool:
    number_of_followers = github_graphql_api.total_number_of_followers(username)
    return True if number_of_followers > 10 else False
