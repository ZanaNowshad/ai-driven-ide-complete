
import unittest
import importlib
import sys
import os

# Adding `AI` module to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

class IntegrationTests(unittest.TestCase):

    def test_code_review_assistant(self):
        try:
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code_review')))
            code_review_module = importlib.import_module('code_review_assistant')
            print("Code Review Assistant executed successfully.")
        except Exception as e:
            self.fail(f"Code Review Assistant test failed: {e}")

    def test_debugging(self):
        try:
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../debugging')))
            debugging_module = importlib.import_module('interactive_debugging')
            print("Interactive Debugging executed successfully.")
        except Exception as e:
            self.fail(f"Interactive Debugging test failed: {e}")

    def test_collaboration(self):
        try:
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../collaboration')))
            collaboration_module = importlib.import_module('collaboration_workspace')
            print("Collaboration Workspace executed successfully.")
        except Exception as e:
            self.fail(f"Collaboration Workspace test failed: {e}")

    def test_serverless_deployment(self):
        try:
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../serverless_deployment')))
            serverless_module = importlib.import_module('serverless_deployment')
            print("Serverless Deployment executed successfully.")
        except Exception as e:
            self.fail(f"Serverless Deployment test failed: {e}")

if __name__ == "__main__":
    unittest.main()
