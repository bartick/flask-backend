from src import app

@app.shell_context_processor
def make_shell_context():
    return {'app': app}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)