from gibela.app import app
from flask_mako import render_template
from flask_security import roles_accepted, current_user, login_required
from sqlalchemy.orm import joinedload

from gibela.models import *


@app.route('/rider')
@login_required
@roles_accepted('rider')
def rider_dashboard():
    form = ()

    return render_template('rider/rider_dashboard.haml',
                           form=form)
