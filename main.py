from file_operations import read_xml_file, load_employees, save_json_to_file
from tree_building import build_employee_hierarchy
import sys


try:
    if len(sys.argv) < 2:
        print("Please provide a xml file as a command line argument")
        sys.exit(1)

    file_path = sys.argv[1]

    xml_content = read_xml_file(file_path)
    employees_list = load_employees(xml_content)

    for employee in employees_list:
        print(f'Found new Employee: {employee}')

    hierarchy = build_employee_hierarchy(employees_list)

    save_json_to_file(hierarchy, 'result.json')
    print("Done!")

except Exception as e:
    print(f"Error: {e}")
