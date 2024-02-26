from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Find department by name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')

def find_department_by_id():
    id = input("Find department by ID: ")
    department = Department.find_by_id(id)
    print(department) if department else print(
        f'Department {id} not found')


def create_department():
    name = input("Department Name: ")
    location = input("Department Location: ")
    try:
        department = Department.create(name, location)
        print(f"Department Created: {department}")
    except Exception as exc:
        print("Error creating department: ", exc)



def update_department():
    depo_id = input("Department ID: ")
    if depo := Department.find_by_id(depo_id):
        try:
            name = input("New Name: ")
            depo.name = name
            location = input("New Location: ")
            depo.location = location
            depo.update()
            print(f'Success: {depo}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {depo_id} not found')

def delete_department():
    pass


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass