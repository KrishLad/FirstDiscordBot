from googleapiclient.discovery import build
import random



def get_id_video(message):
    # Enter your API key here
    API_KEY = 'ytkey'

    # Enter the title of the video you want to search for
    search_title = message

    # Create a YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for videos with the given title
    search_response = youtube.search().list(
        q=search_title,
        type='video',
        part='id,snippet',
        maxResults=25  # You can change this number if you want to get more search results
    ).execute()

    # Get the list of videos returned by the search
    videos = search_response['items']

    # Select a random video from the list
    random_video = random.choice(videos)

    # Get the video ID and title
    video_id = random_video['id']['videoId']
    return video_id