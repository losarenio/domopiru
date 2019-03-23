from flask import Blueprint, render_template

from domopiru.db import get_db
from domopiru.auth import login_required

bp = Blueprint('agent', __name__)

@bp.route('/list')
@login_required
def index():
    db = get_db()
    agents = db.execute(
        'SELECT id, name, status, createdm, ip, port'
        ' FROM agent'
        ' ORDER BY created DESC'
        # number of minions by tipe?? (monitors and actuators) nested query!!
    ).fetchall()
    return render_template('agent/index.html', agents=agents)
