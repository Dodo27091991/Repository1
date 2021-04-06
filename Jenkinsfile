node{
    def abc
    stage('Clone'){
        checkout scm
    }

    stage("build"){
        echo "Building the image"
        abc=docker.build("dodo27091991")
    }

    stage("Test"){
        echo "This is a test"
    }

    stage("Deploy"){
        echo "Deployed"
    }
}