from socket import *  
      
s = socket(AF_INET,SOCK_STREAM)  
s.bind(('', 3333))  
s.listen(5)  
print('waiting...')  

while True:  
    client, addr = s.accept()  
    print('connection from', addr)  
    
    while True:  
        data = client.recv(1024)
        
        if not data:  
            break

        try:
            A, operator, B = data.decode().split()
            if operator == '+':
                answer = int(A) + int(B)
            elif operator == '-':
                answer = int(A) - int(B)
            elif operator == '*':
                answer = int(A) * int(B)
            elif operator == '/':
                answer = round(float(A) / float(B), 1)
        except:
            client.send(b'Try again')
        else:
            client.send(str(answer).encode())            

    client.close()