import unittest
import os
import sys

# Adjust path to make sibling modules importable
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the functions, not the old classes
from agent.tools.shell_tools import generate_shell_script
from agent.tools.website_tools import generate_static_website
from agent.tools.notification_tools import send_telegram_notification

class TestTools(unittest.TestCase):

    def setUp(self):
        """Set up test environment before each test."""
        # Ensure directories exist
        os.makedirs("Tworkers/scripts", exist_ok=True)
        os.makedirs("Tworkers/websites", exist_ok=True)
        # Create a dummy config for testing
        with open("Tworkers/config.json", "w") as f:
            f.write('{"gemini_api_key": "TEST_KEY", "telegram_api_key": "YOUR_TELEGRAM_API_KEY", "x_api_key": "YOUR_X_API_KEY"}')

    def test_shell_script_tool(self):
        """Test the shell script generation tool."""
        filename = "test_script.sh"
        filepath = f"Tworkers/scripts/{filename}"
        if os.path.exists(filepath):
            os.remove(filepath)

        # Call the function directly
        result = generate_shell_script(task="update packages", filename=filename)
        self.assertIn("Successfully generated", result)
        self.assertTrue(os.path.exists(filepath))
        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass

    def test_website_generation_tool(self):
        """Test the website generation tool."""
        dirname = "test-site"
        filepath = f"Tworkers/websites/{dirname}/index.html"
        site_dir = os.path.dirname(filepath)
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(site_dir):
            os.rmdir(site_dir)

        # Call the function directly
        result = generate_static_website(description="a test site", dirname=dirname)
        self.assertIn("Successfully generated", result)
        self.assertTrue(os.path.exists(filepath))
        try:
            os.remove(filepath)
            os.rmdir(site_dir)
        except FileNotFoundError:
            pass

    def test_telegram_notification_tool_no_key(self):
        """Test Telegram tool when API key is a placeholder."""
        # Call the function directly
        result = send_telegram_notification(message="test message", chat_id="12345")
        self.assertIn("Error: Telegram API key not configured", result)

if __name__ == '__main__':
    unittest.main()
