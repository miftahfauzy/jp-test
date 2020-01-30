from pony.orm import *


db = Database()


class Employee(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Optional(str)
    last_name = Optional(str)
    address1 = Optional(LongStr)
    address2 = Optional(LongStr)
    zipcode = Optional(str)
    city = Optional(str)
    state = Optional(str)


db.bind(provider='postgres', user='postgres', password='pgsql', host='192.168.30.26', database='emp')
db.generate_mapping(create_tables=True)
# set_sql_debug(True)
