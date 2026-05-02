from tlv_decoder import DataPacket

raw_tlv_stream = [
    {"packet_id": "PKG-001", "data_type": "Point Cloud", "length": 1024},
    {"packet_id": "PKG-002", "data_type": "Target List", "length": 256},
    {"packet_id": "PKG-003", "data_type": "System Log",  "length": 64}
]
for data in raw_tlv_stream:
    packet_id = data['packet_id']
    data_type = data['data_type']
    length = data['length']

    tlv1 = DataPacket(packet_id,data_type,length)
    tlv1.process_packet()
