import unittest
import app

class Flasktest(unittest.TestCase):
      def test_get(self):
          
          test=app.hello_world()
          self.assertEquals(test,"Hello, World!")

if __name__=="__main__":
   unittest.main()
