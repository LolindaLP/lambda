# Spotify Top 50 Songs

https://tgs50.com/

## Project Overview

<p style="font-size: 18px;">The Flask web application displays today's top 50 Spotify tracks and allows users to view top tracks for other days in the database. **Note:** This project is no longer working due to changes in Spotify’s API policy.</p>

## How It Works

### 1. Daily Data Acquisition:
<p style="font-size: 16px;">
An AWS Lambda function is triggered daily by an EventBridge rule.
The Lambda function generates a Spotify API access token.
It then fetches the Spotify Top 50 Global playlist data.
Track details (title, artist, album, popularity) are extracted and stored in a DynamoDB table.
</p>

### 2. Data Storage:
<p style="font-size: 16px;">
Track data is stored in a DynamoDB table, maintaining historical data for user access.
DynamoDB's scalability ensures fast and reliable data access.
</p>

### 3. Web Interface Hosted on AWS Lambda:
<p style="font-size: 16px;">
A Flask web application, deployed on AWS Lambda via API Gateway, retrieves and displays the top 50 tracks for the current day.
The application uses the Plotly library to create a graph showing the top 5 artists and their song contributions.
Users can select different dates to view past top tracks, dynamically updating the displayed data.
</p>

### 4. User Interaction:
<p style="font-size: 16px;">
A date picker allows users to choose specific dates.
The application fetches and displays data for the selected date from the DynamoDB table.
</p>

### 5. Data Persistence:
<p style="font-size: 16px;">
DynamoDB ensures data persistence and high availability for future access.
Daily updates are handled by the Lambda function triggered by EventBridge, which updates the database with the latest top 50 tracks.
</p>
