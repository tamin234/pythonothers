initial_hour,initial_minute,final_hour,final_minute=map(int,input().split())

count=0
if initial_hour>final_hour:
    for x in range(initial_hour,24):
        count=count+1
    hour=count+final_hour
    if initial_minute>final_hour:
        count=0
        for x in range(initial_minute,60):
            count=count+1
        tmin=count + final_minute
        print("total time",hour,tmin)
    elif final_minute>initial_minute:
        tmin=final_minute-initial_minute
        print("total time",hour,tmin)
    elif initial_minute==final_minute:
        tmin=60
        print("total time",hour,tmin)
    else:
        tmin=0
        print("total time",hour,tmin)
    
elif initial_hour<final_hour:
    hour=final_hour-initial_hour
    if initial_minute>final_minute:
        count=0
        for x in range(initial_minute,60):
            count=count+1
        tmin=count+final_minute
        print("total time",hour,tmin)
    elif final_minute>initial_minute:
        tmin=final_minute-initial_minute
        print("total time",hour,tmin)
    elif final_minute==initial_minute:
        tmin=60
        print("total time",hour,tmin)
    else:
        tmin=0
        print("total time",hour,tmin)
elif initial_hour==final_hour:
    hour=24
    if initial_minute>final_minute:
        count =0
        for x in range(initial_minute,60):
            count=count+1
        tmin=count+final_minute
        print("total time",hour,tmin)
    elif final_minute>initial_minute:
        tmin=final_minute-initial_minute
        print("total time",hour,tmin)
    elif final_minute==initial_minute:
        tmin=60
        print("total time",hour,tmin)
    else:
        tmin=0
        print("total time",hour,tmin)
else:
    hour=0
    if initial_minute>final_minute:
        count=0
        for x in range(initial_minute,60):
            count=count+1
        tmin=count+final_minute
        
        print("total time",hour,tmin)
    elif final_minute>initial_minute:
        tmin=final_minute-initial_minute
        print("total time",hour,tmin)
    elif final_minute==initial_minute:
        tmin=60
        print("total time",hour,tmin)
    else:
        tmin=0
        print("total time",hour,tmin)
    
    
