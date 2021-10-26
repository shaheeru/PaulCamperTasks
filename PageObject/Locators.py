class Locator(object):

    #Vehicle search filter
    vehicle_filter_button = "//span[@data-test-id='FilterCamperType']"    #XPath

    #Vehicle search Filter - Distance From Location
    distance_input_field = "//input[@class='input__value___3Qh9L form-control']"   #XPath

    #Vehicle search Filter - Body Style
    camper_bus_checkbox = "//div[@data-test-id='CampingBus']"    #css selector

    box_van_checkbox = "//div[@data-test-id='Van']"  #XPath

    alcove_checkbox = "//div[@data-test-id='Alcove']"

    partially_integrated_checkbox = "//div[@data-test-id='SemiIntegrated']"

    integrated_checkbox = "//div[@data-test-id='Integrated']"

    caravan_checkbox = "//div[@data-test-id='Trailer']"

    other_checkbox = "//div[@data-test-id='Other']"

    reset_button = "//div[@data-test-id='reset-button']"
