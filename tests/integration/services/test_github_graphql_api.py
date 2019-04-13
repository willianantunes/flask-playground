from flask_playground.services import github_graphql_api


def test_should_return_none_when_user_does_not_exist():
    result = github_graphql_api.total_number_of_followers("this-user-indeed-does-not-exist")

    assert result is None


def test_should_return_more_than_five_followers():
    result = github_graphql_api.total_number_of_followers("willianantunes")

    assert result > 5
