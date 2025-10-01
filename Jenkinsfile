pipeline {
    agent any

    environment {
        IMAGE_NAME = "mythirdimage"
        IMAGE_TAG = "latest"
        REGISTRY = "docker.io/omarsa999"
        SONARQUBE = "sonar-server"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/OMAR300927/My-Third-project'
            }
        }

        stage('Test') {
            steps {
                dir('myapp') {
                    bat 'python -m pip install --upgrade pip'
                    bat 'pip install -r requirements.txt'
                    bat 'pytest --maxfail=1 --disable-warnings -q --cov=. --cov-report=xml:coverage.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('myapp') {
                    bat "docker build -t %REGISTRY%/%IMAGE_NAME%:%IMAGE_TAG% ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'omarsa999', 
                                                 usernameVariable: 'DOCKER_USER', 
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    
                    bat "docker push %REGISTRY%/%IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    dir('myapp') {
                        bat "sonar-scanner -Dsonar.projectKey=myapp -Dsonar.sources=. -Dsonar.python.coverage.reportPaths=coverage.xml"
                    }
                }
            }
        }

        stage('Apply Kubernetes') {
            steps {
                withKubeConfig([credentialsId: 'Kubeconfig']) { 
                    bat "kubectl apply -f ./k8s/"
                }
            }
        }
    }
}
