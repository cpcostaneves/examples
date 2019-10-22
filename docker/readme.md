# Docker Examples

## Docker

Based on Containers
- Packages application and dependencies together into Standardized Units for Development, Shipment and Deployment
- Operating system virtualization. Kernel allows multiple isolated user-space instances (container)
- In contrast to Virtual machines (VMs) : physical hardware virtualization
- Based on Linux kernel features
  - Namespaces : partitions and isolates kernel resources for a set of processes. Names to distinct resources. Examples of resource names: process IDs, hostnames, user IDs, file names
  - Control groups (cgroups) :  Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, files/folders, network shares, hardware devices) of processes in namespaces.
- other names: Zones, partitions, virtual environments, virtual kernel, jails

Why?
- Standardized Units
- Operation system abstraction
- Reduces work to set environment
- Solves dependency issues
- Isolates application and resources

Docker
- Made up of layers of images, binaries packed together into a single package. 
- The base image contains the operating system of the container, which can be different from the OS of the host. This is not the full operating system as on the host, just includes the file system and binaries, not the kernel and hardware control.
- On top of the base image are multiple images, each building a portion of the container.
- Image building done in Layers, each identified by a hash. If a layers changes, only the affected layers are rebuilt.
- Final image is also a layer (final layer), identified by a hash and a top level image

When a container is booted
- the image and its parent images are downloaded from the repo
- the cgroup and namespaces are created, and the image is used to create a virtual environment. From within the container, the files and binaries specified in the image appear to be the only files in the entire machine. Then the container’s main process is started and the container is considered alive.

Image repositories
- Docker has a builin list of image repositories.
- Main repo: docker hub, eg. https://hub.docker.com/_/python
- Defined  name and tag (eg. python, python:latest, python:3.6.5)
- Base images are created using files from a Linux distribution (eg ubuntu, alpine). Files are just copied to image.

Storage
- All data in docker container is non persistent
- Docker Volume or host directory must be mapped for persistent storage

Network
- Virtual network


Docker on non Linux O.S.:
- Uses machine virtualization for Windows

References:
- https://www.freecodecamp.org/news/demystifying-containers-101-a-deep-dive-into-container-technology-for-beginners-d7b60d8511c1/


Working with docker containers:
- docker command
- docker-compose
- Cluster tools, like docker swarm, kubernets

## docker command

### Install

Follow ref: 
- https://docs.docker.com/install/

Using Apt-get
```
sudo apt install -y docker
```

Allow current user to execute (non-root execution)
- Add current user to docker group
```
sudo usermod -a -G docker $USER
```
- Logout and log on using current user


Start docker as a service (enable running at startup). Linux SystemdD:
```
sudo systemctl enable docker
sudo systemctl start docker
```


### Images

P run, imagem repo local antes

Pull an image from remote repository
```
docker pull python:3.6.5
```

Show images
```
docker image list
```

### Run modes

Run command:
Docker run, dados enquanto run se exit perse tudo
Docker run faz pull, create weitabe layer, start

Run modes
- Run detached (-d)
- interactive + tty (output) (-it); - Remove after (-rm)


https://docs.docker.com/engine/reference/run/
https://docs.docker.com/engine/reference/commandline/run/


### Interactive + output


Explicar python entry e o shell

Run as interactive + output
```
docker run -it --rm --name mypython python:3.6.5
```

Add user current (non-root)

As user
Para definir um home temporário:
mkdir -p .home
export HOME=$(pwd)/.home
https://medium.com/redbubble/running-a-docker-container-as-a-non-root-user-7d2e00f8ee15


### Daemon

Detach usar img com web

Note: 
- using postgres image due to entrypoint runs as a daemon (don't return after running)

Run detached -d
```
docker run -d --name mypostgres postgres
```

Show running containers
```
docker ps
```

Show all containers including stopped
```
docker ps --all
```

Commands for a container
-  Can use container id or names


Stop.
```
docker stop mypostgres
```

Start
```
docker start mypostgres
```

Execute commands inside container
```
docker exec -it <CONTAINER_NAME_ID> <COMMAND>
docker exec -it mypostgres ls -la /
```

Execute shell inside container
```
docker exec -it mypostgres bash
```

Copy file from/to container and host
```
docker cp <CONTAINER_NAME_ID>:<CONTAINER_PATH> <LOCAL_PATH>
docker cp <LOCAL_PATH> <CONTAINER_NAME_ID>:<CONTAINER_PATH>
docker cp mypostgres:/usr/lib/os-release .
```


Stop and Remove (if not --rm).
```
docker stop mypostgres
docker rm mypostgres
```

### Settings

Also Most settings can be set in docker image

regular user for security (default is root)

entrypoint and command

Diff 
exec [] exec direto
shell /bin/sh -c ..


Entrypoint pro entrada. Cmd as arguments pentrypoi t e replaced no run p entrypoint. [] Exec direto. Sem sh c
Entrypoin5 sempre e só cmd overwritten. Mas entry pode ser sobre escrito. fazer exemplos com dockrrfile e run p illustrator
Entry vs cmd, exec form , shell form
Run args are passed to rntrypoint
https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
https://docs.docker.com/engine/reference/builder/


Sem entrypoint, cmd vira cmd main. Run passa cmd, p entrypoint --entrypoint

Priv8ledged

network. bridge for inter container communication
Network options, bridge host
exposed ports
Contorno p host acesso (set host)

map volume or folder
map sockets to access resouces (ex. usb)



Set working directory (-w

env vars

log options

Docker restart policy p detach

Resource control dockr

Consyraints on resoutces e linjx capabilities seção a parte. Secao com network e srorage


More complex command:


Rm

Run: pull / start

Docker. Run noniterative docker os docker ls docker kmage ls doxker stop. Doxker rm. Run rm, doxker run faz pull e start

Also: exec, share, copy, ...

Note: take care of version pin (image and depencies installed)

Stop/Rm


docker run -itd ubuntu:xenial /bin/bash 


```
docker run --name testeapi -p 4444:80 -d renatogroffe/apicontagem-sdk-2-2
```



### Creating an Image

Dockerfile
Extending an image .. Build

Example: node + web server.. run and see browser

Dockerfile falar params cmd, label, add,
Metadata

Build context somente o wue precisa pois manda tudo recursi o p docker daemon

Dockerfile varios cnds juntos p i terdependencia layer

How to - using docker-compose

change part and rebuid )only part will be rebuilt)

How to - using docker-compose
Scripts to help..


## Docker compose

Multiple container orchestration. Write settings to YAML file instead of command options.

Great option for Development / test environments.

For production, use Orchestration and Cluster tools:
- Eg. docker swarn, kubernets
- Takes care of all life cycle including service and load balancing


Docker compose app.com.pytjone db. E node com mongo tb

### Install

Install docker-compose, follow ref
- https://docs.docker.com/compose/install/

For Linux
```
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo yum install -y git
```

### Compose file

File reference:
- https://docs.docker.com/compose/compose-file/


Example in...
Ex docker db


### Execution as daemon

docker-compose -f docker/docker-compose.yml up -d --build

Using script



docker-compose vs swarm.
Differnt approaches and some YAML file format changing

# Other tools

Web tools
- Portainer: gerenciando containers Docker via interface Web
