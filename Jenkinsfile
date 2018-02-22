pipeline {

  agent any

  environment {
    AWS_ACCESS_KEY_ID=credentials("aws-key-id")
    AWS_SECRET_ACCESS_KEY=credentials("aws-key")
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    disableConcurrentBuilds()
  }

  stages {

    stage('hello') {
      steps {
        echo Hello!
      }
    }

  }

}

