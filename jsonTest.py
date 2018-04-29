'''
Created on Apr 28, 2018

@author: joclark
'''

if __name__ == '__main__':
    pass

import json
import boto3

with open('data2.json') as f:
    read_data=f.read()
    f.close()


#json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'
 
'''
try:
    decoded = json.loads(read_data)
 
    # Access data
    for x in decoded['persons']:
        print x['name']
 
except (ValueError, KeyError, TypeError):
    print "JSON format error"
'''    

try:
    decoded = json.loads(read_data)
 
    # Access data
    for x in decoded['SecurityGroups']:
        group_Name=x['GroupName']
        if group_Name == 'Travel':
            print x['IpPermissionsEgress']
            for y in x['IpPermissionsEgress']:
                print y.keys()
                print y['IpProtocol']
 
except (ValueError, KeyError, TypeError):
    print "JSON format error"

# Test boto3 connection to AWS s3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
