node {
    stage ("checkout") {
        dir ("checkout"){
            checkout ([
                        $class: 'GitSCM',
                        branches: scm.branches,
                        extensions: [
                                [$class: 'PruneStaleBranch'],
                                [$class: 'CleanCheckout']
                        ],
                        userRemoteConfigs: scm.userRemoteConfigs
                        ])
        }
    }

    stage("running tests") {
        bat "py -3 -m venv venv"
        bat """
            venv\\Scripts\\activate.bat
            pip install -r checkout\\requirements.txt
            """
        dir ("checkout") {
            bat """
                ..\\venv\\Scripts\\activate.bat
                nosetests -v --with-xunit --xunit-file=test-result.xml tests
            """

            junit "test-result.xml"
        }
    }
}