import pymongo
client = pymongo.MongoClient(host='192.168.1.2:27017')
client.admin.authenticate('root', 'root')
rs = client.admin.command('replSetGetStatus')   #replSetGetStatus只能在admin库中使用

print("set:", rs['set'])
print("myState:", rs['myState'])
print("num of members:", len(rs['members']))
