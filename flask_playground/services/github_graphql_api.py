import logging
from typing import Optional

from gql import Client
from gql import gql
from gql.transport.requests import RequestsHTTPTransport

from flask_playground.config.settings import GITHUB_API_TOKEN
from flask_playground.config.settings import GITHUB_GRAPHQL_ENDPOINT
from flask_playground.services.exceps import GithubGraphqlApiNotProperlyConfiguredException

logger = logging.getLogger(__name__)


def _get_client() -> Client:
    if not (GITHUB_API_TOKEN and GITHUB_GRAPHQL_ENDPOINT):
        raise GithubGraphqlApiNotProperlyConfiguredException()
    # TODO I know it will create the same stuff all the time. Working in progress :)
    headers = {"Authorization": f"bearer {GITHUB_API_TOKEN}"}
    _transport = RequestsHTTPTransport(url=GITHUB_GRAPHQL_ENDPOINT, use_json=True, timeout=(5, 25), headers=headers)
    return Client(retries=3, transport=_transport, fetch_schema_from_transport=True)


def total_number_of_followers(github_username_login: str) -> Optional[int]:
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

    try:
        result = _get_client().execute(query)
    except Exception as e:
        if "not_found" in e.args[0].lower():
            logger.warning(f"Provided username login {github_username_login} wasn't found")
            return None
        else:
            raise GithubGraphqlApiNotProperlyConfiguredException("An API call is broken or wrong")

    return result["user"]["followers"]["totalCount"]
