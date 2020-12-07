# To fetch packets
import socket
# To unpack packets
import struct
# For text formatting
import textwrap

# Different TAB levels for formatting purposes
T1="\t"
T2="\t\t"
T3="\t\t\t"
T4="\t\t\t\t"
T5="\t\t\t\t\t"

# Function containing the main code of the Sniffer
def main():
    Connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        # 65535 is the biggest buffer that we can get
        RawData, Addr = Connection.recvfrom(65535)
        DestMacAddr, SrcMacAddr, EthernetProtocol, Data = UnpackEthernetFrame(RawData)

        print(T1+"[ Ethernet Frame ]")
        print(T1+"Source      : "+SrcMacAddr)
        print(T1+"Destination : "+DestMacAddr)
        print(T1+"EthernetProtocol    : "+str(EthernetProtocol)+"\n")

        # 8 -> IPv4
        if EthernetProtocol == 8:
            version, HeaderLength, TTL, IPv4Protocol, src, target, Data = UnpackIPv4Packet(Data)
            print(T2+"[ IPv4 Packet ]")

            print(T2+"Version     : "+str(version))
            print(T2+"Source      : "+src)
            print(T2+"Destination : "+target)   
            print(T2+"HLength     : "+str(HeaderLength))
            print(T2+"TTL         : "+str(TTL))
            print(T2+"IPv4Protocol    : "+str(EthernetProtocol)+"\n")

            # ICMP Packet
            if IPv4Protocol == 1:
                icmp_type, code, checksum, Data = UnpackICMPPacket(Data)
                print(T3+"[ ICMP Packet ]")

                print(T3+"Type     : "+icmp_type)
                print(T3+"Code     : "+code)
                print(T3+"Checksum : "+checksum)

                print(T3+"Data : ")
                print(format_multi_line(T4, Data))

            # TCP Packet
            elif IPv4Protocol == 6:
                SrcPort, DestPort, Sequence, Acknowledgement, flags_urg, flags_ack, flags_psh, flags_rst, flags_syn, flags_fin, Data = UnpackTCPPacket(Data)
                print(T3+"[ TCP Packet ]")
                print(T3+"Source Port      : "+str(SrcPort))
                print(T3+"Destination Port : "+str(DestPort))
                print(T3+"Flags : ")

                print(T3+"    SYNCHRONIZE     : "+str(flags_syn))
                print(T3+"    Acknowledgement : "+str(flags_ack))
                print(T3+"    URGENT          : "+str(flags_urg))
                print(T3+"    PUSH            : "+str(flags_psh))
                print(T3+"    RESET           : "+str(flags_rst))
                print(T3+"    FINISH          : "+str(flags_fin)+"\n")

                print(T3+"Data : ")
                print(format_multi_line(T4, Data))

            # UDP Packet
            elif IPv4Protocol == 17:
                SrcPort, DestPort, length, Data = udp_segment(Data)
                print(T3+"[ UDP Packet ]")
                print(T3+"Source Port      : "+str(SrcPort))
                print(T3+"Destination Port : "+str(DestPort))
                print(T3+"Length           : "+str(length))

                print(T3+"Data : ")
                print(format_multi_line(T4, Data))
                
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Unpack Ethernet Frame
def UnpackEthernetFrame(Data):
    DestMacAddr, SrcMacAddr, EthernetProtocol = struct.unpack('! 6s 6s H', Data[:14])
    return GetMacAddr(DestMacAddr), GetMacAddr(SrcMacAddr), socket.htons(EthernetProtocol), Data[14:]

# Return properly formatted MAC address, i.e. AA:BB:CC:DD:EE:FF
def GetMacAddr(BytesAddress):
    BytesString = map('{:02x}'.format, BytesAddress)
    MacAddr = ':'.join(BytesString).upper()
    return MacAddr

# Unpacks IPv4 packet
def UnpackIPv4Packet(Data):
    VersionAndHeaderLength = Data[0]
    Version = VersionAndHeaderLength >> 4
    HeaderLength = (VersionAndHeaderLength & 15) * 4
    TTL, IPv4Protocol, SrcAddr, DestAddr = struct.unpack('! 8x B B 2x 4s 4s', Data[:20])
    return Version, HeaderLength, TTL, IPv4Protocol, GetIPv4Addr(SrcAddr), GetIPv4Addr(DestAddr), Data[HeaderLength:]

# Return properly formatted IPv4 address
def GetIPv4Addr(BytesAddress):
    return '.'.join(map(str, BytesAddress))

# Unpacks ICMP Packet
def UnpackICMPPacket(Data):
    ICMPType, Code, Checksum = struct.unpack('! B B H', Data[:4])
    return ICMPType, Code, Checksum, Data[4:]

# Unpacks TCP Segment
def UnpackTCPPacket(Data):
    SrcPort, DestPort, Sequence, Acknowledgement, OffsetAndReservedBitsAndFlags = struct.unpack('! H H L L H', Data[:14])
    Offset = (OffsetAndReservedBitsAndFlags >> 12) * 4
    flags_urg = (OffsetAndReservedBitsAndFlags & 32) >> 5
    flags_ack = (OffsetAndReservedBitsAndFlags & 16) >> 4
    flags_psh = (OffsetAndReservedBitsAndFlags & 8) >> 3
    flags_rst = (OffsetAndReservedBitsAndFlags & 4) >> 2
    flags_syn = (OffsetAndReservedBitsAndFlags & 2) >> 1
    flags_fin = OffsetAndReservedBitsAndFlags & 1
    return SrcPort, DestPort, Sequence, Acknowledgement, flags_urg, flags_ack, flags_psh, flags_rst, flags_syn, flags_fin, Data[Offset:]

# Unpacks UDP Segment
def udp_segment(Data):
    SrcPort, DestPort, size = struct.unpack('! H H 2x H', Data[:8])
    return SrcPort, DestPort, size, Data[8:]

# Formats Multi-Line Data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'{:02x} '.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

main()
