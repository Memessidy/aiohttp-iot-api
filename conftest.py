import pytest
from app import create_app


@pytest.fixture
def cli(loop, aiohttp_client):
    app, db = create_app()
    yield loop.run_until_complete(aiohttp_client(app))
    db.close()
