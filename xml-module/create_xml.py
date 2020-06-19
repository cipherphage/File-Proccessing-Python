import xml.etree.ElementTree as ET 
from xml.etree.ElementTree import Element, ElementTree
from xml.dom.minidom import parseString

def create_employee(name, age, years_with_company=0):
    employee = Element('employee')
    employee.set('name', name)

    age_tag = ET.SubElement(employee, 'age')
    age_tag.text = str(age)

    years_tag = ET.SubElement(employee, "years_with_company")
    years_tag.text = str(years_with_company)

    return employee

employees = [
    {"name": "Kevin Bacon", "age": 61, "years_with_company": 3},
    {"name": "Josh Broline", "age": 52, "years_with_company": 1},
    {"name": "Kim Dickens", "age": 54},
]

root = Element("employees")

for employee in employees:
    employee_tag = create_employee(**employee)
    root.append(employee_tag)

xml_string = ET.tostring(root)
dom = parseString(xml_string)

pretty_xml = dom.toprettyxml(encoding="UTF-8")
with open("employees.xml", "wb") as f:
    f.write(pretty_xml)