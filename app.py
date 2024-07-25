from application.models import BaseModel, create_tables, db as database
from application import handlers
from aiohttp import web
import settings


def create_app():
    settings.setup_logging()
    current_connection = create_tables(database, BaseModel)
    app = web.Application()
    app.add_routes([
        # Users
        web.post('/users', handlers.create_user),
        web.get('/users', handlers.list_users),
        web.get('/users/{user_id}', handlers.get_user),
        web.put('/users/{user_id}', handlers.update_user),
        web.delete('/users/{user_id}', handlers.delete_user),
        # Devices
        web.post('/devices', handlers.create_device),
        web.get('/devices', handlers.list_devices),
        web.get('/devices/{device_id}', handlers.get_device),
        web.put('/devices/{device_id}', handlers.update_device),
        web.delete('/devices/{device_id}', handlers.delete_device),
        # Locations
        web.post('/locations', handlers.create_location),
        web.get('/locations', handlers.list_locations),
        web.get('/locations/{location_id}', handlers.get_location),
        web.put('/locations/{location_id}', handlers.update_location),
        web.delete('/locations/{location_id}', handlers.delete_location),
    ])
    return app, current_connection


if __name__ == '__main__':
    app, db = create_app()
    try:
        web.run_app(app, host='0.0.0.0', port=8000)
    except Exception as e:
        settings.logger.info(f"Program stopped. Error: {e}")
        db.close()
 