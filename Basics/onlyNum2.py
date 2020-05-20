data = [99, "no data", 95, 94, "no data"]
def onlyNum(data):
    newData = []
    for i in data:
        if not isinstance(i, str):
            newData.append(i)
    print(newData)

onlyNum(data)
