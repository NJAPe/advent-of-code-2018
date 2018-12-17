node {
    stage ("checkout") {
        dir ("checkout"){
            checkout([$class: 'GitSCM',
                branches: [[name: env.BRANCH_NAME]],
                extensions: [[$class: 'CleanCheckout']],
                userRemoteConfigs: [[credentialsId: 'gitHub', url: 'https://github.com/NJAPe/advent-of-code-2018.git']]
            ])
        }
    }

    stage("running tests") {
        dir ("checkout") {
            bat "nosetests -v --with-xunit --xunit-file=test-result.xml tests"

            junit "test-result.xml"
        }
    }
}