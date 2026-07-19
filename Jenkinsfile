pipeline {
    agent any

    environment {
        PROJECT = "${WORKSPACE}"
    }

    stages {

        stage('Download CloudTrail Logs') {
            steps {
                sh '''
                cd blue_team
                ./venv/bin/python download_logs.py
                '''
            }
        }

        stage('Parse Logs') {
            steps {
                sh '''
                cd blue_team
                ./venv/bin/python parse_cloudtrail.py
                '''
            }
        }

        stage('Upload to Elasticsearch') {
            steps {
                sh '''
                cd blue_team
                ./venv/bin/python upload_elasticsearch.py
                '''
            }
        }

        stage('Run Detection Engine') {
            steps {
                sh '''
                cd blue_team
                ./venv/bin/python detections.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
