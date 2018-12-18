node {
    stage ("checkout") {
        dir ("checkout"){
            git url: "https://github.com/NJAPe/advent-of-code-2018.git"
    }

    stage("running tests") {
        dir ("checkout") {
            bat "nosetests -v --with-xunit --xunit-file=test-result.xml tests"

            junit "test-result.xml"
        }
    }
}