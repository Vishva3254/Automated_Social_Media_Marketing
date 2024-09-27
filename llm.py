# gemini_api_key = "AIzaSyCPPM1d9kcvDZ8HrMxZdu4BD55q5gFZCWs"

import google.generativeai as genai
import os

os.environ["API_KEY"] = 'AIzaSyCPPM1d9kcvDZ8HrMxZdu4BD55q5gFZCWs'
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash-latest')

def content_creator(topics, platform):

    query_text = f"Generate cool, unique and trending contents based on the provided trending topics list here {topics} and these contents are from this platforms {platform}" 

    response = model.generate_content(query_text)
    print(response.text)
    return response.text


trending_topics = [
    {
        "topic": "#MATRIX",
        "tweet_volume": "Under 10k Tweets",
        "summary": "A discussion surrounding the Matrix franchise, possibly related to recent news or content releases.",
        "link": "https://twitter.com/search?q=%23MATRIX"
    },
    {
        "topic": "Hillary",
        "tweet_volume": "224.7k Tweets",
        "summary": "Trending discussions likely focus on Hillary Clinton, possibly related to current political events or commentary.",
        "link": "https://twitter.com/search?q=Hillary"
    },
    {
        "topic": "Constitution Day",
        "tweet_volume": "10.4k Tweets",
        "summary": "Celebrations and discussions regarding Constitution Day, highlighting its significance and events.",
        "link": "https://twitter.com/search?q=Constitution%20Day"
    },
    {
        "topic": "#NationalVoterRegistrationDay",
        "tweet_volume": "Under 10k Tweets",
        "summary": "Awareness campaigns and discussions about voter registration in the United States.",
        "link": "https://twitter.com/search?q=%23NationalVoterRegistrationDay"
    },
    {
        "topic": "Diddy",
        "tweet_volume": "245.2k Tweets",
        "summary": "Conversations surrounding Diddy, possibly related to his music or recent public appearances.",   
        "link": "https://twitter.com/search?q=Diddy"
    },
    {
        "topic": "The Plucky Squire",
        "tweet_volume": "Under 10k Tweets",
        "summary": "Discussions about 'The Plucky Squire', likely pertaining to a game or media release.",
        "link": "https://twitter.com/search?q=The%20Plucky%20Squire"
    },
    {
        "topic": "Howard",
        "tweet_volume": "28.4k Tweets",
        "summary": "'Howard' trending may relate to various contexts, possibly a celebrity or event.",
        "link": "https://twitter.com/search?q=Howard"
    },
    {
        "topic": "#VoteReady",
        "tweet_volume": "Under 10k Tweets",
        "summary": "'#VoteReady' discussions focus on encouraging voter participation and readiness for upcoming elections.",
        "link": "https://twitter.com/search?q=%23VoteReady"
    },
    {
        "topic": "#TuesdayFeeling",
        "tweet_volume": "Under 10k Tweets",
        "summary": "A light-hearted trend where users share their feelings about the day of the week.",
        "link": "https://twitter.com/search?q=%23TuesdayFeeling"
    },
    {
        "topic": "#tuesdayvibe",
        "tweet_volume": "Under 10k Tweets",
        "summary": "Similar to #TuesdayFeeling, this trend captures the mood of users on Tuesdays.",
        "link": "https://twitter.com/search?q=%23tuesdayvibe"
    }
]
platform_name = ['twitter']
content_creator(trending_topics, platform_name)