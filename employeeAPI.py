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

                