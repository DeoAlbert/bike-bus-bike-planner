#!/usr/bin/env python3
"""
Railway startup script for Bike-Bus-Bike Route Planner
"""
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main application
from python_deploy import run_bike_bus_bike_google_server

if __name__ == "__main__":
    print("Starting Bike-Bus-Bike Route Planner on Railway...")
    run_bike_bus_bike_google_server()
