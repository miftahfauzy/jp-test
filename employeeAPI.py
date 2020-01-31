import json
from json.decoder import JSONDecodeError
from japronto import Application, RouteNotFoundException

from employee import *

class EmployeeResource:
    def list_employee(request):
        employees = EmployeeService.list()
        if len(employees) != 0:
            output = {"status": "Success", "http status": 200, "employees": employees}
        else:
            output = {
                "status": "No record found!",
                "http status": 200,
                "exception": str(exceptions),
                "employees": employees,
            }
        return request.Response(json=output)


    def get_employee(request):
        employee_id = int(request.match_dict["id"])
        employee = EmployeeService.get(employee_id)
        if len(employee) != 0:
            output = {"status": "Success", "http status": 200, "employee": employee}
        else:
            output = {
                "status": "No record found!",
                "http status": 200,
                "employee": "None",
            }
        return request.Response(json=output)


    def get_employeebyfirstname(request):
        employee_firstname = request.match_dict["first_name"]
        employee = EmployeeService.getbyfirstname(employee_firstname)
        if len(employee) != 0:
            output = {"status": "Success", "http status": 200, "employee": employee}
        else:
            output = {
                "status": "No record found!",
                "http status": 200,
                "employee": "None",
            }
        return request.Response(json=output)

    def get_employeebylastname(request):
        employee_lastname = request.match_dict["last_name"]
        employee = EmployeeService.getbylastname(employee_lastname)
        if len(employee) != 0:
            output = {"status": "Success", "http status": 200, "employee": employee}
        else:
            output = {
                "status": "No record found!",
                "http status": 200,
                "employee": "None",
            }
        return request.Response(json=output)

    def create_employee(request):
        try:
            vemployee = request.json
        except JSONDecodeError as jsonerror:
            output = {
                "status": "Error: 400 Bad Request",
                "description": "Empty/incomplete on request body, A valid JSON document is required!",
                "http status": 400,
            }
            return request.Response(code=400, json=output)

        except ValueError as ve:
            output = {
                "status": "Error: 400 Bad Request",
                "description": str(ve),
                "http status": 400,
            }
            return request.Response(code=400, json=output)

        employee = {}
        output = {}
        try:
            employee = EmployeeService.create(vemployee)
            return request.Response(code=201, json=employee)
        except KeyError as error:
            output = {
                "status": "Error: 400 Bad Request",
                "description": str(error),
                "http status": 400,
                "employee": employee,
            }
            return request.Response(code=400, json=output)

        
        