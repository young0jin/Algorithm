from collections import deque

def solution(bridge_length, weight, truck_weights):
    onBridge = deque([0 for i in range(bridge_length)])
    sumBridge = 0
    truck_weights = deque(truck_weights)
    time = 0 #걸린 총 시간

    while onBridge:
        time += 1
        
        if onBridge[0] != 0:
            sumBridge -= onBridge[0]
        onBridge.popleft()
        
        if truck_weights:
            if sumBridge + truck_weights[0] <= weight:
                onBridge.append(truck_weights[0])
                sumBridge += truck_weights[0]
                truck_weights.popleft()
            else:
                onBridge.append(0)
    
    return time

