from flask_debugtoolbar import DebugToolbarExtension
from flask_script import Manager, Shell

from app import create_app, mongo

app = create_app()
toolbar = DebugToolbarExtension(app)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=mongo)


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == "__main__":
    manager.run()
