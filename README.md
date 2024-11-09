# Currency Converter Application
by [SURYA PRAKASH VELLINGIRI]

Welcome to the Currency Converter Application! This project is a simple desktop application to help users convert between various currencies with real-time exchange rates, display current rates, and visualize currency data.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
Before running the application, make sure you have the following tools and libraries installed:

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)
- Requests library (for API requests)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
   pip install requests

4. Run the application:
   python currency_converter.py

## Usage
- Launch the application by running the command above. The graphical interface will open up.
- Select Base Currency: Choose from INR, USD, EUR, or GBP in the dropdown.
- Enter Amount: Input the amount you wish to convert.
- Check Exchange Rates: Click to view the latest exchange rates in a new window.
- Graph View: Visualize conversion rates for selected currencies in a bar graph format.

## Features
- Real-Time Exchange Rates: Utilizes the ExchangeRate-API for up-to-date currency rates.
- Graphical Visualization: View conversion rates as a bar graph.
- Multi-Currency Support: Supports conversions between INR, USD, EUR, and GBP.
- Data Storage: Saves exchange rates in a text file for quick access and offline reference.

- ## Contributing
Contributions to this project are welcome! If you find any issues or have improvements to suggest, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


> **Note**: Replace `yourusername` with your GitHub username and add your name where indicated.
