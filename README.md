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
