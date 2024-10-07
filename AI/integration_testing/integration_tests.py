
import unittest
import subprocess

class IntegrationTests(unittest.TestCase):

    def test_code_review_assistant(self):
        result = subprocess.run(['python', 'AI/code_review/code_review_assistant.py'], capture_output=True, text=True)
        self.assertIn("Code Review Result", result.stdout, "Code Review Assistant test failed.")

    def test_debugging(self):
        result = subprocess.run(['python', 'AI/debugging/interactive_debugging.py'], capture_output=True, text=True)
        self.assertIn("Debugging Result", result.stdout, "Interactive Debugging test failed.")

    def test_collaboration(self):
        result = subprocess.run(['python', 'AI/collaboration/collaboration_workspace.py'], capture_output=True, text=True)
        self.assertIn("Pair Programming Review Result", result.stdout, "Collaboration Workspace test failed.")

    def test_serverless_deployment(self):
        result = subprocess.run(['python', 'AI/serverless_deployment/serverless_deployment.py'], capture_output=True, text=True)
        self.assertIn("Serverless Deployment Result", result.stdout, "Serverless Deployment test failed.")

if __name__ == "__main__":
    unittest.main()
