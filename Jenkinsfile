pipeline {
    agent { label 'linux-agent' }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Parallel Build') {
            parallel {

                stage('Build CMake Project') {
                    steps {
                        dir('led-firmware') {
                            sh '''
                                mkdir -p build
                                cd build
                                cmake ..
                                make
                            '''
                        }
                    }
                }

                stage('Build Maven Project') {
                    steps {
                        dir('vehicle-parking') {
                            sh '''
                                mvn clean package
                            '''
                        }
                    }
                }

            }
        }
    }

    post {
        success {
            echo 'Both CMake and Maven builds completed successfully.'
        }

        failure {
            echo 'One or more builds failed.'
        }
    }
}
