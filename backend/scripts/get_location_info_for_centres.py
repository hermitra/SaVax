#!/usr/bin/env python3
import pandas
import csv
import os
import json
import traceback
import typing
import requests
import numpy

def read_main(file_name: str) -> typing.Dict:
    '''
    :param file_name:
    :return:

    '''

    try:
        main_excel_file = pandas.ExcelFile(file_name)
        dict_to_return = {}
        dict_to_return['hospital_hubs'] = pandas.read_excel(main_excel_file,'Hospital hubs')
        dict_to_return['local_vaccination_services'] = pandas.read_excel(main_excel_file,'Local vaccination services')
        dict_to_return['pharmacies'] = pandas.read_excel(main_excel_file,'Pharmacies')
        dict_to_return['vaccination_centres'] = pandas.read_excel(main_excel_file,'Vaccination centres')

        return dict_to_return
    except IOError as i:
        print(traceback.format_exc())

    return None


def send_query(base_call_string: str, api_key: str, data_frame: pandas.DataFrame):
    df = pandas.DataFrame()
    try:
        for index, vaccination_centre in data_frame.iterrows():
            address = vaccination_centre['Name of Site'].replace(' ','+')
            if isinstance(address, str):
                counter = 0
                try:
                    output_json = requests.post(base_call_string.format(address=address, api_key=api_key)).json()
                    for entry in output_json['results']:
                        for component in entry['address_components']:
                            if 'types' in component and 'postal_code' in component['types']:
                                vaccination_centre['postal_code'] = component['short_name']
                                print(component['short_name'])
                                vaccination_centre['postal_code'] = component['short_name']
                        vaccination_centre['latitude'] = entry['geometry']['location']['lat']
                        vaccination_centre['longitude'] = entry['geometry']['location']['lng']

                        new_entry = pandas.DataFrame({
                            'region':vaccination_centre['Region'],
                            'ccg':vaccination_centre['CCG'],
                            'name':vaccination_centre['Name of Site'],
                            'postal_code':vaccination_centre['postal_code'],
                            'latitude':vaccination_centre['latitude'],
                            'longitude':vaccination_centre['longitude']
                        }, index=[counter])
                        df = df.append(new_entry)
                        counter+=1
                except Exception as e:
                    print(e)

        return df
    except Exception as e:
        print(e)




if __name__=="__main__":

    try:
        main_dictionary = read_main('vaccination-sites-22-january-2021.xlsx')
        api_key = os.environ['GOOGLE_GEOCODE_KEY']
        base_call_string = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}+United+Kingdom&key={api_key}'

        for key, value in main_dictionary.items():
            if key=='local_vaccination_services':
                data_frame = send_query(base_call_string=base_call_string, api_key=api_key, data_frame=value)
                data_frame.to_csv('out.csv', mode='w', index=False)



    except Exception as e:
        print(traceback.format_exc())

