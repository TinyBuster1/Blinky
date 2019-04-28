pipeline {
  agent { docker { image 'zerogjoe/mssql-python3.6-pyodbc' } }
  environment {HOME = '/tmp'
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
        sh 'pip install  --user --upgrade pip'
        sh 'pip install --user --upgrade pip wheel'
        sh 'pip install --user --no-cache-dir -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh """
          cd ${WORKSPACE}
          /usr/bin/python3 UnitTest.py
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
