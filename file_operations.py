import json

from employee import Employee
import xml.etree.ElementTree as ET


def load_employees(xml_name):
    employees = []
    root = ET.fromstring(xml_name)
    employee_elements = root.findall('employee')

    for element in employee_elements:
        email = None
        manager = None

        field_elements = element.findall('field')

        for field in field_elements:
            field_id = field.get('id')
            if field_id == 'email':
                email = field.text
            elif field_id == 'manager':
                manager = field.text

        if email is not None:
            employees.append(Employee(email=email, manager=manager))

    return employees


def read_xml_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {path} doesn't exist.")
        raise
    except IOError as err:
        print(f"Error during reading file: {err}")
        raise


def save_json_to_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
            print("Saved to " + file_path)

    except IOError as e:
        print(f"An Error occurred during writing into json file: {e}")
        raise
