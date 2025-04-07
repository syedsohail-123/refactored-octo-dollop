pipeline {
    agent any

    stages {
        stage('Run bool.py') {
            steps {
                bat 'python bool.py'  // use `sh` if you're on Linux
            }
        }
    }
}

