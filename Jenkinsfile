pipeline {

  agent any

  environment {
    EB_APP='OI-95'
    EB_ENV='oi95-env'
    S3BUCKET='oi-86'
    AWS_DEFAULT_REGION='us-west-2'
    AWS_ACCESS_KEY_ID=credentials("aws-key-id")
    AWS_SECRET_ACCESS_KEY=credentials("aws-key")
    ZIP_GLOB='src Dockerrun.aws.json'
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    disableConcurrentBuilds()
  }

  stages {

    stage('deploy') {
      steps {
        zip zipFile:EB_APP+'.zip', glob:ZIP_GLOB
        // create bucket if it doesn't exist
        script {
            try {
                sh 'aws s3 mb s3://$S3BUCKET'
            } catch (err) {
                echo err
            }
        }
        sh 'aws s3 cp $EB_APP.zip s3://$S3BUCKET/$EB_APP.zip'
        sh 'aws elasticbeanstalk create-application-version --application-name $EB_APP --version-label $BUILD_TAG --source-bundle S3Bucket=$S3BUCKET,S3Key=$EB_APP.zip'
        sh 'aws elasticbeanstalk update-environment --environment-name $EB_ENV --application-name $EB_APP --version-label $BUILD_TAG'
      }
    }

  }

  post {
    always {
        deleteDir()
        // sleep 10
        sh 'aws s3 rm s3://$S3BUCKET/$EB_APP.zip'
    }
  }

}

