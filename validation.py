# Схемы хотела проверять примерно так:
#
# from jsonschema import Draft7Validator
# import json
# with open("C:/Dev/task_backend_developer_november_2020/task_folder/schema/cmarker_created.schema", "r") as read_file:
#     my_schema = json.load(read_file)
#     Draft7Validator.check_schema(my_schema)
#
# Однако возникла следующая проблема: при использовании Draft3Validator неверными оказывались все схемы, а при использовании
# Draft4Validator, Draft6Validator, Draft7Validator ошибки в схемах не находились вовсе. Ни того, ни другого по условию Вашей
# задачи быть не может. В чем причина ошибок я, к сожаленю, так и не поняла.
import os
import json
import jsonschema
from jsonschema import validate


with open("C:/Dev/test_task/schema/cmarker_created.schema", "r") as read_schema:
    schema = json.load(read_schema)
    os.chdir("C:/Dev/test_task/cmarker")
    for filename in os.listdir(os.getcwd()):
        with open(filename, "r") as read_file:
            message = json.load(read_file)
        try:
            v = validate(message, schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)

with open("C:/Dev/test_task/schema/label_selected.schema", "r") as read_schema:
    schema = json.load(read_schema)
    os.chdir("C:/Dev/test_task/label")
    for filename in os.listdir(os.getcwd()):
        with open(filename, "r") as read_file:
            message = json.load(read_file)
        try:
            v = validate(message, schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)

with open("C:/Dev/test_task/schema/sleep_created.schema", "r") as read_schema:
    schema = json.load(read_schema)
    os.chdir("C:/Dev/test_task/sleep")
    for filename in os.listdir(os.getcwd()):
        with open(filename, "r") as read_file:
            message = json.load(read_file)
        try:
            v = validate(message, schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)

with open("C:/Dev/test_task/schema/workout_created.schema", "r") as read_schema:
    schema = json.load(read_schema)
    os.chdir("C:/Dev/test_task/workout")
    for filename in os.listdir(os.getcwd()):
        with open(filename, "r") as read_file:
            message = json.load(read_file)
        try:
            v = validate(message, schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)
