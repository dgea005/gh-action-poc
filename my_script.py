##
import pathlib

def main():
    current_dir = pathlib.Path(__file__).parent
    pathlib.Path(current_dir/"templates").mkdir(parents=True, exist_ok=True)
    with open(current_dir/"input/input.txt", "r") as f:
        data = f.read()
    with open(current_dir/"templates/my_file.txt", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
