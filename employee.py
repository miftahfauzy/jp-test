import json
from decimal import Decimal
from datetime import datetime

from pony.converting import str2datetime
from pony.orm import *
from initdb import Employee


db = Database()
db.bind(provider='postgres', user='postgres', password='pgsql', host='192.168.30.26', database='emp')
set_sql_debug(True)

class EmployeeService:

    # get all employee
    @db_session
    def list():
        _emps = Employee.select_by_sql("select id, first_name, last_name, address1, address2, zipcode, city, state from employee order by id")
        emps_array = []
        for emp in _emps:
            dict_emp = {
                "id": str(emp.id),
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

    # get employee by ID
    @db_session
    def get(id):
        employee = Employee.get(id=id)
        print(employee)
        if employee == None:
            result = {
                "status": "failed",
                "message": "Employee with id '" + str(id) + "' was not found!"
            }
            return result
        else:
            dict_emp = {
                    "id": employee.id,
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "address1": employee.address1,
                    "address2": employee.address2,
                    "zipcode": employee.zipcode,
                    "city": employee.city,
                    "state": employee.state  
                }
            return dict_emp


    @db_session
    def getbyfirstname(firstname):
        _emps = Employee.select_by_sql("select id, first_name, last_name, address1, address2, zipcode, city, state from employee where first_name = '" + firstname + "' order by id")
        if _emps == None:
            result = {
                "status": "failed",
                "message": "Employee with first_name '" + firstname + "' was not found!"
            }
            return result
        else:
            emps_array = []
            for emp in _emps:
                dict_emp = {
                    "id": str(emp.id),
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

 
    @db_session
    def getbylastname(lastname):
        _emps = Employee.select_by_sql("select id, first_name, last_name, address1, address2, zipcode, city, state from employee where last_name = '" + lastname + "' order by id")
        if _emps == None:
            result = {
                "status": "failed",
                "message": "Employee with last_name '" + lastname + "' was not found!"
            }
            return result
        else:
            emps_array = []
            for emp in _emps:
                dict_emp = {
                    "id": str(emp.id),
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
    
    @db_session
    def create(_employee):
        # parse json variable
        employee_parse = json.loads(json.dumps(_employee))
        employee = Employee(
            first_name=employee_parse["first_name"], 
            last_name=employee_parse["last_name"],
            address1=employee_parse["address1"], 
            address2=employee_parse["address2"],
            zipcode=employee_parse["zipcode"],
            city=employee_parse["city"],
            state=employee_parse["state"])

        result = {
            "status": "success",
            "message": "Success added employee",
            "employee": {
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "address1": employee.address1,
                "address2": employee.address2,
                "zipcode": employee.zipcode,
                "city": employee.city,
                "state": employee.state  
            }
        }
        return result



# Create new Employee
# new_employee = {
#     "first_name": "Miftah",
#     "last_name": "Fauzy",
#     "address1": "Jl. Kel. Margahayu IV No.7",
#     "address2": "RT 007/RW 07, Kelurahan Margahayu, Kecamatan Bekasi Timur",
#     "zipcode": "17113",
#     "city": "Kota Bekasi",
#     "state": "Jawa Barat"
# }

# print(EmployeeService.getbylastname("McKeurtan"))
# print(EmployeeService.getbyfirstname("Suranev"))
# print(EmployeeService.create(new_employee))
# print(EmployeeService.get(0))
# print(EmployeeService.employeelist())
