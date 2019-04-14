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


def test_should_retrieve_most_stargazed_projects():
    result = github_graphql_api.most_stargazed_projects("willianantunes", 3)

    assert len(result) == 3
    assert result[0] == {
        "projectsUrl": "https://github.com/willianantunes/honesto-sqn/projects",
        "description": "Receba notificações de gastos suspeitos do seu político",
    }
    assert result[1] == {
        "projectsUrl": "https://github.com/willianantunes/django-graphql-playground/projects",
        "description": "Yet another Django GraphQL Playground project",
    }
    assert result[2] == {
        "projectsUrl": "https://github.com/willianantunes/spring-boot-vuejs/projects",
        "description": "An honest CRUD project to know how Vue.js works",
    }
