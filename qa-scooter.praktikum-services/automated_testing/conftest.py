import pytest

from .data.settings import get_browser, get_courier
from .data.data import generate_user, generate_order


@pytest.fixture(scope="function")
def browser_def():
    browser = get_browser()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def get_user_data():
    return generate_user()


@pytest.fixture(scope="function")
def get_order_date():
    return generate_order()


@pytest.fixture(scope="function")
def courier():
    return get_courier()
