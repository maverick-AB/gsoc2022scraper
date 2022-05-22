import csv
import requests

url= 'https://summerofcode.withgoogle.com/api/projects/?role=&program_slug=2022'


with open('gsoc2022.csv','w', encoding='utf-8', newline='') as csv_file:
    field_names = ['Name', 'Organization','Project']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()

    response = requests.get(url=url).json()
    data = response.get("entities").get("projects")
    for ele in data:
        vals = dict()
        vals['Name'] = ele.get("contributor_name")
        vals['Organization'] = ele.get('organization_name')
        vals['Project'] = ele.get("title")
        writer.writerow(vals)