# Car Counter - Image Labeling Tool

## Overview
Machine Learning Model using CNN that counts the number of cars in a picture. This machine learning model contained manually gathered data, manually labeled data. 

## Project Structure
- `label_server.py` - Main Flask web application server to label the pictures for training
- `desk_capture.py` - Desktop screenshot capture script to gather the pictures from the New York Department of Transportation. 
- `pictures.json` - Metadata file containing information about all captured images
- `picture/` - Directory containing traffic camera images organized by camera location
- `labels/` - Directory where labeling data is stored as JSON files
- `main.ipynb` - Jupyter notebook (legacy)

## Camera Locations
- 2nd_Ave_49_st
- Queens_Midtown_Tunnel
- Queens_Plaza_North
- E_63_St
- S_Conduit_Ave_150

## Technical Details
- **Framework**: Flask
- **Language**: Python 3.11
- **Port**: 5000 (bound to 0.0.0.0)
- **Data Storage**: JSON files for labels and picture metadata
