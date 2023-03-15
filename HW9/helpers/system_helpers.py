import json


def get_file_data():
    file = open("database/employees.json", "r")
    data_list = json.loads(file.read())
    file.close()
    return data_list

def save_list_to_file(data, path):
    file = open("database/employees.json", "w")
    data_in_json = json.dumps(data)
    file.write(data_in_json)
    file.close()

def save_to_file(data: dict):
    data_list = get_file_data()
    data_list.append(data)
    file = open("database/employees.json", "w")
    data_in_json = json.dumps(data_list)
    file.write(data_in_json)
    file.close()

# def update_file(data, phone):
#     data_list = get_file_data()
#     phone = []
#     for i in data_list:
#         if phone not in data_list:
#             data_list.append(i)
#     save_list_to_file(data_list, "database/employees.json")



