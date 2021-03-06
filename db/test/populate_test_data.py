from urllib.parse import urlencode
from urllib.request import Request, urlopen
import csv
import json

# This will HTTP POST to the node.js app

# PORT 3000 is used by node.js app connected to carpool DB.
# For testing purposes, setup your own node.js in your home directory and use a different port
BASE_URL = 'http://127.0.0.1:3031'

driverValues = {
      'DriverCollectionZIP' : 0,
      'DriverCollectionRadius' : 0,
      'AvailableDriveTimesJSON' : [],
      'DriverCanLoadRiderWithWheelchair' : False,
      'SeatCount' : 0,
      'DriverHasInsurance' : True,
      'VehicleRegistrationNumber' : 'VEHREG123',
      'DriverFirstName' : 'FIRST',
      'DriverLastName' : 'DRIVER',
      'PermissionCanRunBackgroundCheck' : True,
      'DriverEmail' : 'driver@email.com',
      'DriverPhone' : '555-555-5555',
      'DrivingOnBehalfOfOrganization' : False,
      'DrivingOBOOrganizationName' : 'none',
      'RidersCanSeeDriverDetails' : False,
      'DriverWillNotTalkPolitics' : True,
      'PleaseStayInTouch' : True
      }

url = BASE_URL + '/driver'
with open('carpool_test_databank_driver.csv', newline='\n') as csvfile:
    driver_reader = csv.reader(csvfile, delimiter=',')
    row_idx = 0
    for row in driver_reader:
        if row_idx > 0:
            driverValues['DriverLastName']=row[0]
            driverValues['DriverCollectionZIP']=row[1]
            driverValues['DriverCollectionRadius']=row[2]
            driverValues['SeatCount']=row[3]
            if row[4] == 'T':
                driverValues['DriverCanLoadRiderWithWheelchair']=True
            else:
                driverValues['DriverCanLoadRiderWithWheelchair']=False
            driverValues['AvailableDriveTimesJSON'] = row[5]
            #ride_times = row[5].split('|')
            #times_arr = []
            #for a_time in ride_times:
            #    times_arr.append(a_time)

            #driverValues['AvailableDriveTimesJSON'] = json.dumps(times_arr)
            data = urlencode(driverValues).encode("utf-8")
            req = Request(url, data)
            response = urlopen(req)
            the_page = response.read().decode("utf-8")
            print (the_page)
        row_idx += 1


riderValues = {
      'RiderFirstName' : 'FIRST',
      'RiderLastName' : 'RIDER',
      'RiderEmail' : 'rider@email.com',
      'RiderPhone' : '555-555-5555',
      'RiderVotingState' : 'DC',
      'RiderCollectionZIP' : 0,
      'RiderDropOffZIP' : 0,
      'AvailableRideTimesJSON' : [],
      'NeedWheelchair' : False,
      'RiderAccommodationNotes' : '',
      'TotalPartySize' : 0,
      'TwoWayTripNeeded' : False,
      'RiderPreferredContactMethod' : 'Email',
      'RiderIsVulnerable' : False,
      'DriverCanContactRider' : False,
      'RiderWillNotTalkPolitics' : True,
      'RiderLegalConsent' : True, 
      'PleaseStayInTouch' : True
      }


url = BASE_URL + '/rider'
with open('carpool_test_databank_rider.csv', newline='\n') as csvfile:
    rider_reader = csv.reader(csvfile, delimiter=',')
    row_idx = 0
    for row in rider_reader:
        if row_idx > 0:
            riderValues['RiderLastName']=row[0]
            riderValues['RiderCollectionZIP']=row[1]
            riderValues['RiderDropOffZIP']=row[2]
            riderValues['TotalPartySize']=row[3]
            if row[4] == 'T':
                riderValues['NeedWheelchair']=True
            else:
                riderValues['NeedWheelchair']=False
            #ride_times = row[5].split('|')
            #times_arr = []
            #for a_time in ride_times:
            #    times_arr.append(a_time)
            #riderValues['AvailableRideTimesJSON'] = json.dumps(times_arr)
            riderValues['AvailableRideTimesJSON'] = row[5]
            data = urlencode(riderValues).encode("utf-8")
            req = Request(url, data)
            response = urlopen(req)
            the_page = response.read().decode("utf-8")
            print (the_page)
        row_idx += 1


