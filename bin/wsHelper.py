import websocket
import sys
import time
import ssl
from threading import Thread


def on_message(ws, message):
    print(message)
    if message[0:6]=='{"0":{':
       print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")



clientIdent = 'draPenEmuPyth'

toSendStack = []

def stackSend( ob ):
    global toSendStack
    toSendStack.append( ob )

def on_open(ws):
    global toSendStack

    def run(*args):
        global toSendStack
        iterNo = 0
        while True:
            if iterNo == 5:
                print("ws register me:")
                ws.send(f"wsClientIdent:{clientIdent}")

            # send the message, then wait
            # so thread doesn't exit and socket
            # isn't closed
            if len( toSendStack )>0:
                for ob in range(len(toSendStack)):
                    #print(f"wsSendToWSID:3ddziDeb:{toSendStack[0]}")
                    ws.send( f"wsSendToWSID:3ddziDeb:{toSendStack[0]}" )
                    toSendStack.pop(0)

            #print(["w count",len(toSendStack)])
            time.sleep(.3)
            iterNo+=1

        time.sleep(1)
        ws.close()
        print("Thread terminating...")

    Thread(target=run).start()


def wsStart( callOnMsg, wsCI='NotSetIdentDef', host = "ws://localhost:2999/" ):
    global clientIdent
    clientIdent = wsCI
    websocket.enableTrace(False)
    #websocket.enableVerify( False )
    ws = websocket.WebSocketApp(
        host, 
        on_message=callOnMsg, 
        on_error=on_error, 
        on_close=on_close
    )
    ws.on_open = on_open
    


    def run(*args):
        time.sleep(1)
        print("Started WS client ... {}\n\twsClientIdent: {}".format(
            host, wsCI
        ))
        ws.run_forever( sslopt={"cert_reqs": ssl.CERT_NONE} )
        print("Thread terminating...")

    Thread(target=run).start()

    return ws



if __name__ == "__main__":
    #websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "ws://localhost:2999/"
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(
        host, on_message=on_message, on_error=on_error, on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
