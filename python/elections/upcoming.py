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
    """Take in an address from form and make call to turbo vote api.
    Currently only state and city are being used to
    generate ocd-ids per the assignment instructions
    """
    if request.method == 'POST':
        street = request.form.get('street')
        street2 = request.form.get('street-2')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip')
        ocd_ids = helpers.ocd_ids_helper(state, city)

        url = helpers.generate_api_url(ocd_ids)
        r = requests.get(
            url=url,
            headers={'Accept': 'application/json'}
            )
        flash(r.text)
        parsed = helpers.parse_response(r)
        return render_template('election_results.html', parsed=parsed)

    return render_template('address_form.html', states=postal_abbreviations)
