import socket;
import sys;
import thread;

try:
    s = socket.socket();
    port = 12345;
    s.bind(('', port));
    s.listen(5);
    i = 0;

    def main(c,numOfThread):
        while True:
            rcvdData = c.recv(1024).decode();
            print "Thread:", numOfThread+1, "S:", rcvdData;
            sendData = raw_input("N: ");
            c.send(sendData.encode());
            if(sendData == "Bye" or sendData == "bye"):
                break;
        c.close();

    while True:
        print "Server Script started";
        c, addr = s.accept();
        print "Socket Up and running with a connection from",addr;
        thread.start_new_thread(main,(c,i,));
        i+=1;

except KeyboardInterrupt:
    print "\nClosing Connection and freeing the port."
    c.close();
    sys.exit();
