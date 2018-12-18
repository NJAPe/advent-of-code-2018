def isPr() {
    env.CHANGE_ID != null
}

node {
    stage ("checkout") {
        dir ("checkout"){
            // github-specific refspec
            def refspec = "+refs/pull/${env.CHANGE_ID}/head:refs/remotes/origin/PR-${env.CHANGE_ID} +refs/heads/master:refs/remotes/origin/master"
            def url = 'https://github.com/orgi/workflow-durable-task-step-plugin.git'

            def extensions = []
            if (isPr()) {
                extensions = [[$class: 'PreBuildMerge', options: [mergeRemote: "refs/remotes/origin", mergeTarget: "PR-${env.CHANGE_ID}"]]]
            }

            checkout([
                $class: 'GitSCM',
                doGenerateSubmoduleConfigurations: false,
                extensions: extensions,
                submoduleCfg: [],
                userRemoteConfigs: [[
                    refspec: refspec,
                    credentialsId: '<your credentials>',
                    url: url
                ]]
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