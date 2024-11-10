# Ethereum Cracker Generator and Checker

This project is an Ethereum wallet generator and checker. It generates Ethereum wallets by creating random mnemonic phrases, derives corresponding private keys and addresses, and checks if any of these addresses have a transaction history or a balance on the Ethereum blockchain. If an address is found with a transaction history or a non-zero balance, it saves the wallet details in a file.

## Features

- **Mnemonic Phrase Generation**: Uses a mnemonic phrase to generate private keys and Ethereum addresses.
- **Address Checking**: Verifies if each generated address has a transaction history or balance using a blockchain API.
- **Interesting Wallet Logging**: Logs any "interesting" wallets (with past transactions or balance) in a `Found.txt` file.
- **System Resource Monitoring**: Displays CPU, RAM, and disk usage to monitor system performance.
- **Multithreading**: Uses multiple threads to generate and check wallets concurrently for improved performance.


## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/notadminn/Ethereum-Cracker-Generator
2. **Install & Run**:
```bash
   cd Ethereum-Cracker-Generator
   pip install -r requirements.txt
   python cracker.py

