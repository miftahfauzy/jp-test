from japronto import Application, RouteNotFoundException

from employeeAPI import *

api = Application()

router = api.router

# Employee Router
# list
router.add_route("/employee/list", EmployeeResource.list_employee, method="GET")
router.add_route("/employee/{id}", EmployeeResource.get_employee, method="GET")


api.run(port=8000)