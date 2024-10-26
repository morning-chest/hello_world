
import numpy as np
import ctypes
import socket
import struct
from ctypes import *

import time

# FSR = 20

# class MCPSEND(Structure):
#     _pack_ = 1   #让结构体内存连续
#     _fields_ = [("data", c_ubyte * 8)]

# class MCPRECV(Structure):
#     _pack_ = 1   #让结构体内存连续
#     _fields_ = [("data", c_ubyte * 16)]
    
# class DATA(Structure):
#     _pack_ = 1   #让结构体内存连续
#     _fields_ = [("channel", c_ushort),
#                 ("value", c_double)]

# channel_num = 25
# voltage_0 = 0    
# channels = np.arange(1, channel_num + 1)
# voltage_status = np.array((channels, voltage_0* np.linspace(1, 1, channel_num)))
# for i in channels:
#     # mcpsend = lib.makeSetProtocol(i, voltage_status[1, i- 1], FSR)
#     # sender_socket.sendto(mcpsend, receiver_address)
#     print("Channel {:} set to {:} V".format(i, voltage_status[1, i- 1]))
# print(voltage_status)

#     # 定值电压
# # channel_stable = []
# # for i in channel_stable:
#     # mcpsend = lib.makeSetProtocol(channels[i - 1], voltage_0, FSR)
#     # sender_socket.sendto(mcpsend, receiver_address)

#     # sinusoidal变化电压
# channel_sin = 5
# a_sin = 3
# np.set_printoptions(precision=3)
# r = np.linspace(0, np.pi*2, 20)
# voltage_ratio = np.sin(r)
# for i in np.arange(1,21):
#     voltage_status[1, channel_sin - 1] = a_sin * voltage_ratio[i-1] + voltage_0
#         # print("Channel {:} set to {:} V".format(voltage_status[1, channel_sin- 1], i))
#     print(voltage_status)
#     # mcpsend = lib.makeSetProtocol(channel_sin, voltage_status[1, channel_sin- 1], FSR)
#     #     # makeSetProtocol(channel, A, FSR)
#     #     # FSR = 20, Voltage = A-10
#     # sender_socket.sendto(mcpsend, receiver_address)
#     time.sleep(0.5)   

channel_sin = 7
linear = np.arange(2,6,0.05)
print(linear)
for i in range(1, 80):
    voltage_source.set_voltage(channel=channel_sin - 1, voltage=np.arange[i -1])
    time.sleep(1)
    tagger_data = counter.getData()
    print("TimeTagger Data: ", tagger_data[0].sum())