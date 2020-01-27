from elections.helpers import ocd_ids_helper, generate_api_url
# import api_response_fixture

state = 'MA'
city =  'Wayland'
def test_ocd_ids_helper():
    results = ocd_ids_helper(state, city)
    assert len(results) == 2
    assert results[0] == 'ocd-division/country:us/state:ma'
    assert results[1] == 'ocd-division/country:us/state:ma/place:wayland'

def test_generate_api_url():
    input = ocd_ids_helper(state, city)
    result = generate_api_url(input)
    expected = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland'
    assert result == expected

def test_parse_response():
    # ran out of time but I would test this function using the api_response_fixture.txt file
    pass