1. Create a Readme File - Done
2. Create a Docker Container to run Jenkins - 

```
docker pull jenkins/jenkins:lts - Pull Jenkins Image
docker run -d -p 8080:8080 jenkins/jenkins:lts
``` 

Get the Container ID using 

```
Docker ps
```

Container ID - dd4000ce674f

Access the container to get the jenkins password
```
docker exec -it dd4000ce674f /bin/bash
cd cd /var/jenkins_home/secrets
cat initialAdminPassword
```

Admin password - e04933cccacc437c9728a3b93e5838d2

Login and install the suggested plugin

- Done

3. Create the application and Dockerfile

app.py:
```
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
```

Dockerfile:
```
FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
CMD ["python", "app.py"]
```

Run the docker container:
```
docker build -t readme-printer .
docker run -d --name readme_printer readme-printer
docker logs readme_printer
```

The code and Container is working properly

4. Create a Jenkins Pipeline that

```

```

