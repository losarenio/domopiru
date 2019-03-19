"DOMOPIRU - v0.001 - 2019-03-16"

import os
from flask import Flask, render_template
from flask_navigation import Navigation

## http://flask.pocoo.org/docs/1.0/
## next: http://flask.pocoo.org/docs/1.0/tutorial/install/

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'domopiru.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/notjetimplemented')
    def notjetimplemented():
        return render_template('notjetimplemented.html')


    # preparing database
    from . import db
    db.init_app(app)

    # adding blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

app = create_app()

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Dashboard', 'notjetimplemented'),
    nav.Item('Monitors', 'notjetimplemented'),
    nav.Item('Actions', 'notjetimplemented'),
    nav.Item('Rules', 'notjetimplemented'),
    nav.Item('Admin', 'notjetimplemented')
])




