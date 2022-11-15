import os
import json
from os.path import splitext

EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(path_file: str):
    extension = splitext(path_file)[1][1:]
    if extension in EXTENSIONS:
        with open(path_file) as f:
            data = f.read()
            return data, extension


def dict_to_str(dictionary):
    string = ['{']
    dict_keys = dictionary.keys()
    for key in dict_keys:
        sim = str(key) + ' ' + str(dictionary[key])
        string.append(sim)
    string.append('}')
    result = '\n'.join(string)
    return result


def compare(file_1, file_2):
    dict_1 = {}
    dict_2 = {}
    dict_keys_1 = file_1.keys()
    dict_keys_2 = file_2.keys()
    for key in dict_keys_1:
        if key in dict_keys_2:
            if file_1[key] == file_2[key]:
                dict_1[key] = file_1[key]
            else:
                dict_1[key] = file_1[key]
                dict_2[key] = file_2[key]
        else:
            dict_1[key] = file_1[key]
    for key in dict_keys_2:
        dict_2[key] = file_2[key]
    return dict_1, dict_2


def sort(dicts):
    diff = {}
    dict_1 = dicts[0]
    dict_2 = dicts[1]
    dict_keys_1 = sorted(dict_1.keys())
    dict_keys_2 = sorted(dict_2.keys())
    for key in dict_keys_1:
        if key in dict_keys_2 and dict_1[key] == dict_2[key]:
            diff['   ' + key] = dict_1[key]
        else:
            diff[' - ' + key] = dict_1[key]
    for key in dict_keys_2:
        if key in dict_keys_1 and dict_1[key] != dict_2[key]:
            diff[' + ' + key] = dict_2[key]
        if key not in dict_keys_1:
            diff[' + ' + key] = dict_2[key]
    return diff


def parse(data, forma):
    if forma == 'json':
        return json.loads(data)


def generate_diff(path_file1, path_file2):
    data1, format1 = prepare_data(path_file1)
    data2, format2 = prepare_data(path_file2)
    parc_data1 = parse(data1, format1)
    parc_data2 = parse(data2, format2)
    diff = sort(compare(parc_data1, parc_data2))
    return dict_to_str(diff)
