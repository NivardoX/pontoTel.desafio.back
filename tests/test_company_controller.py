import json

from app import Company


def test_db(app):
    client = app.test_client()
    url = "/"

    response = client.get(url)
    assert response.get_data() == b"pontotel_teste"
    assert response.status_code == 200


def test_get_companies(app, db):
    from flask_jwt_extended import create_access_token

    with app.app_context():

        client = app.test_client()
        access_token = create_access_token(1)
        headers = {"Authorization": "Bearer {}".format(access_token)}

        url = "/companies"
        response = client.get(url, headers=headers)

        output = json.loads(response.get_data())
        print(output)

        assert output["pagination"]["itens_count"] == 67
        assert not output["has_error"]
        assert response.status_code == 200


def test_view_company(app, db):
    from flask_jwt_extended import create_access_token

    with app.app_context():

        client = app.test_client()
        access_token = create_access_token(1)
        headers = {"Authorization": "Bearer {}".format(access_token)}

        url = "/company/67"

        response = client.get(url, headers=headers)

        output = json.loads(response.get_data())
        print(output)
        assert not output["has_error"]
        assert response.status_code == 200


def test_delete_company(app, db):
    from flask_jwt_extended import create_access_token

    with app.app_context():

        client = app.test_client()
        access_token = create_access_token(1)
        headers = {"Authorization": "Bearer {}".format(access_token)}

        url = "/company/67"

        response = client.delete(url, headers=headers)

        output = json.loads(response.get_data())

        assert not output["has_error"]
        assert response.status_code == 200

        url = "/companies"

        response = client.get(url, headers=headers)

        output = json.loads(response.get_data())
        print(output)

        assert output["pagination"]["itens_count"] == 66
        assert not output["has_error"]
        assert response.status_code == 200


def test_get_history(app, db):
    from flask_jwt_extended import create_access_token

    with app.app_context():

        client = app.test_client()
        access_token = create_access_token(1)
        headers = {"Authorization": "Bearer {}".format(access_token)}

        url = "/company/^BVSP/history"

        response = client.get(url, headers=headers)

        output = json.loads(response.get_data())

        assert len(output.get("history", []))
        assert not output["has_error"]
        assert response.status_code == 200


def test_post_company(app, db):
    from flask_jwt_extended import create_access_token

    with app.app_context():
        client = app.test_client()
        access_token = create_access_token(1)
        headers = {"Authorization": "Bearer {}".format(access_token)}

        url = "/company"
        input = {"name": "teste", "symbol": "teste", "peso": 0.0}

        response = client.post(url, data=input, headers=headers)

        output = json.loads(response.get_data())
        print(output)
        assert output["has_error"]
        assert output["message"] == "Ocorreram erros no preenchimento do formulário."
        assert response.status_code == 200
