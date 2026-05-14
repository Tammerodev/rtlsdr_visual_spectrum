from rtlsdr import *

sdr = RtlSdr()

def configRTL(bw, gain):
    # config
    sdr.sample_rate = bw * 1e6 # 2.4 MHz bandwidth
    sdr.gain = gain