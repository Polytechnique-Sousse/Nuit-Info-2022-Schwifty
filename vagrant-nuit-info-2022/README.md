# Nuit Info 2022 Schwifty

# Django & react & node & HTML & SCSS & JS & PostgreSQL & mongo ...
Template repository:
* Django and PostgreSQL node back-end
* HTML, CSS, JS, SCSS Front-end
* Docker & kubernetes
* CI/CD Jenkins


# Requirements:
* Python 3.10
* Node 14
* Linux


# Getting started:
## Django back-end
1. Set up a virtual environment for your project.:
```
python3 -m venv env
```

2. Activate the virtual environment:
```
source env/bin/activate
```
3. Install python dependencies:
```
pip install -r app/requirements.txt
```
4. Migrate Djnago database:
```
python app/manage.py migrate
```

## Front-end (HTML, CSS, Js, SASS and NodeJs):
1. Install NPM dependencies:
```
npm -prefix frontend install
```
2. Build the Front-end:
```
npm -prefix frontend run build
```

# Running the app:
## Running dev environment
### Normal installation:
In your dev environment, it's useful to automate your build when there is any change. So you can see the code changes immediately in your browser:

1. This will watch for Front-end code changes:

```
npm -prefix frontend run watch
```


2. Run the app using the built in Django web server. This will make sure that back-end django code are applyed live:
```
python app/manage.py runserver
```

## Development environment optional requirements
* Node and NPM
* Docker and kubernetes
* Linux
* Linux (Recommended if using Docker)


### Docker install:
By using Docker, we don’t have to worry about the installation of the PostgreSQL or pgAdmin.

Same thing with the normal installation, we want our changes applied as we code them:
1. Depending on your docker compose setup run:
```
docker-compose -f docker-compose.dev.yaml up --build
```
Or :
```
docker compose -f docker-compose.dev.yaml up --build
```
2. Finally, Accessing services:
    * Django app: http://127.0.0.1:8080/
    * pgAdmin: http://127.0.0.1:5050/

        EMAIL: root@root.com
        
        PASSWORD: root


## Running production environment
### Docker install:
We need to verify how our application will work in production to achieve this:
1. Depending on your docker compose setup run:
```
docker-compose -f docker-compose.yaml up --build
```
Or :
```
docker compose -f docker-compose.yaml up --build
```
2. Finally, Accessing services:
    * Django app: http://127.0.0.1:8080/




### Docker swarm install:
1. Build the project images:
Depending on your docker compose setup run:

```
docker-compose -f docker-compose.stack.yaml build
```
Or :
```
docker compose -f docker-compose.stack.yaml build
```
2. Push the images to docker hub:
Depending on your docker compose setup run:

```
docker-compose -f docker-compose.stack.yaml push
```
Or :
```
docker compose -f docker-compose.stack.yaml push
```
3. Deploy to docker swarm:

```
docker stack deploy -c docker-compose.stack.yaml django_template
```


### Kubernetes install:
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
minikube start
```

### Kubectl install:
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

1. Build the project images:
Depending on your docker compose setup run:



2. Finally, Accessing services:
    * Django app: http://127.0.0.1:8080/



### Kubectl install:
```
sudo wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
```
sudo apt update && sudo apt install vagrant
```
vagrant plugin install vagrant-docker-compose
```
vagrant up
```