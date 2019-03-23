from flask import Blueprint, render_template

from domopiru.db import get_db

bp = Blueprint('agent', __name__, url_prefix='/agent')

@bp.route('/list')
def index():
    db = get_db()
    agents = db.execute(
        'SELECT id, name, status, created, ip, port'
        ' FROM agent'
        ' ORDER BY created DESC'
        # number of minions by tipe?? (monitors and actuators) nested query!!
    ).fetchall()
    return render_template('agent/index.html', agents=agents)
