node {
    def app
    stage('Clone repository'){
        checkout scm
    }

    stage('Build image'){
        app=docker.build("dodo27091991/repository1")
    }

    stage ('Test image'){
        app.inside{
            sh 'echo "test passed"'
        }
    }

    stage ('Push image'){
        docker.withRegistry('https://registry.hub.docker.com','docker-credential'){
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}