data = [99, "no data", 95, 94, "no data"]
def onlyNum(data):
    newData = [type(item) for item in data]
    print(newData)

onlyNum(data)
