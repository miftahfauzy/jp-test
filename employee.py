from decimal import Decimal
from datetime import datetime

from pony.converting import str2datetime
from pony.orm import *
from initdb import Employee


db = Database()
db.bind(provider='postgres', user='postgres', password='pgsql', host='192.168.30.94', database='emp')


class EmployeeService:
    @db_session
    def employeelist():
        _emps = Employee.select()
        emps_array = []
        for emp in _emps:
            dict_emp = {
                "id": emp.id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "address1": emp.address1,
                "address2": emp.address2,
                "zipcode": emp.zipcode,
                "city": emp.city,
                "state": emp.state  
            }
            emps_array.append(dict_emp)
        return emps_array



# print(EmployeeService.employeelist())
