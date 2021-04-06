node{
    def app
    stage("Clone"){
        checkout scm
    }

    stage("Build"){
        docker { image 'node:14-alpine' }
    }

    stage("Test"){
        echo "Test Images"
    }

    stage("Deploy"){
        echo "Deploy Images"
    }
}