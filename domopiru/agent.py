from flask import Blueprint, render_template

from domopiru.db import get_db

bp = Blueprint('agent', __name__)

@bp.route('/')
def index():
    db = get_db()
    agents = db.execute(
        'SELECT id, name, status, createdm, ip, port'
        ' FROM agent'
        ' ORDER BY created DESC'
        # number of minions (monitors and actuators)?
    ).fetchall()
    return render_template('agent/index.html', agents=agents)
