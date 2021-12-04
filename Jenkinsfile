pipeline {
    agent any
    stages {
        stage('install docker'){
            steps(
                sh 'sudo apt-get update'
                sh 'sudo appt install curl -y'
                sh 'curl https://get.docker.com | sudo bash'
                sh 'sudo apt update'
                sh 'sudo apt install curl -y jq'
                sh 'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s) -$(uname -m)" -o /usr/local/bin/docker-compose'
            )
        }
        // stage('Run unit tests') {
        //     steps {
        //         sh "bash test.sh"
        //     }
        // }

        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_username')
                DOCKER_PWORD = credentials('docker_password')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i /ansible/roles/inventory.yaml /ansible/roles/playbook.yaml"
            }
        }
    }
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'frontend/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'service2/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'service3/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'service4/coverage.xml', failNoReports: false
        }
    }
}