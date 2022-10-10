import numpy as np
from scipy import fftpack

timestep = 0.05
timevec = np.arange(0, 10, timestep)
period = 5

sig = (np.sin(2*np.pi*timevec/period) + 0.25* np.random.randn(timevec.size) )


sig_fft = fftpack.fft(sig)
Amplitude = np.abs(sig_fft)
Power = Amplitude**2
Angle = np.angle(sig_fft)

sample_freq = fftpack.fftfreq(sig.size, d=timestep)

Amp_freq = np.array([Amplitude, sample_freq])
Amp_position = Amp_freq[0, :].argmax()
peak_freq = Amp_freq[1, Amp_position]

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

print(peak_freq)
print(Amp_position)
print(filtered_sig)
