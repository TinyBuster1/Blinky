    
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
    stage('Commits') {
        steps {
        sh 'python Commits.py'
        
      }
    }
    stage('transperent') {
        steps {
        sh 'python transperent.py'
        
      }
    }
    stage('Benchmark') {
        steps {
        sh 'python Benchmark.py'
        
      }
    }
    stage('Evaluation') {
        steps {
        sh 'python Evaluation.py'
        
      }
    }
  }
}
