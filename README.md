# Pre requis

python need to be installed on your host

```
pip install pipenv
cd /path/root/site
pipenv install
```

# Command

`pipenv run flask run`

# Test requirements

1. Install pytest
`pip install -U pytest`

2. Install pytest-html
`pip install pytest-html`

3. Install mocker
`python -m pip install pytest-mock`

4. Install Locust
`pip install locust`
# Test

1. Execute all the tests.
`pytest -v`
2. Test non-root URL paths.
`pytest -v -k path`
3. Export results in HTML
`pytest -v  --html=report.html --self-contained-html`
4. Test path other
`pytest -m others -v`
5. Locust
`locust -f locustfile.py`
