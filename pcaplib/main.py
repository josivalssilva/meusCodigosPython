from pylibpcap.pcap import sniff


for plen, t, buf in sniff("wlp2s0", filters="port 443", count=-1, promisc=1, out_file="pcap.pcap"):
    if plen == 97:
       print("[+]: Payload len=", plen)
       print("[+]: Time", t)
       print("[+]: Payload", buf)
       print("Example:" , int.from_bytes(b'\x00\x01', 'big'))
       #if buf[0] is not None:
       print(int.from_bytes(buf[0:2], 'big'))
  #  print("Content-Type: ", int.from_bytes(r(buf[0]), 'big'))
   
