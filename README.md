# Ethereum Wallet Generator and Checker

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
   git clone https://github.com/notadminn/EthWalletHunter
2. **Install & Run**:
   ```bash
   cd EthWalletHunter
   pip install -r requirements.txt
   python cracker.py

## Disclaimer

This tool is intended strictly for private learning and educational purposes. This GitHub repository is private, and any unauthorized access or use of its contents is prohibited and considered illegal. **Only the repository owner is authorized to access, use, or modify this code.**

Misuse of this tool, especially for unauthorized access to cryptocurrency wallets or funds, is illegal and unethical. Any such actions are strictly the responsibility of the user.

**The authors and contributors of this tool do not endorse or support any misuse and are not liable for any damages or legal issues arising from its misuse.**
