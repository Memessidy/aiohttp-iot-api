from aiohttp import web
from application import models
import settings


async def create_user(request):
    try:
        data = await request.json()
        user = models.ApiUser.create(**data)
        settings.logger.info(f"User created: {user.id}")
        return web.json_response({'user_id': user.id})
    except Exception as e:
        settings.logger.error(f"Error creating user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def get_user(request):
    try:
        user_id = request.match_info.get('user_id')
        user = models.ApiUser.get_or_none(models.ApiUser.id == user_id)
        if user:
            return web.json_response({'name': user.name, 'email': user.email})
        else:
            return web.json_response({'error': 'User not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error fetching user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def update_user(request):
    try:
        user_id = request.match_info.get('user_id')
        data = await request.json()
        query = models.ApiUser.update(**data).where(models.ApiUser.id == user_id)
        if query.execute():
            settings.logger.info(f"User updated: {user_id}")
            return web.json_response({'status': 'User updated'})
        else:
            return web.json_response({'error': 'User not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error updating user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def delete_user(request):
    try:
        user_id = request.match_info.get('user_id')
        query = models.ApiUser.delete().where(models.ApiUser.id == user_id)
        if query.execute():
            settings.logger.info(f"User deleted: {user_id}")
            return web.json_response({'status': 'User deleted'})
        else:
            return web.json_response({'error': 'User not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error deleting user: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def list_users(request):
    try:
        users = list(models.ApiUser.select().dicts())
        return web.json_response(users)
    except Exception as e:
        settings.logger.error(f"Error listing users: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def create_device(request):
    try:
        data = await request.json()
        device = models.Device.create(**data)
        settings.logger.info(f"Device created: {device.id}")
        return web.json_response({'device_id': device.id})
    except Exception as e:
        settings.logger.error(f"Error creating device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def get_device(request):
    try:
        device_id = request.match_info.get('device_id')
        device = models.Device.get_or_none(models.Device.id == device_id)
        if device:
            return web.json_response({
                'name': device.name, 'type': device.type, 'login': device.login,
                'password': device.password, 'location_id': device.location.id,
                'api_user_id': device.api_user.id
            })
        else:
            return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error fetching device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def update_device(request):
    try:
        device_id = request.match_info.get('device_id')
        data = await request.json()
        query = models.Device.update(**data).where(models.Device.id == device_id)
        if query.execute():
            settings.logger.info(f"Device updated: {device_id}")
            return web.json_response({'status': 'Device updated'})
        else:
            return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error updating device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def delete_device(request):
    try:
        device_id = request.match_info.get('device_id')
        query = models.Device.delete().where(models.Device.id == device_id)
        if query.execute():
            settings.logger.info(f"Device deleted: {device_id}")
            return web.json_response({'status': 'Device deleted'})
        else:
            return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error deleting device: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def list_devices(request):
    try:
        devices = list(models.Device.select().dicts())
        return web.json_response(devices)
    except Exception as e:
        settings.logger.error(f"Error listing devices: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def create_location(request):
    try:
        data = await request.json()
        location = models.Location.create(**data)
        settings.logger.info(f"Location created: {location.id}")
        return web.json_response({'location_id': location.id})
    except Exception as e:
        settings.logger.error(f"Error creating location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def get_location(request):
    try:
        location_id = request.match_info.get('location_id')
        location = models.Location.get_or_none(models.Location.id == location_id)
        if location:
            return web.json_response({'name': location.name})
        else:
            return web.json_response({'error': 'Location not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error fetching location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def update_location(request):
    try:
        location_id = request.match_info.get('location_id')
        data = await request.json()
        query = models.Location.update(**data).where(models.Location.id == location_id)
        if query.execute():
            settings.logger.info(f"Location updated: {location_id}")
            return web.json_response({'status': 'Location updated'})
        else:
            return web.json_response({'error': 'Location not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error updating location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def delete_location(request):
    try:
        location_id = request.match_info.get('location_id')
        query = models.Location.delete().where(models.Location.id == location_id)
        if query.execute():
            settings.logger.info(f"Location deleted: {location_id}")
            return web.json_response({'status': 'Location deleted'})
        else:
            return web.json_response({'error': 'Location not found'}, status=404)
    except Exception as e:
        settings.logger.error(f"Error deleting location: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)


async def list_locations(request):
    try:
        locations = list(models.Location.select().dicts())
        return web.json_response(locations)
    except Exception as e:
        settings.logger.error(f"Error listing locations: {str(e)}")
        return web.json_response({'error': str(e)}, status=500)
