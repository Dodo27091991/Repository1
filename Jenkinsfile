pipeline {
    agent any
    stages{
        stage("Clone"){
            steps{
                checkout scm
            }
        }

        stage("Build"){
            steps{
                echo "I'm in bulding stage"
                docker{
                    docker.build("dodo27091991/dodo1")
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
