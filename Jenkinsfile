pipeline {
  agent { docker { image 'python:3.7.2' } }
  environment {HOME = '/tmp'} 
  stages {
    // First stage , get files from your GitHub repository.
    stage('Git'){
        steps{
            checkout scm
        }
    }
    stage('preperation') {
      steps {
        sh 'pip install --user --no-cache-dir -r requirements.txt '
      }
    }
    stage('test') {
      steps {
        sh 'python tests.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}
