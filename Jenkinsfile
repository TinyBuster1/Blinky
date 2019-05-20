    
pipeline {
    agent { docker { image 'shurikg/python-pyodbc:3.7.3' } }
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
            sh 'python UnitTest.py'
        
      }
    }
  }
}
