from japronto import Application, RouteNotFoundException

from employeeAPI import *

api = Application()

router = api.router

# Employee Router
# list
router.add_route("/employee/list", EmployeeResource.list_employee, method="GET")
router.add_route("/employee/id/{id}", EmployeeResource.get_employee, method="GET")
router.add_route("/employee/firstname/{first_name}", EmployeeResource.get_employeebyfirstname, method="GET")
router.add_route("/employee/lastname/{last_name}", EmployeeResource.get_employeebylastname, method="GET")
router.add_route("/employee/create", EmployeeResource.create_employee, method="POST")

api.run(port=8000)