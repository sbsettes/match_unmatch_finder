with open("arguments.txt") as f:
    arguments = f.readlines()

with open("key_points.txt") as f:
    key_points = f.readlines()

if( len(key_points)>len(arguments) ):
    DATA_SIZE = len(arguments)
else:
    DATA_SIZE = len(key_points)

key_points = key_points[:DATA_SIZE]
arguments = arguments[:DATA_SIZE]

for i in range(DATA_SIZE):
    argument_topic = arguments[i].split(",")[-2]
    key_point_topic = key_points[i].split(",")[-2]
    argument_id = arguments[i].split(",")[0]
    key_point_id = key_points[i].split(",")[0]
    print(key_point_id+"|"+argument_id +","+("Matched" if argument_topic == key_point_topic else "Unmatched"))
