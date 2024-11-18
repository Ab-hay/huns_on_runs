
# Travian Farm List Automation

This Python script automates farming tasks in the Travian game using Selenium for web automation. It reloads the farm list at randomized intervals to mimic human-like behavior and includes color-coded terminal outputs for better readability.

## Features

- Automates login and execution of the farm list in Travian.
- Implements randomized delays (`jitter`) between runs to simulate human behavior.
- Terminal outputs with color-coded messages for easy tracking:
  - **Yellow**: Start of a farming session.
  - **Green**: Waiting time before the next session.
  - **Red**: Errors encountered during execution.

## Requirements

- Python 3.7 or higher
- Firefox browser
- GeckoDriver (for Selenium)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/travian-farm-automation.git
   cd travian-farm-automation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download GeckoDriver**:
   - Download the [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and place it in the directory specified by `GECKODRIVER_PATH` in the script (`../bin/geckodriver` by default).

4. **Update script variables**:
   - Replace the placeholders with your Travian login details and URLs:
     ```python
     USERNAME = 'your-email@example.com'
     PASSWORD = 'your-password'
     master_site = "https://your-travian-server.com/dorf1.php"
     farm_list_url = "https://your-travian-server.com/build.php?id=39&gid=16&tt=99"
     ```

## Usage

Run the script using Python:
```bash
python3 your_script_name.py
```

### What the script does:
1. Opens the Travian login page.
2. Logs in using your credentials.
3. Navigates to the farm list and executes it.
4. Waits for a randomized interval before repeating the process.

## Output Format

The script outputs status messages in the terminal with colors for clarity:
- **Yellow**: Indicates the start of a farming session.
  ```
  Starting farm list, triggered count: X
  ```
- **Green**: Displays the waiting time before the next farming session.
  ```
  waiting for X seconds before restarting
  ```
- **Red**: Reports errors, if any.
  ```
  Error: <error message>
  ```

## Troubleshooting

- **Ensure GeckoDriver is installed**:
  Verify the `GECKODRIVER_PATH` in the script is set correctly to the path of your GeckoDriver executable.
- **Verify the URLs**:
  Ensure the `master_site` and `farm_list_url` match your Travian server and farm list.
- **Check for dependencies**:
  Install all Python dependencies listed in the `requirements.txt` file.

## Disclaimer

This script is for educational purposes only. Automating tasks in online games may violate the game's terms of service. Use responsibly and at your own risk.

---
**Author**: Your Name  
**License**: MIT License
