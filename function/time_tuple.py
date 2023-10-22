
import  datetime

current_time = datetime.datetime.now()
print(current_time)

struct_time_obj = (current_time.timetuple())
print(struct_time_obj[0])
print(struct_time_obj[1])
print(struct_time_obj[2])
print(struct_time_obj[3])
print(struct_time_obj[4])
print(struct_time_obj[5])
print(struct_time_obj[6])
print(struct_time_obj[7])
print(struct_time_obj[8])