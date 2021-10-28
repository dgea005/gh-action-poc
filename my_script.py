##
import pathlib

def write_file_using_inputs():
    current_dir = pathlib.Path(__file__).parent
    with open(current_dir/"templates/my_file.txt", "w") as f:
        f.write("test")


if __name__ == "__main__":
    write_file_using_inputs()
