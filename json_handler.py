"""Define function to work with json files"""
import json


def read_json(file_path):
    """
    Read Json file data

    Arguments:
        file_path: Given json file path
    """
    with open(file_path) as data:
        json_data = json.load(data)

    return json_data


def write_json(file_path, json_data):
    """
    Write data to json file (overwrite the current data!!)

    Arguments:
        file_path: Given json file path
        json_data: data to write into json file
    """
    with open(file_path, "w") as w:
        json.dump(json_data, w, indent=2)


def append_json(file_path, new_data):
    """
    Append data to json file

    Arguments:
        file_path: Given json file path
        new_data: data to append it
    """
    json_data = read_json(file_path)
    for key, value in new_data.items():
        json_data[key] = value
    write_json(file_path, json_data)
