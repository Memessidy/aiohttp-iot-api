import pytest
from application import models


@pytest.mark.asyncio
async def test_create_user(cli):
    payload = {
        "name": "TestUser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    resp = await cli.post('/users', json=payload)
    assert resp.status == 200
    data = await resp.json()
    assert 'user_id' in data


@pytest.mark.asyncio
async def test_create_location(cli):
    payload = {
        "name": "TestLocation"
    }
    resp = await cli.post('/locations', json=payload)
    assert resp.status == 200
    data = await resp.json()
    assert 'location_id' in data


@pytest.mark.asyncio
async def test_create_device(cli):
    payload = {
        "name": "TestDevice",
        "type": "Device Type",
        "login": "TestLogin",
        "password": "PASSWORD",
        "location": 1,
        "api_user": 1
    }

    resp = await cli.post('/devices', json=payload)
    assert resp.status == 200
    data = await resp.json()
    assert 'device_id' in data


@pytest.mark.asyncio
async def test_get_user(cli):
    resp = await cli.get(f'/users/1')
    assert resp.status == 200
    data = await resp.json()
    assert data['name'] == 'TestUser'
    assert data['email'] == 'test@example.com'


@pytest.mark.asyncio
async def test_get_device(cli):
    resp = await cli.get(f'/devices/1')
    assert resp.status == 200
    data = await resp.json()
    assert data['name'] == 'TestDevice'
    assert data['password'] == 'PASSWORD'


@pytest.mark.asyncio
async def test_update_user(cli):
    payload = {
        "name": "UpdatedUser"
    }
    resp = await cli.put(f'/users/1', json=payload)
    assert resp.status == 200
    data = await resp.json()
    assert data['status'] == 'User updated'

    updated_user = models.ApiUser.get_by_id(1)
    assert updated_user.name == 'UpdatedUser'


@pytest.mark.asyncio
async def test_update_device(cli):
    payload = {
        "name": "TestDevice2",
        "type": "Device Type2",
        "login": "TestLogin2",
        "password": "PASSWORD11111",
        "location": 1,
        "api_user": 1
    }
    resp = await cli.put(f'/devices/1', json=payload)
    assert resp.status == 200
    data = await resp.json()
    assert data['status'] == 'Device updated'

    updated_device = models.Device.get_by_id(1)
    assert updated_device.name == 'TestDevice2'


@pytest.mark.asyncio
async def test_delete_device(cli):
    resp = await cli.delete(f'/devices/1')
    assert resp.status == 200
    data = await resp.json()
    assert data['status'] == 'Device deleted'
