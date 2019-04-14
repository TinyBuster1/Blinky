pipeline {
  agent { docker { image 'python:2.7.15' } }
  environment {HOME = '/tmp'} 
  stages {
    // First stage , get files from your GitHub repository.
    stage('Git'){
        steps{
            checkout scm
        }
    }
    stage('build') {
      steps {
        sh 'pip install --user --no-cache-dir -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh """
          cd ${WORKSPACE}
          /usr/local/bin/python UnitTest.py
        """
      }
      post {
        always {
           junit 'tests/results/*.xml'
        }
      }
    }
  }
}
