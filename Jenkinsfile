pipeline {
    agent any
    stages{
        stage("Clone"){
            steps{
                checkout scm
            }
        }
        agent { dockerfile = true}
        stage("Build"){
            steps{
                echo "I'm in bulding stage"
                script{
                    def app=docker.build("dodo1:${env.BUILD_ID}")
                }

            }
        }
        
        stage("Test"){
            steps{
                echo "Test the image"
            }
        }

        stage("Deploy"){
            steps{
                echo "Deploying the image"
            }
        }
    }
}
