# EEG Signal Visualization

This repository provides tools and guidelines for visualizing raw EEG (electroencephalography) data. It focuses on converting raw EEG data into readable and interpretable graphs.

## Theory

### Converting Raw EEG Data to Graphs

Raw EEG data can vary significantly between different equipment, brands, models, and configurations. To effectively study and analyze these signals, they need to be converted into visual formats. This process involves loading EEG data and plotting it to visualize its behavior.

### Loading EEG Signals

EEG signals can be stored in various file formats (.csv, .txt, .m, .cnt). These files may contain additional information such as patient details, equipment specifics, test characteristics, and other relevant metadata. The `mne` library in Python is commonly used to handle and load these different file formats.

### Metadata and Visualization

Before visualizing EEG signals, it is important to understand the internal metadata of the file. Metadata provides essential information like the number of channels, sampling frequency, and channel names, which are crucial for accurate visualization.

### Adjusting Graphs for Better Visualization

When plotting EEG signals, the following parameters can be adjusted to enhance visualization:

- **`n_channels`**: Determines the number of EEG channels displayed in the graph. Adjusting this allows focusing on specific signals.
- **`scalings`**: Controls the scale of data in the graph, enabling amplification or reduction of signal amplitude.
- **`title`**: Sets a title for the graph, providing a descriptive label.
- **`show`**: Indicates whether to display the graph immediately or save it for later use.
- **`time_range`** (Optional): Specifies the time interval of data to include in the graph.
- **`block`** (Optional): Controls how data is grouped for graphical representation.
- **`axes`** (Optional): Allows customization of graph axes, including labels and limits.
- **`color`** (Optional): Defines the color of lines representing EEG signals.
- **`linewidth`** (Optional): Adjusts the thickness of lines in the graph.

### Converting EEG Signals to Vectors

To facilitate processing, EEG signals can be converted into multiple vectors. This involves filtering, removing trends, and segmenting the signal into different channels. This vector format makes it easier to manipulate and analyze the data.

### Saving EEG Signals

Once the EEG signal is visualized and processed, it can be saved. Converting the signal into a DataFrame and storing it in a .csv file allows for easy retrieval and future analysis.

## Requirements

To work with EEG signals and visualize them, ensure you have the following Python packages installed:

- **`mne`**: A library for processing and analyzing EEG, MEG, and other neuroimaging data.
- **`numpy`**: A library for numerical computations and array manipulations.
- **`matplotlib`**: A library for creating static, animated, and interactive visualizations in Python.
- **`pandas`**: A library for data manipulation and analysis, especially for handling CSV files.

You can install these dependencies using pip. Open your terminal or command prompt and run the following command:

```bash
pip install mne numpy matplotlib pandas
