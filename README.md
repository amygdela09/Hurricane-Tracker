# Hurricane-Tracker

This will eventually be incorporated into my NexradNext repo. 

A comprehensive, interactive web-based platform for monitoring and analyzing tropical cyclones and related weather phenomena in real-time. This tool integrates live storm data, historical tracks, environmental analysis layers, and real-time Hurricane Hunter aircraft tracking into a single, easy-to-use interface.

Features

This application combines data from numerous official and public sources to provide a multi-faceted view of the tropical weather environment.
🛰️ Live Tropical Cyclone Tracking
 * Official Forecasts: Plots the latest official forecast track and cone of uncertainty from the National Hurricane Center (NHC) for all active storms.
 * Spaghetti Models: Overlays an ensemble of computer model predictions (spaghetti plots) to visualize forecast uncertainty.
 * Tropical Outlooks: Fetches and displays the latest text-based Tropical Weather Outlooks from the NHC, detailing potential areas for future development.
✈️ Live Hurricane Hunter Tracking
 * Real-Time Flight Paths: Integrates with live ADS-B (Automatic Dependent Surveillance-Broadcast) data to track the flight paths of NOAA and USAF Reserve Hurricane Hunter aircraft.
 * Dynamic Updates: Aircraft positions, altitudes, callsigns, and flight trails are updated automatically on the map every 30 seconds.
 * Aircraft Details: Clicking on an aircraft icon reveals its callsign, speed, altitude, and heading.
⛈️ Advanced Meteorological Analysis
Analyze the atmospheric conditions that fuel or inhibit tropical development with professional-grade data layers:
 * Sea Surface Temperature (SST): Visualizes the "ocean fuel" necessary for storms to form and intensify.
 * Vertical Wind Shear: Shows atmospheric disruption that can tear storms apart, a key inhibitor of development.
 * Steering Flow (500mb Winds): Displays the mid-level atmospheric winds that guide a storm's path.
 * Mid-Level Moisture: Highlights areas of moist, supportive air versus dry, inhibiting air (like the Saharan Air Layer).
📖 Historical Storm Analysis
 * Historical Database: Switch to "Historical Mode" to explore the tracks of significant past hurricanes.
 * Intensity-Coded Tracks: Historical storm paths are color-coded based on the Saffir-Simpson Hurricane Wind Scale, providing an at-a-glance view of the storm's intensification and weakening phases.
🗺️ Interactive Map Controls
 * Layer Toggling: A user-friendly, grouped layer control allows for toggling the visibility of every data layer, from storm tracks to analysis grids.
 * Basemap Selector: Switch between Street, Satellite, and Dark basemaps to customize your view.
 * Storm Selector: When multiple storms are active, a dropdown menu allows you to focus the map on a specific system.
   
Setup and Installation

This project is designed to be lightweight and accessible. It runs entirely in the browser without needing a complex backend.
 * Clone the Repository:
   git clone https://github.com/your-username/hurricane-tracker.git
 * Get Your API Key:
   The Hurricane Hunter tracking feature requires a free API key from ADS-B Exchange.
   * Sign up for a key at ADS-B Exchange API Data.
   * Open the professional_tracker_with_hunters.html file in a text editor.
 * Insert Your API Key:
   Locate the following line in the <script> section and replace the placeholder with your key:
   // !!! IMPORTANT: REPLACE WITH YOUR KEY !!!
API_KEY: 'YOUR_ADS-B_EXCHANGE_API_KEY',

 * Run the Project:
   
   Simply open the professional_tracker_with_hunters.html file in any modern web browser.
   
Credits and Data Sources

This project would not be possible without the open data and software provided by the following organizations:
 * National Hurricane Center (NHC): For providing the foundational tropical cyclone advisories, text outlooks, and forecast data.
 * Florida Division of Emergency Management (FDEM): For providing the processed GeoJSON feeds for active storms, which simplifies the visualization of cones, tracks, and spaghetti models.
 * ADS-B Exchange: For offering the accessible, real-time API for tracking Hurricane Hunter aircraft.
 * NOAA Environmental Modeling Center (EMC): For the public Web Map Services (WMS) that provide the advanced analysis layers from the GFS model.
 * Leaflet.js: The core open-source mapping library that powers the entire interactive map.
 * OpenStreetMap & CartoDB: For the high-quality, free-to-use base map tiles.
 * Flaticon: For the airplane icon used for the Hurricane Hunter tracker.

Contributing

Contributions are welcome and appreciated! If you have an idea for a new feature or have found a bug, please feel free to:
 * Open an issue to discuss the change.
 * Fork the repository and submit a pull request.
   
License

This project is licensed under the MIT License. See the LICENSE file for full details.
Disclaimer
This tool is for informational and educational purposes only. It should NOT be used for making life-or-death decisions. Always consult official information and follow the guidance issued by the National Hurricane Center and your local authorities.
