from app import app, db # define flask application instance
from app.models import Contact

@app.shell_context_processor # pre-import the application instance and arguments provided
def make_shell_context():
    return {'db': db, 'Contact': Contact}