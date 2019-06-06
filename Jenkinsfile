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
        sh 'python Hackaton_2019/Commits.py'

      }
    }
    stage('transperent') {
        steps {
        sh 'python transperent.py'
        sh 'python Hackaton_2019/transperent.py'

      }
    }
    stage('Benchmark') {
        steps {
        sh 'python Benchmark.py'
        sh 'python Hackaton_2019/Benchmark.py'

      }
    }
    stage('Evaluation') {
        steps {
        sh 'python Evaluation.py'
        sh 'python Hackaton_2019/Evaluation.py'

      }
    }
  }
}
