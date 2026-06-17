// Pipeline declarativo de Jenkins.
// Alternativa a GitHub Actions, común en empresas grandes.
// Actívalo solo cuando ya domines GitHub Actions.

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r backend/requirements.txt'
            }
        }

        stage('Tests') {
            steps {
                dir('backend') {
                    sh 'pytest'
                }
            }
        }

        stage('Build de imagen Docker') {
            steps {
                sh 'docker build -f backend/Dockerfile -t taskflow:latest .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado con éxito.'
        }
        failure {
            echo 'El pipeline falló. Revisa los logs.'
        }
    }
}
