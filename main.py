"""TempGame main logic file"""
###### Python Packges ######
import typer
from typing_extensions import Annotated
from cryptography.fernet import Fernet

###### Path Append ######
# sys.path.append("../PyEngine_v2")

###### My Packges ######
# from Libs.json_handler import read_json, append_json
from json_handler import read_json, append_json

app = typer.Typer()


@app.command()
def generate_key(name: Annotated[str, typer.Argument()]):
    """
    Generate a new key

    Arguments:
        name: key file name
    """
    key = Fernet.generate_key()

    with open(name, "wb") as file:
        file.write(key)


@app.command()
def add_record(key_path: Annotated[str, typer.Argument()],
                file_path: Annotated[str, typer.Argument()],
                record_name: Annotated[str, typer.Argument()],
                record: Annotated[str, typer.Argument()]):
    """
    Add a new record

    Arguments:
        key_path: key file path to encrpt data with it
        file_path: file path to save data into it
        data: given data to save
    """
    with open(key_path, "rb") as file:
        key_data = file.read()

    key_obj = Fernet(key_data)
    record_data = {}
    temp_dict = {}

    for data in record.split(","):
        record_key = data.split(":")[0].strip()
        record_value = key_obj.encrypt(data.split(":")[1].strip().encode())
        temp_dict[record_key] = record_value.decode("utf-8")

    record_data[record_name] = temp_dict
    append_json(file_path, record_data)


@app.command()
def show_records(key_path: Annotated[str, typer.Argument()],
                file_path: Annotated[str, typer.Argument()]):
    """
    Display all the given file records

    Arguments:
        key_path: key file path to decrypt data with it
        file_path: file path to display data from it
    """
    with open(key_path, "rb") as file:
        key_data = file.read()

    key_obj = Fernet(key_data)
    json_data = read_json(file_path)

    for record_name, record in json_data.items():
        email = key_obj.decrypt(record["email"].encode()).decode("utf-8")
        password = key_obj.decrypt(record["password"].encode()).decode("utf-8")
        print(f"Record: {record_name}\n")
        print(f"\tEmail: {email}")
        print(f"\tPassword: {password}")
        print("#" * 15)


if __name__ == "__main__":
    app()
