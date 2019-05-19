    
pipeline {
    agent { docker { image  'python' } }
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
     stage('hackathon') {
      steps {
        sh 'python hackathon.py'
      }
      post {
        always {
          sh 'ln -s Existing-file tests/hackathon-unit.xml $WORKSPACE'
          junit 'hackathon-reports/*.xml'
        }
      }
    }
  }
}
