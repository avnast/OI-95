pipeline {

  agent any

  environment {
    EB_APP='OI-95'
    EB_ENV='oi95-env'
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
        zip zipFile:EB_APP+'.zip'
        sh 'printenv'
        sh 'aws s3 cp $EB_APP.zip s3://oi-86/$EB_APP.zip'
        sh 'aws elasticbeanstalk create-application-version --application-name $EB_APP --version-label $BUILD_TAG --source-bundle S3Bucket=oi-86,S3Key=$EB_APP.zip'
        sh 'aws elasticbeanstalk update-environment --environment-name $EB_ENV --application-name $EB_APP --version-label $BUILD_TAG'
      }
    }

  }

  post {
    always {
        deleteDir()
    }
  }

}

