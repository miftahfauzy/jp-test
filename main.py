from japronto import Application, RouteNotFoundException

from employeeAPI import *

api = Application()

router = api.router

# Product Router
router.add_route("/employee/list", EmployeeResource.list_employee, method="GET")


api.run(port=8000)