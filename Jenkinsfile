pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
                echo 'Asignando workspace y validando entorno.'
            }
        }
        stage('Estándar de código') {
            steps {
                sh '''
                # Cambiar al directorio del proyecto
                cd calculadora


                # Activar el entorno virtual
                .    ~/env/bin/activate

                # Ejecutar pruebas
                flake8 .
                '''
            }
        }
        stage('Pruebas unitarias') {
            steps {
                sh '''
                # Cambiar al directorio del proyecto
                cd calculadora


                # Activar el entorno virtual
                .    ~/env/bin/activate

                # Ejecutar pruebas
                python test_calculadora.py
                '''
            }
        }

    }
    post {
       always {
            script {
                if (env.WORKSPACE) {
                    cleanWs()
                } else {
                    echo 'No hay WORKSPACE activo, se omite cleanWs().'
                }
            }
        }
        failure {
            emailext (
                to: 'esme.espino19@gmail.com, amgdark@uaz.edu.mx',
                subject: "¡FALLO en el Pipeline! ${env.JOB_NAME} - Build ${env.BUILD_NUMBER}",
                body: """El pipeline ${env.JOB_NAME} (Build #${env.BUILD_NUMBER}) ha fallado en la etapa: ${env.STAGE_NAME}.
                       Por favor, revisa los logs para identificar la causa del problema: ${env.BUILD_URL}"""
            )
        }
        success {
            emailext (
                to: 'esme.espino19@gmail.com',
                subject: "Pipeline Exitoso: ${env.JOB_NAME} - Build ${env.BUILD_NUMBER}",
                body: "El pipeline ${env.JOB_NAME} (Build #${env.BUILD_NUMBER}) se ha completado exitosamente."
            )
        }
    }
}