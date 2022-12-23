import smbus
import time


i2c = smbus.SMBus(1)
addr=0x5a # デバイスアドレス


def main():
    while True:
        Atemp = i2c.read_i2c_block_data(addr,0x6,3)
        Otemp1 = i2c.read_i2c_block_data(addr,0x7,3)
        AmbientTemp = ((Atemp[1]*256 + Atemp[0]) *0.02 -273.15) # 外気温
        ObjectTemp1 = ((Otemp1[1]*256 + Otemp1[0]) *0.02 -273.15) # 対象物温度

        print("Ambient Temp:", round(AmbientTemp,2), " Object Temp:", round(ObjectTemp1,2))
        
        time.sleep(1)


if __name__ == '__main__':
    main()