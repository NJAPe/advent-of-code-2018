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
        dir ("checkout") {
            bat "nosetests -v --with-xunit --xunit-file=test-result.xml tests"

            junit "test-result.xml"
        }
    }
}