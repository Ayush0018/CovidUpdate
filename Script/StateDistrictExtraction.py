import json

import requests


class StateDistrictExtraction:

    def __init__(self):
        self.headers_dict = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/90.0.4430.93 Safari/537.36"}

    def extract_state_codes(self):
        state_dump = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states',
                                  headers=self.headers_dict).json()

        with open(r'../Resource/state_codes.json', mode='w') as state_codes_writer:
            json.dump(state_dump, state_codes_writer)

    def extract_district_code(self):
        with open(r'../Resource/state_codes.json', mode='r') as state_codes_reader:
            states_dict = json.load(state_codes_reader)

            with open(r'../Resource/district_codes.json', mode='r+') as district_codes_writer:
                # for self.state_code in range(1, len(self.states_dict['states'])+1):
                district_codes_writer.truncate()
                district_dump = requests.get(
                    'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(str(34)),
                    headers=self.headers_dict).json()
                json.dump(district_dump, district_codes_writer)

    def json_merger(self):
        pass

        # districts = []
        # district_dump_dict = {'districts': []}
        #
        # with open(r'../Resource/state_codes.json', mode='r') as state_codes_reader:
        #     self.states_dict = json.load(state_codes_reader)
        #
        #     with open(r'../Resource/district_codes.json', mode='r+') as district_codes_writer:
        #         #for self.state_code in range(1, len(self.states_dict['states'])+1):
        #             district_dump = requests.get(r'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(str(self.state_code)),headers = self.headers_dict).json()
        #             for x in district_dump['districts']:
        #                 district_dump_dict['districts'].append(x)
        #         #districts.append(district_dump)
        #         json.dump(district_dump_dict, district_codes_writer)

    # def read_data_cowin(self):
    #
    #     if self.user_district is None and self.state is None:
    #         req_avail = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date=31-03-2021'.format)
