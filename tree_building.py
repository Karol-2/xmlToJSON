
def build_json_tree(email, manager_to_reports):
    direct_reports = []
    for report in manager_to_reports.get(email, []):
        direct_reports.append(build_json_tree(report.email, manager_to_reports))

    return {
        "employee": {
            "email": email,
            "direct_reports": direct_reports
        }
    }


def build_employee_hierarchy(list_of_employees):
    manager_to_reports = {}

    for employee in list_of_employees:
        if employee.manager:
            if employee.manager not in manager_to_reports:
                manager_to_reports[employee.manager] = []
            manager_to_reports[employee.manager].append(employee)

    top_level_employees = []
    for employee in list_of_employees:
        if employee.manager is None:
            top_level_employees.append(employee)

    hierarchy = []
    for employee in top_level_employees:
        hierarchy.append(build_json_tree(employee.email, manager_to_reports))

    return hierarchy

