FILEPATH = "todos.txt"


def read_file(file_path=FILEPATH):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_file(todos_local, file_path=FILEPATH):
    with open(file_path, "w") as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print("Running functions.py file")
