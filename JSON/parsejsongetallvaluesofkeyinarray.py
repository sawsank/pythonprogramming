import json

sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList1 = [item.get('color') for item in data]
dataList2 = [item.get('name') for item in data]
dataList3 = [item.get('id') for item in data]


print(dataList1)
print(dataList2)
print(dataList3)