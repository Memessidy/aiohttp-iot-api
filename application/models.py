import peewee
import inspect
import settings

db = peewee.PostgresqlDatabase(database=settings.database_name,
                               user=settings.username,
                               password=settings.password,
                               host=settings.host)


class BaseModel(peewee.Model):
    class Meta:
        database = db


def create_tables(database=db, base_model=BaseModel):
    models = [cls for name, cls in inspect.getmembers(inspect.getmodule(base_model)) if inspect.isclass(cls) and
              issubclass(cls, base_model) and cls is not base_model]
    database.connect()
    database.create_tables(models)
    return database


class ApiUser(BaseModel):
    class Meta:
        db_table = 'api_user'

    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()


class Location(BaseModel):
    name = peewee.CharField()


class Device(BaseModel):
    name = peewee.CharField()
    type = peewee.CharField()
    login = peewee.CharField()
    password = peewee.CharField()
    location = peewee.ForeignKeyField(Location, backref='devices')
    api_user = peewee.ForeignKeyField(ApiUser, backref='devices')


if __name__ == '__main__':
    create_tables(db, BaseModel)
