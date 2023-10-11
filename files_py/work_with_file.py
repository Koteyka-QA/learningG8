# Маємо такий словник:
# test_dict = {
#     'user1': {'gender': 'm',
#               'firstname': 'Vasya',
#               'lastname': 'Pupkin',
#               'age': 20},
#     'user2': {'gender': 'f',
#               'firstname': 'Vasilisa',
#               'lastname': 'Pupkina',
#               'age': 21}
# }
# Завдання XML:
#  Завдання 1: Збереження словника у форматі XML: Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml".
#  Завдання 2: Читання XML-файлу: Відкрийте XML-файл та розпарсіть його, щоб отримати знову словник Python як оригінал.
# task1
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}
root = ET.Element("users")
for key, value in test_dict.items():
    user_element = ET.SubElement(root, "user", id=key)
    for attr, val in value.items():
        ET.SubElement(user_element, attr).text = str(val)

tree = ET.ElementTree(root)
tree.write("users.xml")
# task2

import xml.etree.ElementTree as ET

tree = ET.parse("users.xml")
root = tree.getroot()
parsed_dict = {}
for user_element in root.findall("user"):
    user_id = user_element.get("id")
    user_data = {}
    for elem in user_element:
        user_data[elem.tag] = elem.text
    parsed_dict[user_id] = user_data
print(parsed_dict)

# Завдання JSON:
# Завдання 3: Збереження словника у форматі JSON: Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json".
# Завдання 4: Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.
# task3:
import json
test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}
with open("users.json", "w") as json_file:
    json.dump(test_dict, json_file)
# task4

import json
with open("users.json", "r") as json_file:
    loated_dict = json.load(json_file)
print(loated_dict)
# task5 Ковертація з XML в JSON

import xml.etree.ElementTree as ET
import json
tree = ET.parse("users.xml")
root = tree.getroot()
parsed_dict = {}
for user_element in root.findall("user"):
    user_id = user_element.get("id")
    user_data = {}
    for elem in user_element:
        user_data[elem.tag] = user_data
# Saving in Json format
with open("users_from_xml.json", "w") as json_file:
    json.dump(parsed_dict, json_file)
