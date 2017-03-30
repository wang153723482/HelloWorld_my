import json

people = '{"name":"wangc","age":12,"pets":[{"name":"coco","type":"dog"},{"name":"jam","type":"cat"}]}'


json_people = json.loads(people)

print json_people['name']
print json_people['pets'][0]  #不用dumps，输出的结果中每一个key和value前都会有一个u
print json.dumps(json_people['pets'][0])
print json_people['pets'][0]["name"]

json_people["age"]=26
print json_people['age']


