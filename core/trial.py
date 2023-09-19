data = {
    "name": "John Doe",
    "age": "30",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main Street",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345",
    },
    "full": {"name": "pro"},
    "full_t": [{"name": "pro"}],
    "hobbies": ["Reading", "Hiking", "Cooking"],
    "age": "30",
    "is_student": False,
    "marks": "34",
    "nums": [1, 2, 3, 4],
    "url": "https://xyz.com|https://abc.com",
    "date": "12 sep 2023 kohinara kama",
}

s = 'url | $split("|") | $map_list({"image_url":".value"}) | $join("|")'
s = "address.city"
s = "age + marks"
s = 'hobbies | $join("|")'
s = "hobbies + hobbies"
s = "age + marks + age"
s = "nums[1]+nums[3]"
s = "full+address"
s = 'hobbies | $map_list({"name": .value})'
s = 'address | $map_dict({"key":".key","value":".value"}) | $join("|")'
s = "full_t[contains(@.name,'pro')]"
s = 'name | $split(" ")'
s = '"marks"+marks'
s = 'url | $split("|") | $map_list({"key":"image_url","value"".value"}) | $join("|")'
s = 'date | $split("kohinara") | $get("0")'
s = '$select("age","marks","nums") | $map_dict({"key-.key":"key"})'
s = '$select("age","marks","nums")| $map_list({"hero_age":".value"})'
s = "full_t[0]"


import json

data = open("/home/vamstar/aws-s3-files/bec_20230505T000001.json").read()
data = data.split("\n")[0]
data = json.loads(data)

print(data)
s = 'lots|$eq("lotNumber","2")|$get("0") | $select("lotNumber","lotTitle")| $map_dict({"key":".key","value":".value"})|$join("|")'


from core.main import parse

#
# data = {"data":[{"id":"1","name":"parser"},{"id":"2","name":"pro"},{"id":"3","name":"v1.0"}]}
# s = 'data | $eq("id","1")'


res = parse(data, s)
print(res)


# import time
# st = time.perf_counter()
#
# def run():
#   for _ in range(500):
#     for _ in range(243):
#         res = parse(data,s)
#
#
# run()
# print(time.perf_counter()-st)
