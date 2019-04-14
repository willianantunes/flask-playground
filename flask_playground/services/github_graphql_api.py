import logging
from typing import Any
from typing import Callable

from gql import Client
from gql import gql
from gql.transport.requests import RequestsHTTPTransport

from flask_playground.config.settings import GITHUB_API_TOKEN
from flask_playground.config.settings import GITHUB_GRAPHQL_ENDPOINT
from flask_playground.services.exceps import GithubGraphqlApiNotProperlyConfiguredException

logger = logging.getLogger(__name__)


def _get_client() -> Client:
    if not (GITHUB_API_TOKEN and GITHUB_GRAPHQL_ENDPOINT):
        raise GithubGraphqlApiNotProperlyConfiguredException("Token and endpoint properties are required")
    # TODO I know it will create the same stuff all the time. Working in progress :)
    headers = {"Authorization": f"bearer {GITHUB_API_TOKEN}"}
    _transport = RequestsHTTPTransport(url=GITHUB_GRAPHQL_ENDPOINT, use_json=True, timeout=(5, 25), headers=headers)
    return Client(retries=3, transport=_transport, fetch_schema_from_transport=True)


def _execute(request_to_be_executed: Callable) -> Any:
    try:
        return request_to_be_executed()
    except Exception as e:
        logger.exception(f"An error of type {type(e)} was caught during execution: {e.args}")
        raise GithubGraphqlApiNotProperlyConfiguredException("An API call is broken or wrong")


def total_number_of_followers(github_username_login: str) -> int:
    query = gql(
        f"""
            query {{
              user(login:"{github_username_login}") {{
                followers {{
                  totalCount
                }}
              }}
            }}        
        """
    )
    result = _execute(lambda: _get_client().execute(query))
    return result["user"]["followers"]["totalCount"]


def most_stargazed_projects(github_username_login: str, number_of_projects_to_retrieve: int):
    query = gql(
        f"""
            query threeMostStargazedProjects($data: RepositoryOrder!) {{
              user(login: "{github_username_login}") {{
                repositories(first: {number_of_projects_to_retrieve}, orderBy: $data) {{
                  nodes {{
                    projectsUrl
                    description
                  }}
                }}
              }}
            }}       
        """
    )
    query_variables = {"data": {"field": "STARGAZERS", "direction": "DESC"}}
    result = _execute(lambda: _get_client().execute(query, variable_values=query_variables))
    return result["user"]["repositories"]["nodes"]
