import pytest

@pytest.fixture(scope="function")
def my_global_fixture():
    print("global lecture_pytest fixture setup")
    yield
    print("global lecture_pytest fixture teardown")