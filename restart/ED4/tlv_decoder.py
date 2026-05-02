class DataPacket:
    def __init__(self,packet_id,data_type,length):
        self.packet_id = packet_id
        self.data_type = data_type
        self.length = length

    def process_packet(self):
        if self.data_type == 'Point Cloud':
            print(f'{self.packet_id}收到點雲資料,{self.length}長度')
        elif self.data_type == 'Target List':
            print(f'{self.packet_id}追蹤到人,{self.length}長度')
        else:
            print(f'錯誤{self.packet_id}')
        
        