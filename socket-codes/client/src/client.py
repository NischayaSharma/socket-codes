import socket;
import sys;

try:
    s = socket.socket();
    s.connect(('18.219.110.96',12345));
    while True:
        str = raw_input("S: ");
        s.send(str.encode());
        if(str == "Bye" or str == "bye"):
            break;
        print "N:",s.recv(1024).decode();
    s.close();
except KeyboardInterrupt:
    print "Closing Connection and freeing the port."
    s.close();
    sys.exit();
