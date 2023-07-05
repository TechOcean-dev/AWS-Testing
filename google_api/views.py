from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import urlencode
from google.oauth2.credentials import Credentials

class GoogleAuthView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri('/oauth2callback')
        scopes = ['https://www.googleapis.com/auth/calendar']

        flow = Flow.from_client_secrets_file(
            'client_secret.json',  # Replace with your client secret file path
            scopes=scopes,
            redirect_uri=redirect_uri
        )

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        return Response({'url': authorization_url, 'state': state}, status=status.HTTP_200_OK)
    
class GoogleAuthCallbackView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri('/oauth2callback')
        authorization_code = request.GET.get('code', '')

        flow = Flow.from_client_secrets_file(
            'client_secret.json',  # Replace with your client secret file path
            scopes=['https://www.googleapis.com/auth/calendar'],
            redirect_uri=redirect_uri
        )

        flow.fetch_token(authorization_response=redirect_uri, code=authorization_code)

        # Store the access token for future use (e.g., in the user session or database)

        return Response('Authentication successful', status=status.HTTP_200_OK)
    
class CalendarEventsView(APIView):
    def get(self, request):
        # Retrieve the access token from storage (e.g., user session or database)
        access_token = 'ya29.a0AbVbY6McehTOCrTTLey9gyQ9q4styY94i8npDzk0SE21JbDHQicYQMD2ia6RqK4RjHhRRnKXpP8APefr1ZUyp4xkImhJBvGrxpzz11dI5AU-ZZjFqVrq8e4cQvineOmxKMxUZOaa0kUzKrc6_SiVsOLIFmL7aCgYKAScSARMSFQFWKvPluMJYCwgqQZai3LZuhb5ZRA0163'

        credentials = Credentials.from_authorized_user_info(
            {
              'access_token': access_token, 
              'client_secret': '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',
              'client_id': '859111825072-2pgjg8bbrs1vlmat8qi66c5j4kvfjbj2.apps.googleusercontent.com',
              'refresh_token': '1//03yXUbBVYIhYsCgYIARAAGAMSNwF-L9IrJIXkCrYvz09zXGzl45yQs3TIvLFiUJAc4elQK4Styx9C1bBC-qYLCtQul58lphU_kus'
            },
            scopes=['https://www.googleapis.com/auth/calendar']
        )

        service = build('calendar', 'v3', credentials=credentials)

        # Perform operations on the calendar, e.g., list events
        events = service.events().list(calendarId='primary').execute()

        return Response(events, status=status.HTTP_200_OK)

