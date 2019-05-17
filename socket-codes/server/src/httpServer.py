import socket;

HOST, PORT = '', 8888;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
s.bind((HOST, PORT));
s.listen(1);
print 'Serving HTTP on port '+PORT+' ...';
while True:
    c, addr = s.accept();
    request = c.recv(1024);
    print request;
    http_response = """"\
HTTP/1.1 200 OK

Hello, World!""";
    c.send(http_response);
    c.close();
