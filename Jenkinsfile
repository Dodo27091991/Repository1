pipeline{
    agent any
    stages{
        stage("Clone"){
            checkout scm
        }

        stage("Build"){
            echo "Building image"
        }

        stage("Test"){
            echo "Testing Image"
        }

        stage("Deploy"){
            echo "Deploying image"
        }

    }
}