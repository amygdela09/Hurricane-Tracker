import os
import requests
from flask import Flask, render_template, jsonify, request, Response

app = Flask(__name__)

# Route to serve the main tracker webpage
@app.route('/')
def index():
    """Renders the main map page."""
    return render_template('index.html')

# Proxy route for live storm data from FDEM
@app.route('/storm-data')
def get_storm_data():
    """Fetches live storm data. Returns empty list if source is down or no storms."""
    try:
        url = 'https://www.floridadisaster.org/data/geojson/active_storms.geojson'
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching storm data: {e}")
        # Return an empty FeatureCollection on error, so the frontend can handle it
        return jsonify({"type": "FeatureCollection", "features": []})

# Proxy route for NOAA's WMS tile server
@app.route('/noaa-wms')
def proxy_noaa_wms():
    """Proxies requests to the NOAA WMS server to avoid CORS issues."""
    try:
        wms_url = 'https://mag.ncep.noaa.gov/arcgis/services/mac/gfs/MapServer/WmsServer'
        # Forward all query parameters from the Leaflet request to the WMS server
        response = requests.get(wms_url, params=request.args, stream=True, timeout=10)
        response.raise_for_status()
        # Return the image content with the correct content type
        return Response(response.content, content_type=response.headers['content-type'])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NOAA WMS tile: {e}")
        return Response(status=500)

# Proxy route for Hurricane Hunter aircraft data
@app.route('/adsb-proxy/<path:hex_codes>')
def proxy_adsb(hex_codes):
    """Proxies requests to the ADS-B Exchange API, securely adding the API key."""
    # Securely get API key from an environment variable
    api_key = os.getenv('ADS_B_API_KEY')
    if not api_key:
        return jsonify({"error": "ADS-B API key not configured on server."}), 500

    api_url = f"https://adsbexchange-com1.p.rapidapi.com/v2/hex/{hex_codes}/"
    headers = {'api-auth': api_key}
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ADS-B data: {e}")
        return jsonify({"error": "Failed to fetch aircraft data."}), 502


if __name__ == '__main__':
    app.run(debug=True, port=5000)
