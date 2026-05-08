import sys
import os

# Ensure the app module can be found when running from the root dictionary
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run the server on all available interfaces (0.0.0.0) so Docker can expose it
    # Debug is turned off by default for security, but can be enabled for local testing
    app.run(host='0.0.0.0', port=5000, debug=False)
