pipeline{
   agent any
   stages
   {
   stage('Checkout')
   {
      steps{
         
   checkout scm
      }}
   stage('Build')
      {
         steps
         {
  sh  pip install -r requirements.txt
            }}
   stage('Test')
      {
         steps{
    sh python -m test
         } }
   stage('Notification')
      {
         steps
         {
     sh  echo 'This is some notification step'
         } }
   }
}
