node{
    def app
    stage("Clone"){
        checkout scm
    }

    stage("Build"){
        app = docker.Build("Dodo27091991/Repository1")
    }

    stage("Test"){
        echo "Test Images"
    }

    stage("Deploy"){
        echo "Deploy Images"
    }
}