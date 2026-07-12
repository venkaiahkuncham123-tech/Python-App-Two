pipeline {
    agent any
    environment {
        SONAR_HOME = tool 'python-sonar-scanner'
    }
    parameters {
        choice(name:'BRANCH', choices: ['master','main','ppd','qa'], description: 'Brnach To Clone')
        booleanParam(name:'SONAR', defaultValue: false, description: 'Do you need Sonar Analysis')
        booleanParam(name: 'NEXUS', defaultValue: false, description: 'Do you want to publich artifact')
    }
    stages {
        stage('Git Checkout') {
            steps {
                git branch: "${params.BRANCH}", url: 'https://github.com/venkaiahkuncham123-tech/Python-App-Two.git'            }
        }
         stage('Installing Virtual Environment and dependencies') {
            steps {
                sh '''
                    python -m venv venv \
                    ./venv/bin/pip install -r requirements.txt'''
                    
            }
        }
         stage('Sonaqube Analysis') {
             when {
                 expression { params.SONAR == true }
             }
            steps {
        
        withCredentials([usernamePassword(credentialsId: 'Sonar-Cred-Server', passwordVariable: '', usernameVariable: '')]) {
                sh "${SONAR_HOME}/bin/sonar-scanner -Dsonar.settings=sonar-project.settings"
            
        }
            }
        }
         stage('Articat Publication') {
             when {
                 expression { params.NEXUS == true }
             }
            steps {
                configFileProvider([configFile(fileId: 'python-nexus-config', targetLocation: '.')]) {
                            sh './venv/bin/pip install twine'
            sh './venv/bin/twine upload --config-file .pypirc dist/*'
                            }
            }
                }
                stage('Running Application') {
            steps {
                sh './venv/bin/python run.py'
            }
        }
    }
}
