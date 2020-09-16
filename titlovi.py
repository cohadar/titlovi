import sys


def main():
    with open(sys.argv[1], 'rb') as f:
        data = bytearray(f.read())
        mapper = {}
        mapper[138] = 'Š'
        mapper[142] = 'Ž'
        mapper[154] = 'š'
        mapper[158] = 'ž'
        mapper[200] = 'Č'
        mapper[230] = 'ć'
        mapper[232] = 'č'
        mapper[240] = 'đ'
        mapper[150] = '*'
        out = ""
        for c in data:
            if c < 128:
                out += chr(c)
            elif c in mapper:
                out += mapper[c]
            else:
                raise ValueError(c)
                out += '?'+str(c)
        print(out)


if __name__ == '__main__':
    main()
