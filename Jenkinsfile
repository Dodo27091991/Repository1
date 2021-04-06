node{
    def app
    stage("Clone"){
        checkout scm
    }

    stage("Build"){
        app=docker.build("dodo27091991/dodo1")
    }

    stage("Test"){
        echo "Test Images"
    }

    stage("Deploy"){
        echo "Deploy Images"
    }
}
