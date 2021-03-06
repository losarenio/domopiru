
import logging

from flask import (Blueprint, render_template, flash, url_for, request)
from flask_table import Table, Col, DatetimeCol, NestedTableCol

from domopiru.db import get_db

bp = Blueprint('agent', __name__, url_prefix='/agent')

logger = logging.getLogger('agent')

@bp.route('/index')
def index():
    # logger.debug("request from %s - %s", request.url, request.remote_addr)

    sort = request.args.get('sort', 'id')
    direction = (request.args.get('direction', 'asc') == 'desc')

    logger.info("Query: sort: %s - dir: %s", sort, direction)

    table_agent = get_table_agents(col_key=sort, direction=direction)
    if not table_agent:
        logger.debug("No agents on bbdd")
        flash("No agents connected!!")

    return render_template('agent/index.html', table_agent=table_agent)

def get_table_minions(agent_id):

    db = get_db()
    minions = db.execute(
        'SELECT M.id as id, M.name as name, M.status as status, type, M.created as created'
        ' FROM minion M join '
        '   agent A on (M.agent_id = agent.id)'
        ' Where agent.id = ?'
        ' ORDER BY M.name',
        agent_id).fetchall()

    logger.info("getting %s agents", len(minions))

    minion_list = []
    table_minions = None
    for row in minions:
        logger.info("%s %s %s %s %s",
                    row[0], row[1], row[2], row[3],row[4])
        minion_list.append(ItemMinion(row[0], row[1], row[2], row[3], row[4]))

    table_minions = TableAgent(minion_list)

    return table_minions

def get_table_agents(col_key='created', direction=False):
    _direction = 'asc'
    if direction:
        _direction = 'desc'

    if col_key not in ('id', 'name', 'status', 'created', 'ip', 'port'):
        col_key = 'id'

    db = get_db()
    query = 'SELECT id, name, status, created, ip, port' +\
            ' FROM agent' +\
            ' ORDER BY %s %s' % (col_key, _direction)
    logger.info("Query: %s", query)
    agents = db.execute(query).fetchall()

    logger.info("getting %s agents", len(agents))

    agent_list = []
    table_agents = None
    for row in agents:
        logger.info("%s %s %s %s %s %s",
                    row[0], row[1], row[2], row[3], row[4], row[5])

        agent_list.append(ItemAgent(row[0], row[1], row[2], row[4], row[5],
                                    get_table_minions(row[0])))


    table_agents = TableAgent(agent_list, sort_by=col_key,
                              sort_reverse=direction, border=3)

    return table_agents

class TableMinion(Table):
    allow_sort = False

    _id = Col('id')
    name = Col('name')
    status = Col('status')
    _type = Col('type')

    created = DatetimeCol('created')
class ItemMinion():
    def __init__(self, _id, name, status, _type, created):
        self._id = _id
        self.name = name
        self.status = status
        self.created = created
        self._type = _type

class TableAgent(Table):
    allow_sort = True

    _id = Col('id')
    name = Col('name')
    status = Col('status')
    created = DatetimeCol('created')
    ip = Col('IP')
    port = Col('port')
    minions = NestedTableCol('minions', TableMinion)

    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction =  'desc'
        else:
            direction = 'asc'

        return url_for('agent.index', sort=col_key, direction=direction)

class ItemAgent():
    def __init__(self, _id, name, status, created, ip, port):
        self._id = _id
        self.name = name
        self.status = status
        self.created = created
        self.ip = ip
        self.port = port
