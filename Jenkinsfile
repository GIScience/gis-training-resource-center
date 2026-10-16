pipeline {
    agent { label 'worker' }
    options {
        timeout(time: 30, unit: 'MINUTES')
    }

    environment {
        REPO_NAME = sh(returnStdout: true, script: 'basename `git remote get-url origin` .git').trim()
        VERSION = sh(returnStdout: true, script: 'grep -Po "^version = \\"\\K([^\\"]+)" pyproject.toml').trim()
        LATEST_AUTHOR = sh(returnStdout: true, script: 'git show -s --pretty=%an').trim()
        LATEST_COMMIT_ID = sh(returnStdout: true, script: 'git describe --tags --long  --always').trim()

        PYTEST_TEST_OPTIONS = ' '
        SNAPSHOT_BRANCH_REGEX = /(^main$)/
        RELEASE_REGEX = /^([0-9]+(\.[0-9]+)*)(-(RC|beta-|alpha-)[0-9]+)?$/
        RELEASE_DEPLOY = false
        SNAPSHOT_DEPLOY = false

        DOCKER_IMAGE_NAME = 'repo.heigit.org/heigit/gis-training'
        DOCKER_CREDENTIALS_ID = 'docker-heigit-ci-service'
        DOCKER_REGISTRY_URL = 'https://repo.heigit.org'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo REPO_NAME
                    echo LATEST_AUTHOR
                    echo LATEST_COMMIT_ID

                    echo env.BRANCH_NAME
                    echo env.BUILD_NUMBER
                    echo env.TAG_NAME

                    if (!(VERSION ==~ RELEASE_REGEX || VERSION ==~ /.*-SNAPSHOT$/)) {
                        echo 'Version:'
                        echo VERSION
                        error 'The version declaration is invalid. It is neither a release nor a snapshot.'
                    }
                }
                script {
                    sh 'uv sync --locked --no-editable'
                }
            }
            post {
                failure {
                  rocket_buildfail()
                }
            }
        }

        stage('Build and Deploy Image') {
            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY_URL, DOCKER_CREDENTIALS_ID) {
                        if (env.BRANCH_NAME ==~ SNAPSHOT_BRANCH_REGEX) {
                            sh 'uv version "$VERSION+$LATEST_COMMIT_ID"'
                            dockerImage = docker.build(DOCKER_IMAGE_NAME + ':' + env.BRANCH_NAME)
                            dockerImage.push()
                        }
                        if (VERSION ==~ RELEASE_REGEX && env.TAG_NAME ==~ RELEASE_REGEX) {
                            dockerImage = docker.build(DOCKER_IMAGE_NAME + ':' + VERSION)
                            dockerImage.push()
                            dockerImage.push('latest')
                        }
                    }
                }
            }
        }

        stage('Wrapping Up') {
            steps {
                encourage()
                status_change()
            }
        }
    }
}
