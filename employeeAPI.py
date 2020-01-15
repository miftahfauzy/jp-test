import json
from json.decoder import JSONDecodeError
from japronto import Application, RouteNotFoundException

from employee import *

class EmployeeResource:
    def list_employee(request):
            try:
                employees = EmployeeService.employeelist()
                if len(employees) != 0:
                    output = {"status": "Success", "http status": 200, "employees": employees}
                else:
                    output = {
                        "status": "No record found!",
                        "http status": 200,
                        "exception": str(exceptions),
                        "employees": employees,
                    }
            except exceptions as ex:
                output = {
                    "status": str(ex),
                    "http status": "Server Error",
                    "exception": str(ex),
                    "employees": employees,
                }

            return request.Response(json=output)