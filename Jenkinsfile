pipeline {

  agent any

  environment {
    APP='OI-95'
    AWS_ACCESS_KEY_ID=credentials("aws-key-id")
    AWS_SECRET_ACCESS_KEY=credentials("aws-key")
    AWS_DEFAULT_REGION='us-west-2'
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
        sh 'aws s3 cp $APP.zip s3://oi-86/$APP.zip'
        sh 'aws elasticbeanstalk create-application-version --application-name $APP --version-label $BUILD_TAG --source-bundle S3Bucket=oi-86,S3Key=$APP.zip'
      }
    }

  }

  post {
    always {
        deleteDir()
    }
  }

}

