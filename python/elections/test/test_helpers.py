from elections.helpers import ocd_ids_helper, api_url

state = 'NY'
city =  'Brooklyn'
def test_ocd_ids_helper():
    results = ocd_ids_helper(state, city)
    assert len(results) == 2
    assert results[0] == 'ocd-division/country:us/state:ma'
    assert results[1] == 'ocd-division/country:us/state:ny/place:wayland'

def test_api_url():
    input = ocd_ids_helper(state, city)
    result = api_url(input)
    expected = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland'
    assert result == expected

