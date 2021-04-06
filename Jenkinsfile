node{
    def app
    stage("Clone"){
        checkout scm
    }

    stage("Build"){
        docker.build("dodo/dodo1")
    }

    stage("Test"){
        echo "Test Images"
    }

    stage("Deploy"){
        echo "Deploy Images"
    }
}
