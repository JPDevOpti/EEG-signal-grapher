import mne
import matplotlib.pyplot as plt  
from scipy.signal import detrend
import os
import pandas as pd  # Import pandas for saving data to CSV

# Load the EEG file (replace 'your_file.cnt' with the path to your file)
eeg_file = 'test_signal.cnt'
eeg_data = mne.io.read_raw_cnt(eeg_file, preload=True)

# Choose a channel (e.g., the first channel)
channel_name = eeg_data.ch_names[1]  # Replace with your channel of interest

# Extract data for the chosen channel
data, times = eeg_data[channel_name, :]  # `data` is the signal, `times` is the time vector
data_volts = data * 1e6  # Convert amplitude to µV

# Create the assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Plot the single channel data
plt.figure(figsize=(20, 4))  # Adjust the size as needed
plt.plot(times, data_volts.T)  # Transpose `data_volts` to match dimensions
plt.title(f'EEG Signal: channel {channel_name}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (µV)')  # µV is used in the label
plt.grid(True)

# Save the plot as an image in the assets folder
plt.savefig('assets/eeg_signal.png')  # Save the figure to the 'assets' directory

# Save the signal data to a CSV file in the assets folder
df = pd.DataFrame({'Time (s)': times.flatten(), 'Amplitude (µV)': data_volts.flatten()})
df.to_csv('assets/eeg_signal_data.csv', index=False)  # Save data to 'assets' directory

# Show the plot (optional, can be removed if you only want to save the image)
plt.show()
