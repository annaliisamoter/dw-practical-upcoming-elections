import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from elections.us_states import postal_abbreviations
import elections.helpers as helpers
bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/search', methods=('GET', 'POST'))
@bp.route('/')
def search():
    """Take in an address."""
    if request.method == 'POST':
        street = request.form.get('street')
        #flash(street)
        street2 = request.form.get('street-2')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip')
        ocd_ids = helpers.ocd_ids_helper(state, city)
        flash(state)
        flash(city)
        flash(ocd_ids)

        url = helpers.api_url(ocd_ids)
        r = requests.get(
            url='https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland',
            headers={'Accept': 'application/json'}
            )
        flash(r.text)
        return render_template('election_results.html', ocd_ids=ocd_ids)

    return render_template('address_form.html', states=postal_abbreviations)
