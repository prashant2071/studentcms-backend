import redis
# //6379
r = redis.Redis(host='127.0.0.1',port="6379")
r.set("student1_name","ram")
name = r.get("student1_name")
print(name)

name = r.get("student2_name")
print(name)
