pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                cd blue_team
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Download Logs') {
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

        stage('Run Detection') {
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
            echo 'Pipeline failed!'
        }
    }
}
