import numpy as np
import matplotlib.pyplot as plt
from time import gmtime, strftime

import rtl

def remove_block_dc_spike(p, f, width=10):
    cleaned = p.copy()

    center = len(cleaned) // 2

    left = cleaned[center - width]
    right = cleaned[center + width]

    replacement = (left + right) / 2

    cleaned[center - width : center + width] = replacement

    return cleaned

# lo (minimum frequency) to hi (maximum frequency) in MHz.
def readRange(lo, hi, bw):  
    for center_f in np.arange(lo, hi, bw):
        sdr.center_freq = center_f * 1e6
        samples = sdr.read_samples(256*1024)

        Pxx, freqs = plt.psd(
            samples,
            NFFT = 1024,
            Fs = bw,
            Fc = center_f,
            visible = False
        )
        
        Pxx_clean = remove_block_dc_spike(Pxx, freqs)

        block_freqs.append(freqs)
        block_psd_charts.append(10 * np.log10(Pxx_clean))   


def displaySpectrum(lo_str, hi_str, gain):
    lo = int(lo_str)
    hi = int(hi_str)

    BANDWIDTH_MHZ = 2.4
    STEP_MHZ = 2.4

    configRTL(BANDWIDTH_MHZ, int(gain))

    time_start = strftime("%d.%m.%Y %H:%M:%S", gmtime());

    range_lo = lo
    range_hi = hi
    range_span = (range_hi - range_lo)
    range_mid = range_lo + (range_span / 2)

    print(range_span)
    print(range_mid)

    samples = readRange(range_lo, range_hi, STEP_MHZ);

    sdr.close()

    for f, p in zip(block_freqs, block_psd_charts):
        plt.plot(f, p, color="red")

    time_end = strftime("%H:%M:%S", gmtime());

    plt.title("Spectrum " + time_start + " - " + time_end)
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Power (dB)')

    plt.show()