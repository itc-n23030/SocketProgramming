import socket

def sen(sock,msg):
    sent_len=0
    msg_len=len(msg)
    while sent_len < msg_len:
        s_len=sock.send(msg[sent_len:])
        if s_len==0:
            raise RuntimeError("socket connection broken")
        sent_len+=s_len

def rec(sock,c_len=1024):
    while True:
        r_chunk=sock.recv(c_len)
        if len(r_chunk)==0:
            break
        yield r_chunk

def main(ip,port):
    c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c_socket.connect((ip,port))
    r_text="GET / HTTP/1.1\r\n\r\n"
    r_bytes=r_text.encode("utf-8")
    sen(c_socket,r_bytes)
    re_bytes=b"".join(rec(c_socket))
    re_text=re_bytes.decode("utf-8")
    print(re_text)
    c_socket.close()


if __name__=="__main__":
    ip,port=input().split(":")
    main()

