import pytest

from .data.migrate import create_db_and_tables
from .data.function import BD
from .data.data import stations, colors
from .data.models import  Color, Station


@pytest.fixture(scope="class")
def create_or_update_bd():
    create_db_and_tables()
    stations_data = []
    for station in stations:
        stations_data.append(Station(name=station))
    BD().write(stations_data)
    color_data = []
    for color in colors:
        color_data.append(Color(name=color))
    BD().write(color_data)


@pytest.fixture(scope="session")
def database():
    return BD()

@pytest.fixture(scope="session")
def run():
    pass

class B:
    
    def hello(self):
        print("hello")

@pytest.fixture(scope="function")
def abc():
    print("Начало фикстуры")
    db = B()
    yield db
    db.hello()
    print("конец фикстуры")