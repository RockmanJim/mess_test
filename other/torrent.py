import binascii


class AnalysisTorrent(object):
    # 仅适用于普通的torrent
    def __init__(self):
        self.colon = bytes(':', encoding='utf_8')
        self.p_colon = 0
        self.p = 0
        self.t_bytes: bytes = b''
        self.t_str: str = ''
        self.len = 0
        self.after_bracket: list = []
        self.keys: list = ['announce', 'info', 'announce-list', 'comment', 'created by', 'creation date', 'name',
                           'pieces', 'piece length', 'files', 'path', 'length']

    def get_length(self) -> int:
        self.p_colon = self.t_bytes.find(self.colon, self.p)
        return int(self.t_bytes[self.p: self.p_colon])

    def check_one_byte(self):
        one_str = chr(self.t_bytes[self.p])
        if one_str.isdigit():
            # get number length
            length = self.get_length()
            self.p = self.p_colon + 1
            # get the str which length is the number
            temp_str = str(self.t_bytes[self.p: self.p + length], encoding='utf_8')
            self.t_str += '"%s"' % temp_str
            if temp_str in self.keys:
                self.t_str += ':'
            else:
                self.t_str += ','
            self.p += length
            # pieces
            if temp_str == 'pieces':
                length_b = self.get_length()
                self.p_colon = self.t_bytes.find(self.colon, self.p)
                temp_16 = self.t_bytes[self.p_colon + 1: self.p + length_b]
                self.t_str += '"%s"' % str(binascii.hexlify(temp_16), encoding='utf-8')
                self.p += length_b
        elif one_str.isalpha():
            if one_str == 'd':
                self.t_str += '{'
                self.after_bracket.append('}')
                self.p += 1
            elif one_str == 'l':
                self.t_str += '['
                self.after_bracket.append('],')
                self.p += 1
            elif one_str == 'i':
                p_e = self.t_bytes.find(bytes('e', encoding='utf-8'), self.p)
                self.t_str += str(int(self.t_bytes[self.p + 1: p_e]))
                self.t_str += ','
                self.p = p_e + 1
            elif one_str == 'e':
                self.t_str += self.after_bracket.pop()
                self.p += 1
        else:
            self.t_str += self.after_bracket.pop()
            self.p += 1

    def run(self):
        try:
            with open('E:\\to_torrent\\最果ての少女トリシア\\最果ての少女トリシア-personal_cut.webm.torrent', 'rb') as f:
                self.t_bytes = f.read()
                self.len = len(self.t_bytes)
                while self.p < self.len:
                    self.check_one_byte()
                    if len(self.after_bracket) == 0:
                        break
        except Exception:
            print('some thing error!')
        finally:
            print(self.len)
            print(self.p)
            print(self.t_str)
            print(eval(self.t_str))


if __name__ == '__main__':
    AnalysisTorrent().run()
