pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        DOCKER_IMAGE = "deepikagowda123/calc-k8s-demo"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/deepgowda123/calc-k8s-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    echo "Pushing Docker image to DockerHub..."
                    bat "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                }
            }
        }
    }
}
