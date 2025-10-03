My third demo project: CI/CD pipeline for deploying flask page and monitor it

Build and deploy a flask page using Jenkins, Kubernetes, SonarQube and Prometheus

# Prerequisites

* flask page
* Docker
* Git and GitHub
* Jenkins
* Kubernetes
* SonarQube
* Prometheus

# Steps in the CI/CD pipeline

1. Create a flask page
2. Dockerize the flask page
3. Create a GitHub repository and push code to it
4. Start Jenkins server on a host
5. Start SonarQube container and make a token
6. Use the token to make credential in Jenkins and add SonarQube server
7. Write Jenkins pipeline to build and push the Docker image to Docker and code quality analysis
8. Set up Kubernetes on a host using Minikube
9. Create a Kubernetes deployment and service for the flask page
10. Create a Kubernetes deployment and service for mongoDB as DB for the flask page
11. Create a Kubernetes ingress to expose the flask service externally
12. Create a Kubernetes ServiceMonitor to monitor the flask app by Prometheus
13. Use Jenkins to deploy the Kubernetes cluster

# Project structure

| File                  | Description
|-----------------------|---------------------------------------------------------------------------------------------|
| flask_app.py          |  HTML page which will print "This is my second project" when you run it                     |
| test_app.py           |  Contains unit tests for Flask application using pytest                                     |
| Dockerfile            |  Contains commands to build and run the Docker image                                        |
| Jenkinsfile           |  Contains the pipeline script for build, push, Scan and deploy                              |
| flask.yaml            |  Kubernetes deployment and service file for the flask page                                  |
| flask-secret.yaml     |  Kubernetes secret file                                                                     |
| flask-configmap.yaml  |  Kubernetes configmap file                                                                  |
| mongoDB.yaml          |  Kubernetes deployment and service file for mongoDB                                         |
| flask-ingress.yaml    |  Kubernetes ingress to expose the flask service externally                                  |
| serviceMonitor        |  Kubernetes servicemonitor file to monitor the app by Prometheus                            |

# Conclusion

* In this project, I built a very simple CI/CD pipeline using Jenkins, Kubernetes, SonarQube and Prometheus
* Don't forget to use ngrok in terminal and keep the terminal open so you can use the webhook between Jenkins and SonarQube
* I used credentials for Docker Hub, after deploy the application, run `minikube service html-service` to access it in browser
* Or you can use the tunnel by run `minikube tunnel` to access it , But if you use this method, you should also update your hosts file

# Notes

* To make this flask app show the metrics i add prometheus_flask_exporter library and `metrics = PrometheusMetrics(app)` 
* This flask page won't show anything, it's just to test if the secret file work or not by write in terminal this command :
`curl -c cookies.txt -b cookies.txt -X POST http://<NodeIP>:<NodePort>/login -H "Content-Type: application/json" -d '{"username":"admin","password":"admin123"}' && curl -b cookies.txt http://<NodeIP>:<NodePort>/`
* In this project i used the kube-prometheus-stack ( Full Stack ) so the configutarion will be written by Kubernetes CRDs not manually, that's why i used servicemonitor file to monitor the flask app inside the cluster
* If i want to modify Prometheus.yml manually i need to install Prometheus ( not full stack )
