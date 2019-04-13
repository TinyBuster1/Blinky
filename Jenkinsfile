pipeline {
  agent { docker { image 'python:2.7.15' } }
  environment {HOME=${env.WORKSPACE}} 
  stages {
    // First stage , get files from your GitHub repository.
    stage('Git'){
        steps{
            checkout scm
        }
    }
    stage('preperation') {
      steps {
        sh 'pip install --user --no-cache-dir -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'UnitTest.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
          cleanup {
                script {clean_up()}
          }
        }
      }
    }
  }
}
