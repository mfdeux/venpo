import datetime
import json
import os
import random
import typing

import dateutil.parser as date_parser
import requests
from bs4 import BeautifulSoup

# Location of package-included user agents
DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data')
USER_AGENT_FILE = os.path.join(DATA_DIR, 'user_agents.json')


def load_user_agents(filepath: str) -> typing.List[str]:
    """
    Loads list of user agents
    Args:
        filepath: path to user agent file

    Returns:
        List of user agents

    """
    user_agents = []

    with open(filepath) as f:
        user_agents = json.load(f)

    return user_agents


def scrape_profile(username: str, user_agents: typing.List[str]) -> typing.List[typing.Dict]:
    """
    Scrapes public Venmo profile for specified username

    Args:
        username:
        user_agents:

    Returns:

    """
    try:
        r = requests.get(f"https://venmo.com/{username}",
                         headers={"User-Agent": random.choice(user_agents)})
    except requests.exceptions.ConnectionError:
        print("Error, unable to connect to host... check your network connection")
        return 1

    soup = BeautifulSoup(r.text, "lxml")
    profile_data = []

    transactions = soup.find_all("div", attrs={"class": "single-payment content-wrap"})

    for transaction in transactions:
        send, recv = transaction.find_all("a")
        send, recv = send.text, recv.text
        message = transaction.find_all("div", attrs={"class": "paymentpage-text m_five_t"})[0].text
        date = date_parser.parse(transaction.find_all("div", attrs={"class": "date"})[0].text.split('-')[0], fuzzy=True)
        export_message = f"{send} paid {recv} on {date.replace(microsecond=0).isoformat()} for {message}"
        profile_data.append({"sender": send,
                             "recipient": recv,
                             "date": date.replace(microsecond=0).isoformat(),
                             "export_message": export_message})

    return profile_data


def save_data(data: typing.List[typing.Dict], filename: str):
    """
    Saves scraped profile data to file
    Args:
        data:
        filename:

    Returns:

    """
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{filename}-{now}.json", "w") as f:
        f.write(json.dumps(data))
