import datetime

def printtime(context):
    print(str(datetime.datetime.now().time())[0:8],context)