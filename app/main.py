import os


def copy_file(command: str) -> None:
    parts = list(command.split())
    if len(parts) < 3:
        return

    if parts[0] != "cp":
        return
    obj1 = parts[1]
    obj2 = parts[2]
    if obj1 == obj2:
        return

    if not os.path.exists(obj1):
        return

    with open(obj1, "r") as file_in, open(obj2, "w") as file_out:
        file_out.write(file_in.read())
