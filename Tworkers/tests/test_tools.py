import unittest
from unittest.mock import patch
import os
import sys

# Adjust path to make sibling modules importable
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from agent.tools.shell_tools import generate_shell_script
from agent.tools.website_tools import generate_static_website
from agent.tools.notification_tools import send_telegram_notification

class TestTools(unittest.TestCase):

    def setUp(self):
        """Set up test environment before each test."""
        os.makedirs("Tworkers/scripts", exist_ok=True)
        os.makedirs("Tworkers/websites", exist_ok=True)
        with open("Tworkers/config.json", "w") as f:
            f.write('{"gemini_api_key": "TEST_KEY", "telegram_api_key": "YOUR_TELEGRAM_API_KEY", "x_api_key": "YOUR_X_API_KEY"}')

    @patch('agent.tools.shell_tools.LlmAgent')
    def test_shell_script_tool(self, MockLlmAgent):
        """Test the shell script generation tool with a mocked LLM."""
        # Configure the mock
        mock_instance = MockLlmAgent.return_value
        mock_instance.infer.return_value = "#!/bin/bash\necho 'Mocked script'"

        filename = "test_script.sh"
        filepath = f"Tworkers/scripts/{filename}"
        if os.path.exists(filepath):
            os.remove(filepath)

        result = generate_shell_script(task="update packages", filename=filename)
        self.assertIn("Successfully generated", result)
        self.assertTrue(os.path.exists(filepath))

        # Verify the content was written
        with open(filepath, 'r') as f:
            content = f.read()
        self.assertIn("Mocked script", content)

        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass

    @patch('agent.tools.website_tools.LlmAgent')
    def test_website_generation_tool(self, MockLlmAgent):
        """Test the website generation tool with a mocked LLM."""
        # Configure the mock
        mock_instance = MockLlmAgent.return_value
        mock_instance.infer.return_value = "<!doctype html><html><body>Mocked Website</body></html>"

        dirname = "test-site"
        filepath = f"Tworkers/websites/{dirname}/index.html"
        site_dir = os.path.dirname(filepath)
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(site_dir):
            os.rmdir(site_dir)

        result = generate_static_website(description="a test site", dirname=dirname)
        self.assertIn("Successfully generated", result)
        self.assertTrue(os.path.exists(filepath))

        # Verify the content was written
        with open(filepath, 'r') as f:
            content = f.read()
        self.assertIn("Mocked Website", content)

        try:
            os.remove(filepath)
            os.rmdir(site_dir)
        except FileNotFoundError:
            pass

    def test_telegram_notification_tool_no_key(self):
        """Test Telegram tool when API key is a placeholder."""
        result = send_telegram_notification(message="test message", chat_id="12345")
        self.assertIn("Error: Telegram API key not configured", result)

if __name__ == '__main__':
    unittest.main()
