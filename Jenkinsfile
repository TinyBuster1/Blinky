pipeline {
  agent { docker { image 'python:2.7.15' } }
  environment {HOME = '/tmp'
               VIRTUAL_ENV = "${env.WORKSPACE}/venv"} 
  }
  stages {
    // First stage , get files from your GitHub repository.
    stage('Git'){
        steps{
            checkout scm
        }
    }
    stage('build') {
      steps {
        sh' pip install --upgrade pip'
        sh 'pip install -r requirements.txt -r dev-requirements.txt'
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
