import os
from flask import jsonify, request, render_template

# In-memory database for simplicity (suitable for a presentation/demo)
notes = [
    {"id": 1, "title": "First Note", "content": "Welcome to the DevSecOps Demo API!"}
]

def init_routes(app):
    @app.route('/metrics', methods=['GET'])
    def get_metrics():
        """Dynamically check files for vulnerabilities to make the dashboard live"""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Check requirements.txt for the requests vulnerability
        req_path = os.path.join(base_dir, 'requirements.txt')
        dep_count = 0
        dep_status = "success"
        dep_message = "Clean"
        
        if os.path.exists(req_path):
            with open(req_path, 'r') as f:
                content = f.read().replace(' ', '')
                if '\nrequests==' in content: # uncommented active vulnerability
                    dep_count = 1
                    dep_status = "danger"
                    dep_message = "Vulnerable Package Found"
                elif '#requests==' in content: # commented vulnerability
                    dep_count = 1
                    dep_status = "warning"
                    dep_message = "Commented Vulnerability"
        
        # Check routes.py for SAST vulnerabilities (exec or SECRET_API_KEY)
        routes_path = os.path.join(base_dir, 'app', 'routes.py')
        sast_count = 0
        sast_status = "success"
        sast_message = "Clean"
        
        if os.path.exists(routes_path):
            with open(routes_path, 'r') as f:
                for line in f.readlines():
                    line = line.strip()
                    # Check if line is not commented out
                    if not line.startswith('#'):
                        if 'exec(' in line or 'SECRET_API_KEY' in line:
                            sast_count += 1
            
            if sast_count > 0:
                sast_status = "danger"
                sast_message = "Vulnerabilities Found"
            elif '# exec(' in open(routes_path, 'r').read():
                sast_count = 2
                sast_status = "warning"
                sast_message = "Intentionally Commented"

        return jsonify({
            "dependency": {
                "count": dep_count,
                "status": dep_status,
                "message": dep_message
            },
            "sast": {
                "count": sast_count,
                "status": sast_status,
                "message": sast_message
            }
        })

    @app.route('/', methods=['GET'])
    def home():
        """Render the main UI"""
        return render_template('index.html')

    @app.route('/api-info', methods=['GET'])
    def api_info():
        """Health check and API info endpoint"""
        return jsonify({
            "status": "online",
            "message": "Welcome to the DevSecOps Notes API!",
            "version": "1.0.0"
        })

    @app.route('/notes', methods=['GET'])
    def get_notes():
        """Retrieve all notes"""
        return jsonify({"notes": notes})

    @app.route('/notes', methods=['POST'])
    def create_note():
        """Create a new note"""
        data = request.get_json()
        
        # Input validation
        if not data or not 'title' in data or not 'content' in data:
            return jsonify({"error": "Missing title or content in the request body"}), 400

        # =========================================================================
        # INTENTIONALLY INSECURE CODE EXAMPLE
        # Commented out for future SAST/Bandit testing demos.
        # Uncommenting this will trigger CWE-798 (Hardcoded Secrets) and CWE-94 (Code Injection)
        # =========================================================================
        # SECRET_API_KEY = "AKIAIOSFODNN7EXAMPLE"
        # user_input = data.get('command', 'print("No command")')
        # exec(user_input)

        new_note = {
            "id": len(notes) + 1,
            "title": data['title'],
            "content": data['content']
        }
        
        notes.append(new_note)
        return jsonify(new_note), 201
