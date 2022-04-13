
import http.client as client 
import sys



def start(http_server):
    #create a connection
    conn = client.HTTPConnection(http_server)

    #request to server
    conn.request("GET", "/")

    #get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    
    conn.close()


#get http server ip
http_server = sys.argv[1]
start(http_server)
