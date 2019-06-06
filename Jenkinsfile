    
pipeline {
    agent { docker { image 'python 3.7.2' } }
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
        dir("Hackaton_2019") {
            sh 'python Commits.py'
        }
        
      }
    }
 
    stage('transperent') {
        steps {
            dir("Hackaton_2019") {
                 sh 'python transperent.py'
            }
        
      }
    }
    stage('Benchmark') {
        steps {
        dir("Hackaton_2019") {
            sh 'python Benchmark.py'
        }
        
      }
    }
    stage('Evaluation') {
        steps {
        dir("Hackaton_2019") {
            sh 'python Evaluation.py'
        }
        
      }
    }
    stage('test') {
        steps {
            sh 'python UnitTest.py
      }
    }
  }
}
