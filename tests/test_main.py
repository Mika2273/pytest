import pytest
from app import appflask

@pytest.mark.root
def test_flask_root():
    appflask.config['TESTING'] = True
    client = appflask.test_client()
    result = client.get('/')
    assert b'<p>Hello, World!</p>' == result.data


@pytest.fixture(scope='module')
def page_no():
    page = 2
    return page


@pytest.mark.other
def test_flask_path1(page_no):
    appflask.config['TESTING'] = True
    client = appflask.test_client()
    result = client.get('/other?page=' + str(page_no))
    assert b'<p>Hello, Other!</p><p>Page : 2</p>' == result.data


@pytest.fixture(scope='module')
def value_no():
    value = 2
    return value


@pytest.mark.exp
def test_flask_path2(value_no):
    appflask.config['TESTING'] = True
    client = appflask.test_client()
    result = client.get('/exp?value=' + str(value_no))
    assert b'<p>Exposant 2 de 2 : 4</p>' == result.data


@pytest.mark.parametrize(('value', 'expected'), [
    (1, b'<p>Exposant 2 de 1 : 1</p>'),
    (2, b'<p>Exposant 2 de 2 : 4</p>'),
    (3, b'<p>Exposant 2 de 3 : 9</p>'),
    (4, b'<p>Exposant 2 de 4 : 16</p>'),
    (5, b'<p>Exposant 2 de 5 : 25</p>'),
])
@pytest.mark.exp
def test_flask_path2_parametrize(value, expected):
    appflask.config['TESTING'] = True
    client = appflask.test_client()
    result = client.get('/exp?value=' + str(value))
    assert result.data == expected


def test_flask_path2_mock(mocker):

    appflask.config['TESTING'] = True
    client = appflask.test_client()

    mocker.patch("app.get_hello",return_value = 'Hello Mika')

    result = client.get('/')
    assert b'Hello Mika' == result.data

@pytest.mark.exp
@pytest.mark.parametrize("value", ["x", "&", None])
def test_flask_path2_except(value:int):
    try:
        pow(value, 2)
    except TypeError:
        assert True
