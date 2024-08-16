# How to Copy Files from Host Environment to Container Environment

## Creating a Docker Container

To create a Docker container, use the following command:

```
docker create -it --name mypython python
```

Here "mypython" is container name.
"python" is image name (Here python which is official Python Docker image)

Link for Python official Docker image : https://hub.docker.com/_/python


**Notes** 
1. Remove a Docker image:

```
docker rmi <image_name>
```
In this case, the image name is "python".

```
docker rmi python
```

2. To list down all the containers

```
docker ps -a
```
   
## Option 1: Directly Copying Files from host system to container

1. Use the following command to copy files from the host to the container.

```
docker cp myfirst.py mypython:/tmp/myfirst.py
```

2. Checking the Copied File
   
To start the container and check if the file was copied successfully, run:

```
docker start -i mypython
```

You will get the Python command line terminal.
```
import os

os.listdir('/tmp')
exec(open('/tmp/myfirst.py').read())

exit()
```
3. Make Changes to the File on host system.

4. After making changes to the file on the host, copy the updated version to the container.

```
docker cp myfirst.py mypython:/tmp/myfirst.v2.py
```

5. Check the Updated File
Start the container and check the updated file:

```
docker start -i mypython
```

```
import os

os.listdir('/tmp')
exec(open('/tmp/myfirst.v2.py').read())

exit()
```

6. Removing the Container

```
docker rm mypython
```
*Note: The Docker image will still be available after removing the container.*

## Option 2: Mounting Host Folder to Container (Bind Mount)

**Running a Container with a Bind Mount**
You can mount a host folder to the container using below command:

```
docker run -v <host_folder>:<container_folder>
```

For examples:

```
docker run -it -v ${PWD}:/app python
```
```
docker run -d -v ${PWD}/data:/data python
```

Here "python" is the image name.

##### Way 1: Creating a Container First and Then Executing

1. Create the container.

```
docker create -it --name mypython python
```
2. Run the container with the bind mount.

```
docker run -it -v ${PWD}:/app python
```
3. Test the mounted folder inside the container.

```
import os

# Check if all the files from host folder is present inside container or not.
   
os.listdir('/app')


exec(open('/app/myfirst.py').read())

# Now, make changes on the host code and see if they are reflected in the container. You can do it iteratively by executing the above line to test it.

# To exit the Python Command line shell
exit()
```

4. Remove the container:

```
docker rm mypython
```

##### Way 2: Directly Creating and Executing a Container

**Example 1: Create and start the container in one command**

1. Execute the below command.
```
docker run -it --name mypython -v ${PWD}:/app python
```
2. Test the mounted folders inside the container

```
import os

os.listdir('/app')

exec(open('/app/myfirst.py').read())

# Now, make changes on the host code and see if they are reflected in the container. You can do it iteratively by executing the above line to test it.

# To exit the Python Command line shell

exit()

```
3. Remove the container:

```
docker rm mypython
```

**Example 2: Directly run the Python script inside the container:**

1. Execute the below command
```
docker run -it --name my_first_container -v ${PWD}:/app python python /app/myfirst.py
```

2. Make changes in the source code, then start the container:

```
docker start -i my_first_container
```
Changes should be reflected in the container.

3. Remove the container:

```
docker rm my_first_container
```


**Example 3: Run another script inside a new container**

1. Execute the below command
```
docker run -it --name my_second_container -v ${PWD}:/app python python /app/mysecond.py
```
2. Make changes in the source code, then start the container:

```
docker start -i my_second_container
```
Changes should be reflected in the container.

3. Remove the container:

```
docker rm my_second_container
```

**Example 4: Bash Scripting in Container**

Run a Bash shell inside the container:

```
docker run -it --name my_bash_script_container -v ${PWD}:/app python /bin/bash
```
To exit :
```
exit
```