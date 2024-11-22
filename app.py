import os

def read_readme():
    file_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print('Contents of README.md:\n', content)
    except Exception as e:
        print(f'Error reading the file: {e}')

if __name__ == "__main__":
    read_readme()