import omniture
import os
import json
from datetime import datetime, date, timedelta

creds = {}
creds['username'] = os.environ['OMNITURE_USERNAME']
creds['secret'] = os.environ['OMNITURE_SECRET']
test_report_suite = "royalcaribbeanprod"

data = {
	"accessLevel": "shared",
	"fields": [
		"definition"
	],
	"filters": {
		"name": "Test AeM: Weekly EM Report Launch Date Filter"
	}
}

test = omniture.authenticate({'OMNITURE_USERNAME':creds['username'], 'OMNITURE_SECRET':creds['secret']})
suite = test.suites[test_report_suite]
segments = suite.retrieve_segments(data)
#print(len(segments))
#print(json.dumps(segments, indent=4))

for segment in segments:
	print(segment['id'], segment["name"])
	rules = segment["definition"]['container']['rules']
	for rule in rules:
		d = datetime.strptime(rule['value'], '%m/%d/%Y') + timedelta(days=7)
		rule['value'] = d.strftime("%m/%d/%Y")
	segment["reportSuiteID"] = test_report_suite
	#response =  suite.save_segment(segment)
	#print(response)
