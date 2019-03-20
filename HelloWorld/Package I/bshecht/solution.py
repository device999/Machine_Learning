import datetime

def date_time():
    now = datetime.datetime.now()
    print ("Current date - time: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    date_time()
    

if __name__=="__main__":
    main()


