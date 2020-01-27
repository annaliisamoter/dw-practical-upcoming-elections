import json
def ocd_ids_helper(state, city):
    '''helper function for deriving ocd-ids based on state and city'''
    state = state.lower()
    city = city.lower()
    results = []
    base = 'ocd-division/country:us/state:'
    state_ocd = base + state
    city_ocd = state_ocd + '/place:' + city
    results.append(state_ocd)
    results.append(city_ocd)
    return results


def api_url(ocd_ids):
    base = 'https://api.turbovote.org/elections/upcoming?district-divisions='
    ocd_id_state = ocd_ids[0]
    ocd_id_city = ocd_ids[1]
    request = base + ocd_id_state + ',' + ocd_id_city
    return request
