no_zone , req_time , left_time = [ int(x) for x in input().split()]

time_zones = [ int(x) for x in input().split()]
time_zones.sort(reverse = True)
flag = True
for t in time_zones:
	if (left_time + t)>= req_time:
		print("YES")
		flag = False
		break;

if flag : 
	print("NO")
