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
   pip install -r requirements.txt
            }}
   stage('Test')
      {
         steps{
    python -m test
         } }
   stage('Notification')
      {
         steps
         {
      echo 'This is some notification step'
         } }
   }
}
