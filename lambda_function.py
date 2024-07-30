from flask import Flask, render_template, request, jsonify
from datetime import datetime
import boto3
import awsgi
from boto3.dynamodb.conditions import Attr

app = Flask(__name__)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tracks')

def get_top_tracks_for_date(today):
    try:
        datetime.strptime(today, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")

    response = table.scan(
            FilterExpression=Attr('date').eq(today)
        )
    tracks = response.get('Items', [])
    sorted_tracks = sorted(tracks, key=lambda x: int(x['id']))
    return sorted_tracks

def get_available_dates():
    response = table.scan(
        ProjectionExpression='#d',
        ExpressionAttributeNames={'#d': 'date'}
    )
    all_dates = sorted({item['date'] for item in response.get('Items', [])})
    return all_dates

@app.route('/')
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    today_top_tracks = get_top_tracks_for_date(today)
    available_dates = get_available_dates()

    return render_template('index.html', today_top_tracks=today_top_tracks, available_dates=available_dates)

@app.route('/available-dates')
def available_dates_route():
    all_dates = get_available_dates()
    return jsonify(all_dates)

@app.route('/top-tracks', methods=['GET'])
def top_tracks():
    date = request.args.get('date')
    tracks = get_top_tracks_for_date(date)
    return jsonify(tracks)


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
