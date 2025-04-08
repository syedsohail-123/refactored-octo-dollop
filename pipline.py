pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               git 'https://github.com/syedsohail-123/syedsohailahmedpython-repo.git' 
            }
        }
        stage('Build') {
            steps {
                sh 'echo Building...'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying...'
            }
        }
    }
}
