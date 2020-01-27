import json


def ocd_ids_helper(state, city):
    '''helper function for deriving ocd-ids based on state and city'''
    state = state.lower()
    # in case of a city name with multiple words, split and rejoin
    city_list = city.split(' ')
    city = ''.join(city_list).lower()
    results = []
    base = 'ocd-division/country:us/state:'
    state_ocd = base + state
    city_ocd = state_ocd + '/place:' + city
    results.append(state_ocd)
    results.append(city_ocd)
    return results


def generate_api_url(ocd_ids):
    '''helper function to generate the api url'''
    base = 'https://api.turbovote.org/elections/upcoming?district-divisions='
    ocd_id_state = ocd_ids[0]
    ocd_id_city = ocd_ids[1]
    request = base + ocd_id_state + ',' + ocd_id_city
    return request

def parse_response(response):
    '''helper function to parse the api response into an object.
    Currently only tested on Wayland MA info.
    In the interest of time, only a few pieces of election information have been
    chosen. With more time, I would finesse the information and format.
    '''
    if not response:
        return {}

    results_dict = {}
    response = response.json()
    for result in response:
        election = result['description']
        results_dict['Description'] = election

        date = result['date'][:10] # elections occur on days, so only capture the yr, mo, and day
        results_dict['Date'] = date
        voter_registration_info = result['district-divisions'][0]['voter-registration-methods'][0]['instructions']['registration']
        results_dict['Voter Registration Info'] = voter_registration_info
        polling_place_info = result['polling-place-url']
        results_dict['Polling Place info:'] = polling_place_info
        for method in result['district-divisions'][0]['voting-methods']:
            if method['primary']:
                results_dict['Voting Day Instructions'] = method['instructions']['voting-id']
            if method['type'] == 'early-voting':
                results_dict['Early Voting Starts'] = method['start'][:10]
                results_dict['Early Voting Ends'] = method['end'][:10]

            elif method['type'] == 'by-mail':
                results_dict['Mail-in Ballot Request Deadline'] = method['ballot-request-deadline-received'][:10]
        # TODO: key error for the following fields. Need to figure out why
        # voter_registration_deadline = result['district-divisions'][0]['voter-registration-methods']['instructions']['deadline-online']
        # results_dict['Voter Registration Deadline'] = voter_registration_deadline
        #results_dict['Online Registration url'] = \
            #result['district-divisions'][0]['voter-registration-methods'][0]['instructions']['url']

    return results_dict


