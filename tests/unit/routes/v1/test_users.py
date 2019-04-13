from pytest import fixture
from pytest_mock import MockFixture

from init import app

BASE_URL = "/api/v1/users"


@fixture
def fake_client():
    app.debug = True
    return app.test_client()


def test_should_give_bad_request_if_username_is_not_provided_when_evaluation_eligibility(fake_client):
    response = fake_client.get(f"{BASE_URL}/eligible")

    assert response.status_code == 400
    assert response.get_json() == {"message": "Username is needed to avaluate its eligibility"}


def test_should_return_valid_when_username_is_eligible(fake_client, mocker: MockFixture):
    mocked_user_dealer = mocker.patch("flask_playground.routes.v1.users.user_dealer")
    mocked_is_eligible = mocked_user_dealer.is_eligible
    mocked_is_eligible.return_value = True

    fake_query_string = {"username": "fake-username"}
    response = fake_client.get(f"{BASE_URL}/eligible", query_string=fake_query_string)

    mocked_is_eligible.assert_called_once_with(fake_query_string["username"])
    assert response.status_code == 200
    assert response.get_json() == {"eligibility": True}
