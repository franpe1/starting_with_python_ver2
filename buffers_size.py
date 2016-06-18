### Input 
speed=float(input("Enter link speed in Gbps: "))
latency=float(input("Enter the expected latency in ms: "))

## Campute
speed=speed * 1000000
speedInBytes = speed / 8
latencyInSeconds = latency / 1000000
buffer = speedInBytes * latencyInSeconds

## Print Result
print("The suggested buffer size is: ",buffer,"KB")
