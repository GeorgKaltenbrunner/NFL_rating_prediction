# Imports

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def collect_data(URL, year):
    """Collects the information from the given url and year.
    :param URL: Represents the needed URL to establish a connection.
    :param year: Is needed for the URL
    :return: 1) Returns the collected data as pd.DataFrame. 2) Information, whether a next page exists (next_page).
                This is needed for pagination. 3) A new URL for pagination (new_url).
    """

    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Get name of each player
    names = [str(name.string) for name in soup.find_all(class_="d3-o-media-object__body")]

    # Get Pass Yds of each player
    pass_yds = [float(passyds.string) for passyds in soup.find_all(class_="selected")]

    # Get Yds/Att for each player
    yds_att = [float(ydsatt.next_sibling.string) for ydsatt in soup.find_all(class_="selected")]

    # Get Att
    att = [float(att.next_sibling.next_sibling.string) for att in soup.find_all(class_="selected")]

    # Get Cmp
    cmp = [float(cmp.next_sibling.next_sibling.next_sibling.string) for cmp in soup.find_all(class_="selected")]

    # Get Cmp%
    cmp_ = [float(cmp_.next_sibling.next_sibling.next_sibling.next_sibling.string) for cmp_ in
            soup.find_all(class_="selected")]

    # Get Td
    td = [float(td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string) for td in
          soup.find_all(class_="selected")]

    # Get INT
    int_ = [float(int_.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string) for
            int_ in
            soup.find_all(class_="selected")]

    # Get each player rating
    rating = [
        float(rating.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string)
        for
        rating in
        soup.find_all(class_="selected")]

    # Change size
    if len(names) != len(pass_yds):
        pass_yds = pass_yds[:len(names)]
        yds_att = yds_att[:len(names)]
        att = att[:len(names)]
        cmp = cmp[:len(names)]
        cmp_ = cmp_[:len(names)]
        td = td[:len(names)]
        int_ = int_[:len(names)]
        rating = rating[:len(names)]
    try:
        df = pd.DataFrame(
            {'Name': names, 'rates': rating, 'pass_yds': pass_yds, 'yds_att': yds_att, 'att': att, 'cmp': cmp,
             'cmp%': cmp_, 'td': td, 'INT_': int_, 'year': np.repeat(year, len(names))})

    except Exception as e:
        print(e)
        df = pd.DataFrame()

    # Pagination
    try:
        next_page = soup.find_all(class_='nfl-o-table-pagination__buttons')
        new_url = next_page[0].contents[0].attrs['href']
        next_page = str(next_page[0].next_element.string)

    except:
        next_page = ""
        new_url = ""

    return df, next_page, new_url


years = np.arange(1970, 2023)
df_players_pass = pd.DataFrame()
for year in years:
    print(year)
    nfl_base = "https://www.nfl.com"
    URL = f"{nfl_base}/stats/player-stats/category/passing/{year}/reg/all/passingyards/desc"
    next_page = 'next page'
    while next_page != "":
        df, next_page, new_url = collect_data(URL, year)
        URL = nfl_base + new_url

        # append to df_players_pass
        df_players_pass = pd.concat([df_players_pass, df])

df_players_pass.to_csv('nfl_pass.csv', index=False)
