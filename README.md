# Hurricane Tracker

This project provides a comprehensive, interactive platform for monitoring tropical cyclones using a robust Python Flask backend to handle data fetching and avoid common browser security (CORS) issues.

## Features

- **Live Storm Tracking:** Displays official NHC cones of uncertainty and forecast tracks.
- **Advanced Data Overlays:** Visualizes sea surface temperature, wind shear, and other environmental data.
- **Live Hurricane Hunter Tracking:** Plots real-time flight paths of hunter aircraft via a secure proxy.
- **Resilient Data Fetching:** Falls back to sample data if live sources are unavailable.

## Setup and Installation

### 1. Prerequisites
- Python 3.6+
- pip (Python package installer)

### 2. Clone the Repository
Clone this project to your local machine.

### 3. Install Dependencies
Navigate into the project directory and install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variable for API Key
The Hurricane Hunter feature requires an API key from ADS-B Exchange. You must set this key as an environment variable so the server can use it securely.

On macOS / Linux:
```bash
export ADS_B_API_KEY="YOUR_API_KEY_HERE"
```
On Windows (Command Prompt):
```bash
set ADS_B_API_KEY="YOUR_API_KEY_HERE"
```
Note: You must set this variable in the same terminal session where you will run the Flask app.

### 5. Run the Application

Start the Flask development server:
```bash
python main.py
```
6. View the Tracker

Open your web browser and navigate to http://127.0.0.1:5000 to see the application running.
