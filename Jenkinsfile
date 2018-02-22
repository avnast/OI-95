pipeline {

  agent any

  environment {
    APP=''
    AWS_ACCESS_KEY_ID=credentials("aws-key-id")
    AWS_SECRET_ACCESS_KEY=credentials("aws-key")
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    disableConcurrentBuilds()
  }

  stages {

    stage('zip') {
      steps {
        zip zipFile:APP+'.zip'
        sh 'printenv'
        sh 'aws elasticbeanstalk create-application-version --application-name $APP --version-label $BUILD_TAG --source-bundle $APP.zip'
      }
    }

  }

  post {
    always {
        deleteDir()
    }
  }

}

