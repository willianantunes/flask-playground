import os

import pytest

from flask_playground.services import github_graphql_api
from flask_playground.services.exceps import GithubGraphqlApiNotProperlyConfiguredException


def test_should_throw_exception_when_user_does_not_exist():

    with pytest.raises(GithubGraphqlApiNotProperlyConfiguredException) as exception:
        github_graphql_api.total_number_of_followers("this-user-indeed-does-not-exist")

    assert exception.value.args[0] == "An API call is broken or wrong"


def test_should_return_more_than_five_followers():
    result = github_graphql_api.total_number_of_followers("willianantunes")

    assert result > 5


def test_should_throw_exception_if_required_properties_are_missing(monkeypatch):
    github_graphql_endpoint = os.getenv("WA_GITHUB_GRAPHQL_ENDPOINT")
    monkeypatch.setattr(github_graphql_api, "GITHUB_GRAPHQL_ENDPOINT", None)

    with pytest.raises(GithubGraphqlApiNotProperlyConfiguredException) as exception:
        github_graphql_api._get_client()

    assert exception.value.args[0] == "Token and endpoint properties are required"

    monkeypatch.setattr(github_graphql_api, "GITHUB_GRAPHQL_ENDPOINT", github_graphql_endpoint)

    configured_client = github_graphql_api._get_client()
    assert configured_client is not None

    monkeypatch.setattr(github_graphql_api, "GITHUB_API_TOKEN", None)

    with pytest.raises(GithubGraphqlApiNotProperlyConfiguredException) as exception:
        github_graphql_api._get_client()

    assert exception.value.args[0] == "Token and endpoint properties are required"
