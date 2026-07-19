pipeline {
    agent any

    stages {

        stage('Blue Team - Download Logs') {
            steps {
                sh '''
                cd ~/cloud-red-blue/blue_team
                source venv/bin/activate
                python download_logs.py
                '''
            }
        }

        stage('Parse Logs') {
            steps {
                sh '''
                cd ~/cloud-red-blue/blue_team
                source venv/bin/activate
                python parse_cloudtrail.py
                '''
            }
        }

        stage('Upload to Elasticsearch') {
            steps {
                sh '''
                cd ~/cloud-red-blue/blue_team
                source venv/bin/activate
                python upload_elasticsearch.py
                '''
            }
        }

        stage('Detection Engine') {
            steps {
                sh '''
                cd ~/cloud-red-blue/blue_team
                source venv/bin/activate
                python detections.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Blue Team pipeline completed.'
        }
    }
}
