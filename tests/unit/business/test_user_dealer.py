from pytest_mock import MockFixture

from flask_playground.business import user_dealer


def test_should_be_eligible_when_number_of_followers_greather_than_10(mocker: MockFixture):
    mocked_github_graphql_api = mocker.patch("flask_playground.business.user_dealer.github_graphql_api")
    mocked_total_number_of_followers = mocked_github_graphql_api.total_number_of_followers
    mocked_total_number_of_followers.return_value = 11
    fake_username_one = "fake-username-one"

    result = user_dealer.is_eligible(fake_username_one)

    mocked_total_number_of_followers.assert_called_once_with(fake_username_one)
    assert result is True

    mocked_github_graphql_api.reset_mock()
    mocked_total_number_of_followers = mocked_github_graphql_api.total_number_of_followers
    mocked_total_number_of_followers.return_value = 500
    fake_username_two = "fake-username-two"

    result = user_dealer.is_eligible(fake_username_two)

    mocked_total_number_of_followers.assert_called_once_with(fake_username_two)
    assert result is True


def test_should_not_be_eligible_when_number_of_followers_less_or_equal_than_10(mocker: MockFixture):
    mocked_github_graphql_api = mocker.patch("flask_playground.business.user_dealer.github_graphql_api")
    mocked_total_number_of_followers = mocked_github_graphql_api.total_number_of_followers
    mocked_total_number_of_followers.return_value = 10
    fake_username_one = "fake-username-one"

    result = user_dealer.is_eligible(fake_username_one)

    mocked_total_number_of_followers.assert_called_once_with(fake_username_one)
    assert result is False

    mocked_github_graphql_api.reset_mock()
    mocked_total_number_of_followers = mocked_github_graphql_api.total_number_of_followers
    mocked_total_number_of_followers.return_value = 1
    fake_username_two = "fake-username-two"

    result = user_dealer.is_eligible(fake_username_two)

    mocked_total_number_of_followers.assert_called_once_with(fake_username_two)
    assert result is False
