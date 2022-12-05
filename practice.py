{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Harshit Kotnala "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Science and Business Analytics Intern @ TSF "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exploratory Data Analysis : Sports (Indian Premier League)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dataset : matches.csv (https://bit.ly/34SRn3b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>season</th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>result</th>\n",
       "      <th>dl_applied</th>\n",
       "      <th>winner</th>\n",
       "      <th>win_by_runs</th>\n",
       "      <th>win_by_wickets</th>\n",
       "      <th>player_of_match</th>\n",
       "      <th>venue</th>\n",
       "      <th>umpire1</th>\n",
       "      <th>umpire2</th>\n",
       "      <th>umpire3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>2017-04-05</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>Yuvraj Singh</td>\n",
       "      <td>Rajiv Gandhi International Stadium, Uppal</td>\n",
       "      <td>AY Dandekar</td>\n",
       "      <td>NJ Llong</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>Pune</td>\n",
       "      <td>2017-04-06</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>SPD Smith</td>\n",
       "      <td>Maharashtra Cricket Association Stadium</td>\n",
       "      <td>A Nand Kishore</td>\n",
       "      <td>S Ravi</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2017</td>\n",
       "      <td>Rajkot</td>\n",
       "      <td>2017-04-07</td>\n",
       "      <td>Gujarat Lions</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>CA Lynn</td>\n",
       "      <td>Saurashtra Cricket Association Stadium</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>CK Nandan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2017</td>\n",
       "      <td>Indore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>GJ Maxwell</td>\n",
       "      <td>Holkar Cricket Stadium</td>\n",
       "      <td>AK Chaudhary</td>\n",
       "      <td>C Shamshuddin</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2017</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Delhi Daredevils</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  season       city        date                        team1  \\\n",
       "0   1    2017  Hyderabad  2017-04-05          Sunrisers Hyderabad   \n",
       "1   2    2017       Pune  2017-04-06               Mumbai Indians   \n",
       "2   3    2017     Rajkot  2017-04-07                Gujarat Lions   \n",
       "3   4    2017     Indore  2017-04-08       Rising Pune Supergiant   \n",
       "4   5    2017  Bangalore  2017-04-08  Royal Challengers Bangalore   \n",
       "\n",
       "                         team2                  toss_winner toss_decision  \\\n",
       "0  Royal Challengers Bangalore  Royal Challengers Bangalore         field   \n",
       "1       Rising Pune Supergiant       Rising Pune Supergiant         field   \n",
       "2        Kolkata Knight Riders        Kolkata Knight Riders         field   \n",
       "3              Kings XI Punjab              Kings XI Punjab         field   \n",
       "4             Delhi Daredevils  Royal Challengers Bangalore           bat   \n",
       "\n",
       "   result  dl_applied                       winner  win_by_runs  \\\n",
       "0  normal           0          Sunrisers Hyderabad           35   \n",
       "1  normal           0       Rising Pune Supergiant            0   \n",
       "2  normal           0        Kolkata Knight Riders            0   \n",
       "3  normal           0              Kings XI Punjab            0   \n",
       "4  normal           0  Royal Challengers Bangalore           15   \n",
       "\n",
       "   win_by_wickets player_of_match                                      venue  \\\n",
       "0               0    Yuvraj Singh  Rajiv Gandhi International Stadium, Uppal   \n",
       "1               7       SPD Smith    Maharashtra Cricket Association Stadium   \n",
       "2              10         CA Lynn     Saurashtra Cricket Association Stadium   \n",
       "3               6      GJ Maxwell                     Holkar Cricket Stadium   \n",
       "4               0       KM Jadhav                      M Chinnaswamy Stadium   \n",
       "\n",
       "          umpire1        umpire2 umpire3  \n",
       "0     AY Dandekar       NJ Llong     NaN  \n",
       "1  A Nand Kishore         S Ravi     NaN  \n",
       "2     Nitin Menon      CK Nandan     NaN  \n",
       "3    AK Chaudhary  C Shamshuddin     NaN  \n",
       "4             NaN            NaN     NaN  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv(\"matches.csv\")\n",
    "\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>inning</th>\n",
       "      <th>batting_team</th>\n",
       "      <th>bowling_team</th>\n",
       "      <th>over</th>\n",
       "      <th>ball</th>\n",
       "      <th>batsman</th>\n",
       "      <th>non_striker</th>\n",
       "      <th>bowler</th>\n",
       "      <th>is_super_over</th>\n",
       "      <th>...</th>\n",
       "      <th>bye_runs</th>\n",
       "      <th>legbye_runs</th>\n",
       "      <th>noball_runs</th>\n",
       "      <th>penalty_runs</th>\n",
       "      <th>batsman_runs</th>\n",
       "      <th>extra_runs</th>\n",
       "      <th>total_runs</th>\n",
       "      <th>player_dismissed</th>\n",
       "      <th>dismissal_kind</th>\n",
       "      <th>fielder</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id  inning         batting_team                 bowling_team  over  \\\n",
       "0         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "1         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "2         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "3         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "4         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "\n",
       "   ball    batsman non_striker    bowler  is_super_over  ...  bye_runs  \\\n",
       "0     1  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "1     2  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "2     3  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "3     4  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "4     5  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "\n",
       "   legbye_runs  noball_runs  penalty_runs  batsman_runs  extra_runs  \\\n",
       "0            0            0             0             0           0   \n",
       "1            0            0             0             0           0   \n",
       "2            0            0             0             4           0   \n",
       "3            0            0             0             0           0   \n",
       "4            0            0             0             0           2   \n",
       "\n",
       "   total_runs  player_dismissed dismissal_kind fielder  \n",
       "0           0               NaN            NaN     NaN  \n",
       "1           0               NaN            NaN     NaN  \n",
       "2           4               NaN            NaN     NaN  \n",
       "3           0               NaN            NaN     NaN  \n",
       "4           2               NaN            NaN     NaN  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Data = pd.read_csv(\"deliveries.csv\")\n",
    "\n",
    "Data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "season_data=data[['id','season','winner']]\n",
    "\n",
    "complete_data=Data.merge(season_data,how='inner',left_on='match_id',right_on='id')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',\n",
       "       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',\n",
       "       'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2',\n",
       "       'umpire3'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>season</th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>result</th>\n",
       "      <th>dl_applied</th>\n",
       "      <th>winner</th>\n",
       "      <th>win_by_runs</th>\n",
       "      <th>win_by_wickets</th>\n",
       "      <th>player_of_match</th>\n",
       "      <th>venue</th>\n",
       "      <th>umpire1</th>\n",
       "      <th>umpire2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>2017-04-05</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>Yuvraj Singh</td>\n",
       "      <td>Rajiv Gandhi International Stadium, Uppal</td>\n",
       "      <td>AY Dandekar</td>\n",
       "      <td>NJ Llong</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>Pune</td>\n",
       "      <td>2017-04-06</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>SPD Smith</td>\n",
       "      <td>Maharashtra Cricket Association Stadium</td>\n",
       "      <td>A Nand Kishore</td>\n",
       "      <td>S Ravi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2017</td>\n",
       "      <td>Rajkot</td>\n",
       "      <td>2017-04-07</td>\n",
       "      <td>Gujarat Lions</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>CA Lynn</td>\n",
       "      <td>Saurashtra Cricket Association Stadium</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>CK Nandan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2017</td>\n",
       "      <td>Indore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>GJ Maxwell</td>\n",
       "      <td>Holkar Cricket Stadium</td>\n",
       "      <td>AK Chaudhary</td>\n",
       "      <td>C Shamshuddin</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2017</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Delhi Daredevils</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  season       city        date                        team1  \\\n",
       "0   1    2017  Hyderabad  2017-04-05          Sunrisers Hyderabad   \n",
       "1   2    2017       Pune  2017-04-06               Mumbai Indians   \n",
       "2   3    2017     Rajkot  2017-04-07                Gujarat Lions   \n",
       "3   4    2017     Indore  2017-04-08       Rising Pune Supergiant   \n",
       "4   5    2017  Bangalore  2017-04-08  Royal Challengers Bangalore   \n",
       "\n",
       "                         team2                  toss_winner toss_decision  \\\n",
       "0  Royal Challengers Bangalore  Royal Challengers Bangalore         field   \n",
       "1       Rising Pune Supergiant       Rising Pune Supergiant         field   \n",
       "2        Kolkata Knight Riders        Kolkata Knight Riders         field   \n",
       "3              Kings XI Punjab              Kings XI Punjab         field   \n",
       "4             Delhi Daredevils  Royal Challengers Bangalore           bat   \n",
       "\n",
       "   result  dl_applied                       winner  win_by_runs  \\\n",
       "0  normal           0          Sunrisers Hyderabad           35   \n",
       "1  normal           0       Rising Pune Supergiant            0   \n",
       "2  normal           0        Kolkata Knight Riders            0   \n",
       "3  normal           0              Kings XI Punjab            0   \n",
       "4  normal           0  Royal Challengers Bangalore           15   \n",
       "\n",
       "   win_by_wickets player_of_match                                      venue  \\\n",
       "0               0    Yuvraj Singh  Rajiv Gandhi International Stadium, Uppal   \n",
       "1               7       SPD Smith    Maharashtra Cricket Association Stadium   \n",
       "2              10         CA Lynn     Saurashtra Cricket Association Stadium   \n",
       "3               6      GJ Maxwell                     Holkar Cricket Stadium   \n",
       "4               0       KM Jadhav                      M Chinnaswamy Stadium   \n",
       "\n",
       "          umpire1        umpire2  \n",
       "0     AY Dandekar       NJ Llong  \n",
       "1  A Nand Kishore         S Ravi  \n",
       "2     Nitin Menon      CK Nandan  \n",
       "3    AK Chaudhary  C Shamshuddin  \n",
       "4             NaN            NaN  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = data.drop(columns=[\"umpire3\"],axis=1)\n",
    "\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "season  winner                     \n",
       "2008    Rajasthan Royals               13\n",
       "        Kings XI Punjab                10\n",
       "        Chennai Super Kings             9\n",
       "        Delhi Daredevils                7\n",
       "        Mumbai Indians                  7\n",
       "                                       ..\n",
       "2019    Kings XI Punjab                 6\n",
       "        Kolkata Knight Riders           6\n",
       "        Sunrisers Hyderabad             6\n",
       "        Rajasthan Royals                5\n",
       "        Royal Challengers Bangalore     5\n",
       "Name: winner, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wins_per_season = data.groupby(\"season\")[\"winner\"].value_counts()\n",
    "wins_per_season"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (18,10))\n",
    "sns.countplot('season',data=data,palette=\"winter\")\n",
    "plt.title(\"Number of Matches played in each IPL season\",fontsize=20)\n",
    "plt.xlabel(\"season\",fontsize=15)\n",
    "plt.ylabel('Matches',fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (18,10))\n",
    "sns.countplot(x='winner',data=data, palette='cool')\n",
    "plt.title(\"Numbers of matches won by team \",fontsize=20)\n",
    "plt.xticks(rotation=50)\n",
    "plt.xlabel(\"Teams\",fontsize=15)\n",
    "plt.ylabel(\"No of wins\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['win_by']=np.where(data['win_by_runs']>0,'Bat first','Bowl first')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Win=data.win_by.value_counts()\n",
    "labels=np.array(Win.index)\n",
    "sizes = Win.values\n",
    "colors = ['#FFBF00', '#FA8072']\n",
    "plt.figure(figsize = (10,8))\n",
    "plt.pie(sizes, labels=labels, colors=colors,\n",
    "        autopct='%1.1f%%', shadow=True,startangle=90)\n",
    "plt.title('Match Result',fontsize=20)\n",
    "plt.axis('equal',fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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PibdI0K3T/cUj+vTdfJ5ZGttyEeGAtyPEAIAAAAYhD4hAAAAgEFstH1CbLPNNm3RokWjLgMAAAAY59JLL72+tbbtZOM22hBi0aJFueSSS0ZdBgAAADBOVf1gqnFuxwAAAAAGIYQAAAAABiGEAAAAAAax0fYJMZk77rgj11xzTW6//fZRl7JRW7hwYbbffvssWLBg1KUAAACwCdmkQohrrrkmW2yxRRYtWpSqGnU5G6XWWm644YZcc801Wbx48ajLAQAAYBOySd2Ocfvtt2frrbcWQKyHqsrWW2+tNQkAAACzbpMKIZIIIGaBdQgAAMBc2ORCCAAAAGDDJISYRc9//vNz0003zfh1++yzTy655JI5qAgAAAA2HJtUx5SjdsYZZ4y6BAAAANhgaQkxA+9///tz7LHHJkne/va3Z7/99kuSnHPOOXn5y1+eRYsW5frrr8+qVauy00475Xd+53fy1Kc+Nb/yK7+S2267bY3z/uhHP5o999wzT3va0/KVr3wld999d5785Cdn9erVSZK77747T3rSk3L99dfP7ZsEAACAOSKEmIG99947F1xwQZLkkksuya233po77rgjF154YZYvX36fab/3ve/lzW9+c771rW9lyy23zKc+9ak1zvunP/1pLrroohx//PF5zWtek8022ywvf/nL87GPfSxJcvbZZ2fJkiXZZptt5ubNAQAAwBwTQszAM57xjFx66aW55ZZb8uAHPzh77LFHLrnkklxwwQX3CyEWL16cpUuX3vO6VatWrXHeL3vZy5J0QcfNN9+cm266Ka95zWvy93//90mSD3/4w3n1q189+28KAAAABiKEmIEFCxZk0aJF+chHPpI999wzy5cvz4oVK3LllVdmp512us+0D37wg+/5ed68ebnzzjvXOO+Jj8Wsquywww7Zbrvtcu655+bLX/5yDjjggNl7MwAAADAwIcQM7b333jnqqKOy9957Z/ny5TnhhBOydOnS+4UIM3XqqacmSS688MI84hGPyCMe8YgkyW//9m/n5S9/eV760pdm3rx5610/AAAAjIoQYoaWL1+e6667LnvssUe22267LFy48H63YqyLrbbaKnvuuWfe8IY35KSTTrpn+EEHHZRbb73VrRgAAABs9Dyic4b233//3HHHHff8/t3vfveen8f6fdhmm23yzW9+857hv//7v7/GeZ533nlTjrv88suzZMmSPOUpT1m3ggEAAGADIYTYgB155JH5wAc+cM8TMgAAAGBj5naMAb35zW/O0qVL7/P1kY98ZMrpjzjiiPzgBz/Is5/97AGrBAAAgLmhJcSAjjvuuFGXAAAAACMzkpYQVTWvqr5WVaf3vy+uqi9X1feq6tSqetAo6gIAAADmzqhux3hrkivG/f6XSY5urT05yY1JXjuSqgAAAIA5M3gIUVXbJ3lBkg/1v1eS/ZJ8sp/klCQvGrouAAAAYG6NoiXEMUn+IMnd/e9bJ7mptXZn//s1SR47grpmxbx587J06dIsWbIkT3/603PRRRetcfqbbropxx9//JTjjz322Oy000455JBDctppp+XII4+cdi2rVq3Kxz/+8WlPDwAAAHNp0I4pq+rXkvyotXZpVe0zNniSSdsUr39dktclyeMe97i1Lm/HVYvXrdApfGfR1Wud5iEPeUguu+yyJMnnP//5vOtd78r5558/5fRjIcSb3vSmSccff/zxOfPMM7N4cfdeDjrooPtNc+edd2b+/Pt/lGMhxMEHH7zWuoH1s3iXVaMuIVd/Y9GoS5g11icAwKZp6JYQeyU5qKpWJfmndLdhHJNky6oaO4vePsl/Tfbi1tqJrbVlrbVl22677RD1rpebb745W221VZLk1ltvzf7775+nP/3p2WWXXfLZz342SfcYziuvvDJLly7NO9/5zvu8/g1veEOuuuqqHHTQQTn66KNz8skn5y1veUuS5NBDD81hhx2WfffdN4cffnjOP//8ex77ueuuu+aWW27JEUcckQsuuCBLly7N0UcfPeybBwAAgAkGbQnRWntXknclSd8S4vdba4dU1T8n+Y10wcSrknx2yLpm02233ZalS5fm9ttvz3XXXZdzzz03SbJw4cJ85jOfycMf/vBcf/312X333XPQQQflyCOPzDe/+c17Wk+Md8IJJ+Sss87KihUrss022+Tkk0++z/jvfve7OfvsszNv3rwceOCBOe6447LXXnvl1ltvzcKFC3PkkUfmqKOOyumnnz7EWwcAAIA1GtXTMSY6PMlhVfX9dH1EnDTietbZ2O0YK1euzFlnnZVXvvKVaa2ltZY//MM/zC/90i/luc99bq699tr88Ic/XK9lveQlL8m8efOSJHvttVcOO+ywHHvssbnpppsmvT0DAAAARmlkZ6qttfOSnNf/fFWS3UZVy1zZY489cv3112f16tU544wzsnr16lx66aVZsGBBFi1alNtvv3295v+whz3snp+POOKIvOAFL8gZZ5yR3XffPWefffb6lg8AAACzyuXyObRy5crcdddd2XrrrfOTn/wkj3rUo7JgwYKsWLEiP/jBD5IkW2yxRW655Zb1XtaVV16ZXXbZJbvssksuvvjirFy5MjvssMOszBsAAABmgxBilo31CZEkrbWccsopmTdvXg455JAceOCBWbZsWZYuXZqnPOUpSZKtt946e+21V572tKflgAMOyF/91V+t03KPOeaYrFixIvPmzcvOO0hPqLUAACAASURBVO+cAw44IJtttlnmz5+fJUuW5NBDD83b3/72WXufAAAAMFPV2qRPw9zgLVu2rF1yySX3GXbFFVdkp512GlFFmxbrEmbGIyVnl/UJALDxqqpLW2vLJhu3oXRMCQAAAGzihBAAAADAIIQQAAAAwCCEEAAAAMAghBAAAADAIDyiEwA2YRvCk0YSTxuBuWZfBzYWWkLMsnnz5mXp0qVZsmRJnv70p+eiiy5a73luvvnmkw4/9thjs9NOO+WQQw7JaaedliOPPHLa81y1alU+/vGPr3dtAAAAMF2bdEuI2U6Ep5PsPuQhD8lll12WJPn85z+fd73rXTn//PNntY4xxx9/fM4888wsXrw4SXLQQQfdb5o777wz8+ff/2MeCyEOPvjgOakNAAAAJtISYg7dfPPN2WqrrZIkrbW8853vzNOe9rTssssuOfXUU5Mkb3rTm3LaaaclSV784hfnNa95TZLkpJNOyh//8R9POe83vOENueqqq3LQQQfl6KOPzsknn5y3vOUtSZJDDz00hx12WPbdd98cfvjhOf/887N06dIsXbo0u+66a2655ZYcccQRueCCC7J06dIcffTRc7kaAAAAIMkm3hJiFG677bYsXbo0t99+e6677rqce+65SZJPf/rTueyyy3L55Zfn+uuvzzOf+czsvffe2XvvvXPBBRfkoIMOyrXXXpvrrrsuSXLhhRfmt37rt6ZczgknnJCzzjorK1asyDbbbJOTTz75PuO/+93v5uyzz868efNy4IEH5rjjjstee+2VW2+9NQsXLsyRRx6Zo446KqeffvqcrQsAAAAYT0uIWTZ2O8bKlStz1lln5ZWvfGVaa7nwwgvzspe9LPPmzct2222X5zzn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\n",
      "text/plain": [
       "<Figure size 1296x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (18,10))\n",
    "sns.countplot('season',hue='win_by',data=data,palette='hsv')\n",
    "plt.title(\"Numbers of matches won by batting and bowling first \",fontsize=20)\n",
    "plt.xlabel(\"Season\",fontsize=15)\n",
    "plt.ylabel(\"Count\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# we will plot pie chart on Toss decision\n",
    "Toss=data.toss_decision.value_counts()\n",
    "labels=np.array(Toss.index)\n",
    "sizes = Toss.values\n",
    "colors = ['#FFBF00', '#FA8072']\n",
    "plt.figure(figsize = (10,8))\n",
    "plt.pie(sizes, labels=labels, colors=colors,\n",
    "        autopct='%1.1f%%', shadow=True,startangle=90)\n",
    "plt.title('Toss result',fontsize=20)\n",
    "plt.axis('equal',fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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WLx4cVasWLH2GQEAAIBuqup7c01zOgYAAADQhRACAAAA6EIIAQAAAHRxlx0TYjY33XRTrrjiitx4442TLmWjtvnmm2fHHXfMZpttNulSAAAAuBtZUCHEFVdcka233jqLFy9OVU26nI1Say1XXXVVrrjiiuy8886TLgcAAIC7kQV1OsaNN96Y7bffXgCxBlWV7bffXm8RAAAAultQIUQSAcQ6sI0AAACYhAUXQgAAAAAbpwUdQlxzzTU55ZRTuq3v8ssvz2677XaHnvvSl740n/70p+ecfuqpp+aMM864o6UBAADAxC2ogSlnmgohjj322EmXslaveMUr1jj9mGOO6VQJAAAAzI8F3RPipJNOyne+853stddeOfHEE3PiiSdmt912y+677573ve99SZIf/ehHecxjHpO99toru+22Wz73uc/llltuyeGHH7563je84Q1zruOLX/xi9txzzzzqUY/KsmXLVrffcsstOfHEE7N06dLsscceedvb3rZ62mtf+9rsvvvu2XPPPXPSSSclSQ4//PCcddZZq+t+2MMelj322CN/8zd/kyQ5+eST8/rXvz5JsnLlyjzykY/MHnvskT/5kz/J1VdfnSTZf//988IXvjB77713HvrQh+Zzn/vcBtyaAAAAcOcs6J4Qr3nNa3LxxRdn5cqVOfvss3PqqafmK1/5Sn7yk59k6dKlecxjHpN3v/vdOfDAA/PiF784t9xyS66//vqsXLkyP/jBD3LxxRcnGXpUzOWII47IW97yluy333458cQTV7e/4x3vyLbbbpvly5fnl7/8Zfbdd98ccMABufTSS/OhD30oX/jCF7Llllvmpz/96W2W99Of/jQf/OAHc+mll6aqZl33s571rNXrfOlLX5qXv/zleeMb35gkufnmm3PRRRfl4x//eF7+8pev8RQPAAAA6GlB94SY7vOf/3z+7M/+LJtssknud7/7Zb/99svy5cuzdOnSnHbaaTn55JPzta99LVtvvXV22WWXXHbZZXn+85+fT37yk9lmm21mXea1116ba665Jvvtt1+S5NBDD1097ZxzzskZZ5yRvfbaK/vss0+uuuqqfOtb38qnP/3pHHHEEdlyyy2TJPe5z31us8xtttkmm2++eY466qh84AMfWD3fXOs87LDD8tnPfnb19Kc97WlJkkc84hG5/PLL79xGAwAAgA3obhNCtNZmbX/MYx6Tz372s3nQgx6UQw89NGeccUa22267fOUrX8n++++fZcuW5aijjppzmXNd7rK1lre85S1ZuXJlVq5cme9+97s54IAD1vicJNl0001z0UUX5eCDD86HPvShPOEJT1iv13mve90rSbLJJpvk5ptvXq/nAgAAwHxa0CHE1ltvneuuuy7JEDa8733vyy233JJVq1bls5/9bPbee+9873vfyw477JDnPOc5OfLII/OlL30pP/nJT3Lrrbfm4IMPzitf+cp86UtfmnX59773vbPtttvm85//fJLkzDPPXD3twAMPzN///d/npptuSpL8+7//e37xi1/kgAMOyD/+4z/m+uuvT5LbnY7x85//PNdee22e9KQn5Y1vfGNWrlx5m+nbbrtttttuu9XjPbzrXe9a3SsCAAAANmYLekyI7bffPvvuu2922223PPGJT8wee+yRPffcM1WV1772tbn//e+f008/Pa973euy2WabZauttsoZZ5yRH/zgBzniiCNy6623Jkle/epXz7mO0047Lc9+9rOz5ZZb5sADD1zdftRRR+Xyyy/P7/7u76a1lkWLFq3u2bBy5cosWbIk97znPfOkJz0pf/u3f7v6edddd10OOuig3HjjjWmtzToo5umnn55jjjkm119/fXbZZZecdtppG3CrAQAAwPyouU5T2NgtWbKkrVix4jZtl1xySXbdddcJVXTXYlsBAAAwH6rqi621JbNNW9CnYwAAAAAbjwV9OsaGdNxxx+WCCy64TdsJJ5yQI444YkIVAQAAwF2LEGIdLVu2bNIlAAAAwF1a9xCiqi5Pcl2SW5Lc3FpbUlX3SfK+JIuTXJ7kGa21q3vXBgAAAMyfSY0J8djW2l7TBqo4Kcm5rbWHJDl3fAwAAAAsIBvLwJQHJTl9/PfpSZ46wVoAAACAeTCJEKIlOaeqvlhVR49t92ut/ShJxvsdJlBXN29+85uz6667ZrvttstrXvOaNc77zne+M8cff/ys07baaqv5KA8AAADmxSQGpty3tfbDqtohyaeq6tJ1feIYWhydJA9+8IPvdCGn7L1hs45jL7py3dZ7yin5xCc+kZ133nmDrh8AAGDKhj7euaPW9ThpY7cxbM+FsC2794Rorf1wvL8yyQeT7J3kx1X1gCQZ72fdsq21t7fWlrTWlixatKhXyRvUMccck8suuyxPecpT8oY3vGF1L4dVq1bl4IMPztKlS7N06dLbXQ40Sb773e/mUY96VJYuXZqXvOQlvUsHAACAO6VrCFFV/6Wqtp76d5IDklyc5CNJDhtnOyzJh3vW1dOpp56aBz7wgTn//POz3XbbrW4/4YQT8ld/9VdZvnx5zj777Bx11FG3e+4JJ5yQ5z3veVm+fHnuf//79ywbAAAA7rTep2PcL8kHq2pq3e9urX2yqpYneX9VHZnk+0me3rmuifv0pz+db3zjG6sf/+xnP8t11113m3kuuOCCnH322UmSQw89NC984Qu71ggAAAB3RtcQorV2WZI9Z2m/Ksnje9aysbn11ltz4YUXZosttljjfGOAAwAAAHc5G8slOu/2DjjggLz1rW9d/XjlypW3m2fffffNe9/73iTJmWee2a02AAAA2BCEEBuJN7/5zVmxYkX22GOPPOxhD8upp556u3ne9KY3ZdmyZVm6dGmuvfbaCVQJAAAAd1y11iZdwx2yZMmStmLFitu0XXLJJdl1110nVNFdi20FAAAL28ZwSclkYVxWMtk4tuddZVtW1Rdba0tmm6YnBAAAANCFEAIAAADoovclOgEAYEHRRRtg3ekJAQAAAHQhhAAAAAC6EEIAAAAAXQghOrv88suz2267rfP873znO/PDH/5wHisCAACAPu7WA1OuWn7cBl3eoqXLNujykiGE2G233fLABz5wgy8bAAAAetITYgJuvvnmHHbYYdljjz1yyCGH5Prrr88rXvGKLF26NLvttluOPvrotNZy1llnZcWKFXnmM5+ZvfbaKzfccMOkSwcAAIA7TAgxAd/85jdz9NFH56tf/Wq22WabnHLKKTn++OOzfPnyXHzxxbnhhhvysY99LIccckiWLFmSM888MytXrswWW2wx6dIBAADgDhNCTMBOO+2UfffdN0nyF3/xF/n85z+f888/P/vss0923333nHfeefn6178+4SoBAABgw7pbjwkxKVV1u8fHHntsVqxYkZ122iknn3xybrzxxglVBwAAAPNDT4gJ+P73v58LL7wwSfKe97wnj370o5Mk973vffPzn/88Z5111up5t95661x33XUTqRMAAAA2JD0hJmDXXXfN6aefnuc+97l5yEMekuc973m5+uqrs/vuu2fx4sVZunTp6nkPP/zwHHPMMdliiy1y4YUXGhcCZjhl7x0mXUKS5NiL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\n",
      "text/plain": [
       "<Figure size 1296x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# we will plot graph on Numbers of matches won by Toss result\n",
    "plt.figure(figsize = (18,10))\n",
    "sns.countplot('season',hue='toss_decision',data=data,palette='afmhot')\n",
    "plt.title(\"Numbers of matches won by Toss result \",fontsize=20)\n",
    "plt.xlabel(\"Season\",fontsize=15)\n",
    "plt.ylabel(\"Count\",fontsize=15)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>season</th>\n",
       "      <th>winner</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2008</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2009</td>\n",
       "      <td>Deccan Chargers</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2010</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2011</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2012</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2013</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2014</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2015</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2016</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2018</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2019</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    season                 winner\n",
       "1     2008       Rajasthan Royals\n",
       "2     2009        Deccan Chargers\n",
       "3     2010    Chennai Super Kings\n",
       "4     2011    Chennai Super Kings\n",
       "5     2012  Kolkata Knight Riders\n",
       "6     2013         Mumbai Indians\n",
       "7     2014  Kolkata Knight Riders\n",
       "8     2015         Mumbai Indians\n",
       "9     2016    Sunrisers Hyderabad\n",
       "0     2017         Mumbai Indians\n",
       "10    2018    Chennai Super Kings\n",
       "11    2019         Mumbai Indians"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# we will print winner season wise\n",
    "final_matches=data.drop_duplicates(subset=['season'], keep='last')\n",
    "\n",
    "final_matches[['season','winner']].reset_index(drop=True).sort_values('season')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjwAAAHWCAYAAABzOFPjAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzdd3xUVcLG8d9JpUPoRCCAKEVUxN4QY0EsUdAVXde2YnddV9ey6+p4163v2nWt2Ct2Y18lImIBRFFAY0N6rwESIJk57x93kCEkEGDmninP108+IXfak4DJk3POPddYaxERERFJZ1muA4iIiIgkmgqPiIiIpD0VHhEREUl7KjwiIiKS9lR4REREJO2p8IiIiEjaU+ERke1ijLnJGGONMYNcZ0kW0a/HGNc5RGRzKjwijkR/OFpjTMQYs/MW7vdBzH3P2cHXPCcezxNvxphBMZ/jhrdqY8w8Y8zLxpiBrjNuLxVDkeSQ4zqASIarwf//8Dzgz7VvNMbsAhwWc790NxN4LPrnJsDewFDgJGPMcGvtC66CiUhq0wiPiFsLgc+Bc40xdRWaEYAB3gg0lTszrLU3Rd+usdYeAfwJ/2vwf46ziUgKU+ERce8hoCNwfOxBY0wucDbwCTCtrgcaY/Y2xtxpjPnKGLPMGLPWGPODMeZWY0xBrfuOAR6NfvhoremjbjH3yzbGXGSM+dgYs9IYU2WM+dEYMzI64lRXjlOMMROMMZXRHM8ZY3bavi/HZh6Ovu9mjGlbx2vnGGMuMcZ8ZoypiGb40hhzmTFms+9xxpgSY8xoY8x8Y8y66LTZh8aYS2rdb4YxZkZdgRo6TRV9fCj6YezUpK7pIxKwTBgiF0l2zwK34Y/mvBpzvAToAFwH9KznsefjT/l8CLwPZAMDgCuBIcaY/a21q6L3fQxYAZwIvAZMjnmeFQDGmDzgTeBIYDbwDFABdIu+zjjgh1oZLolmLY3m2B8YDuxpjOlvrV3XoK9Cw9TEfhAtha8Dg4HvonnXAocDd0eznBlz/wuAB4AF0cctAdoDewDnAvfGMSvAHcBJ+NOSjwMz4vz8ItJAKjwijllrVxljngPOMcZ0ttbOid50Pn7ZeJ461vdE/RO41Fobjj1ojDkPGIlfRv4dfZ3HjDHgF55XrbWP1fF8N+GXndeBX8WWFWNMPtCijsccA+xrrZ0Sc99ngNOjr/V8vZ98w1wYfT/VWrui1m3X45ede4ArNnwdjDHZwIPAb40xL1prX4t5rvXAntbaRbFPVNfo0Y6y1t5hjGmFX3ges9aOifdriEjDaEpLJDk8hD8681sAY0wRcBTwtLW2sr4HWWtn1i47UY/gl6XBDQ0QLQmXAFXARbVHZqy166y1i+t46F2xZSfm8wHYr6GvH9UtOl10kzHm/4wxZcDN+J/LhbF3jE5XXYY/WvOH2K9D9M9XARY4o9Zr1ADVtV/YWrtkG7OKSArRCI9IErDWjjfGTMEfkfgb/vRWFhuLQ52iUzoXAqcBfYGWbPqLzLaso+kdffx4a+28bXjc53Ucmx19X1DHbVtSxMY1LxssB4qttZNrHd8VaIM/xfaX6OhVbVVAn5iPnwZuBaYZY0bhT8F9XE+RE5E0osIjkjweAu7CnyI6F5hkrf1yK48Zhb+2Zjr+upwFwIaRmSuA/G14/VbR93O34TEQXf9Ty4a1Ntnb+FwfWmsHARhjWgMn409XvW6M2ddauyDmvm2i73dh85IUq9mGP1hrbzPGLMEfyboc/2tkjTEfAldba+sqbyKSBlR4RJLHk/jrbR7AH5n565bubIzZB7/svA8ca62tjrktC7hmG19/Q3GJ19lVO8Rauwx4KLqQ+h78BcXDYu6yMvr+FWvtsNqP38LzPgE8EV1bcxD+1/C3wLvGmD4xa3siQF49T9OqnuMikqS0hkckSUQX5L4IdAbW4J+9tSUbztwqjS07UfsBjet4zIZ1LnWNvJTjl549jDGFDQodjPvxT8sfaow5OOb4hrwHRKf2tom1doW19i1r7fn4Z7C1Bg6NuctyoEM9z73PNrzUlr7mIhIQFR6R5PIX/BGHwTGnk9dnRvT9oNiDxpj2wH/reczS6PuutW+ILvS9F78o3R89Kyv2efOMMe22kinuork2TFn9I+Z4Df6p552Au4wxmxU8Y0wnY0zfmI+PqWeDx/bR97ELxCfgj4KfW+s5zwFii9fW1Ps1F5HgaEpLJIlYa2cBsxp494nAx8AwY8wn+HvkdACG4O9JU9fC40/xf6hfEV0jszB6/G5r7UrAw9+75gTge2PMG8AqoAtwNHA1Gy/9EKSX8fcNGmiMGWytfTd6/GZgT+Ai4IToWV1z8QvMLvjF5Hrgm+j9nwPWGmPG4RdGgz+qsy8wCX96cIO78cvOfcaYI/AXYu+JPw32BrU2ityCD/Cnx/5pjOmHP3KEtfZv2/D5i8gO0giPSIqKjnyUAPcBhfiLcA/B339nMHWfer0cfyHwN/g/zG+OvhVEb1+Pv2j6d/hl6Ozon/cDXsEvVYGz1lrgxuiHf4s5Xo2/sd9Z+CXvePzT0Y/B//52A/6ZWRtch1/6BuAvXD4XyAWuBQ6PnRq01n6DvyfRx/gF8AL8PXwOxC9HDc3+Lf7XcUH0NTd8zUUkQMb/PiIiIiKSvjTCIyIiImlPhUdERETSngqPiIiIpD0VHhEREUl7KjwiIiKS9lR4REREJO2p8IiIiEjaU+ERERGRtKfCIyIiImlPhUdERETSngqPiIiIpD0VHhEREUl7KjwiIiKS9lR4REREJO2p8IiIiEjaU+ERERGRtKfCIyIiImlPhUdERETSngqPiIiIpD0VHhEREUl7KjwiIiKS9lR4REREJO2p8IiIiEjaU+ERERGRtJfjOoCIpJFy0wgoiL61AvKA7Ji3LCD7niGX1Syd0TYbCNd6qwFWA8ujbxUhG7JBfxoikn5UeESkfuWmI9AD6Aa0Z2OZqf3WKvq+UUOetmJR83KgdwPuGvaMt5KNBWhFzJ83vC0DZgHTgZkhG1rfsE9ORDKJCo9IJis3TYDu+KUm9q179K2Ju3CAPyrUOvrWEBHPeHPxy8+Gt583/DlkQwsTklJEkp4Kj0gm8Kea9gD2jr71xS82HVzGSoAsoEv07bDaN3rGWwPMAH4AvgQmAZNCNrQgwIwi4oCxVtPjImml3DQG9sQvNgOi73cjiX7BuXHAlUuyq1q0dZ0jxjyi5YeNJWi+20giEk8qPCKprNzk4heafdg4etOHJCo3dblhwJXLcqpaNHSaypX5bFqCPg3Z0BK3kURke6nwiKSacrMbcCRwFP60TTO3gbZdEo7wNIQFvgLeA94HPgrZUJXbSCLSUCo8Ismu3HTCLzgb3grdBtpxKVp4alsLfIxfft4DvgzZUMRtJBGpjwqPSLIpN03xR26Owi84/dwGir80KTy1LQXK8MvPeyEbmuE2jojEUuERSQblpjUwDDgVGATkOs2TYGlaeGr7AXgJGBWyocmuw4hkOhUeEVfKTUvgJGA4/khOWpecWBlSeGJ9BzyPX36muQ4jkolUeESCVG6aAyX4JWcw/qUXMk4GFp5Y04BR+OXne9dhRDKFCo9Iovm7GR+PX3KOpYGXX0hnGV54Yk3GLz/Ph2xouuswIulMhUckUcrNocBFwIlAU8dpkooKT50mAg8DT4VsaI3rMCLpRoVHJJ7KTTPgTOBiYHfHaZKWCs8WVQBPAPeGbOhb12FE0oUKj0g8+JsBXoJfdpo7TpP0VHgabAxwL/BKyIZqHGcRSWkqPCLby7+sw8n4RedQx2lSigrPNpsPPAQ8GLKhua7DiKQiFR6RbVVuugAXAiNIv6uNB0KFZ7vVAK/jj/qMDtmQvoGLNJAKj0hDlZs9gb8AQ4Fsx2lSmgpPXHwH/Bt4UtNdIluX5TqASNIrN3tTbl4DvgROQWVHkkMv4BHgO894IzzjZczGlSLbQ4VHpD7lZj/KzRvA5/ibBRrHiUTq0gN/fc8PnvEu8oyXkZtZimyNCo9IbeXmQMrNO8B44DjXcUQaqAi4D/jJM95lnvHyXQcSSSYqPCIblJtDKTfvA5/gX/ZBJBV1Bu4GpnvG+71nvMauA4kkAxUekXIziHLzATAWOMJ1HJE4KQTuwC8+V3nGa+I6kIhLKjySucpNP8rNu8AHwCDHaUQSpSNwC/CjZ7zfesbT933JSPqHL5mn3LSn3DxgLZOBo13HEQlIJ/xrdU3yjHe46zAiQVPhkcxRbvIpN9dZy4/ABcbo9HLJSP2BMs94r3nG29V1GJGgqPBIZig3Q62lHPinMbrWlQj+VgtTPePd6hmvheswIommwiPprdz0iq7TedkYurmOI5JkcoEr8TcvPNsznvaakrSlwiPpqdw0p9z8x1qmoHU6IlvTEXgMGOcZby/HWUQSQoVH0k+5+ZW1fAf80Ri03b5Iwx0EfO4Z717PeJr6lbSiwiPpo9y0s9+aF4DnjaGT6zgiKSoLuBh/fc+RrsOIxIsKj6SHcvOrSIRvjOEU11FE0kRX4D3PePdrtEfSgQqPpLZy0zY8zbwIPJ+VRVvXcUTS0IXAFM942oVcUpoKj6SucnNKOMx32dmc7DqKSJorwh/tuc8zXjPXYUS2hwqPpB5/VOd54IXsbFq7jiOSIQxwEf5oT7HrMCLbSoVHUku5GRYOU56dza9cRxHJUN2A96Nncmm0R1KGCo+khnJTEJ5mRgEvZWfTxnUckQxn8M/k+toz3kDXYUQaQoVHkl+52bumhq+ysznVdRQR2UR3/Oty/Um7NEuyU+GRpLb2K3NpJMKnOTl0cZ1FROqUDfwDKPWMV+A6jEh9VHgkOZWbJhWfm1ca5XNPVpZ2SxZJAccDkzzj7e06iEhdVHgk6aycaPqsruTbFs04yXUWEdkm3YGPPeNd6DqISG0qPJJUlnxqzm7SmC+bNaGr6ywisl3ygfs94z3hGa+J6zAiG6jwSHIoN7nLPjOPtS3gsdwc8l3HEZEddiYw3jPerq6DiIAKjySBNV+aLhWrmdy6FWe7ziIicdUP/+rr2jdLnFPhEacWf2KOycnmmxbN6Os6i4gkRHPgec94t3nG088ccUb/+MSZWWXm8tYteSM/D+3WKpL+/gC8onU94ooKjwSupNiYH/9nHuhayJ3Z2WS7ziMigSkBPvCM1951EMk8KjwSqJt/bxrfdh1lPbtygessIuLEfsCnnvF2cR1EMosKjwTm/ptM4VknMrlnVwa5ziIiTvXALz0HuQ4imUOFRwLx7K1mz2FH8UVRITpFVUQA2gCjPeMNcx1EMoMKjyTca/eawccO5KP2bejgOouIJJVGwAue8a5wHUTSnwqPJNS7I82IwQdT2rI5zV1nEZGklAXc7hnvdp22Lomkf1ySECXFxox90vz9iAN5oFE+ea7ziEjSuwJ/v55GroNIelLhkbgrKTbZV53Lg4fuw59zsvVvTEQa7GTgbe3VI4mgH0YSVyXFptFlZ/DkwH0YYYzrNCKSggYBb6r0SLyp8EjclBSblhecynNHHcTpKjsisgMGodIjcabCI3FRUmw6nDuMUccdxokqOyISB4NQ6ZE4UuGRHVZSbDqcfRJPnXQEg1V2RCSOBqHSI3GiwiM7ZEPZGXYUR6rsiEgCDEKlR+JAhUe2m8qOiARkECo9soNUeGS7qOyISMAGodIjO0CFR7aZyo6IODIIlR7ZTio8sk1Kik2H047lMZUdEXFkEPCaZ7xc10EktajwSIOVFJsORxzAPcOHcLTKjog4dCTwkOsQklpUeKRBSopNh/69+c9Fp1GSrctFiIh7Z3vG+6vrEJI69INLtqqk2HTo0ombrz6Pofl5uhCoiCSNGzzjnec6hKQGFR7ZopJi06pVc64LXcrQ5k1p5jqPiEgt93vGG+w6hCQ/FR6pV0mxaZybw+9v+h2ntG9NW9d5RETqkAO84Bmvv+sgktxUeKROJcUmBxhx/UWc0aMznV3nERHZgubAW57xuroOIslLhUc2U1JsDDD8sjM4b0BfdnGdR0SkAToBb3vGa+U6iCQnFR6py+DhQ7jk6IPZ03UQEZFt0Bd4xTOeTq6QzajwyCZKis2+h+/PlacfxwGus4iIbIdBwKOuQ0jyUeGRX5QUm117dOaaS05nYFaW/m2ISMr6tWe8q12HkOSiH2oCQEmxKWyUx1V/vpCB+Xnku84jIrKD/ukZb6DrEJI8VHiEkmJTAFx13fkc3L4N7V3nERGJg2xglGe8jq6DSHJQ4clwJcWmEXD58GPZa8Bu7OY6j4hIHHUEnvOMl+06iLinwpPBoqef/7rfLvQffgyHuM4jIpIAhwF/dx1C3FPhyWyHtGjGUdeO4NCcHHJdhxERSZBrPOOVuA4hbqnwZKiSYlMEnHvjJezVsjltXOcREUkgAzzuGa+H6yDijgpPBiopNs2Ayy44lZ67dqOX6zwiIgFoBbzoGa+R6yDihgpPhikpNlnAuQf2p9eQgRzsOo+ISID2Au5yHULcUOHJPEe1b80hl5/JoGxtLigimed8z3hnuw4hwdMPvAxSUmx6AaddfzEDmjamues8IiKO3OsZTxdGzjAqPBkiurngpb85gU7dd6Kn6zwiIg41AR71jKefgRlEf9kZoKTY5AAXdOlIwUlHMsh1HhGRJHAw8PugXswY080YM3Ub7n+OMaYwkZkyjQpPZjgR6HvNCA7Iy9V1skREov7uGW9X1yHqcQ6gwhNHKjxpLrpu54RzhlJQVKipLBGRGI0JdmorxxjzuDHma2PMi8aYJsaYG40xE40xU40xDxrfKcA+wNPGmMnGmMYB5UtrKjxprKTYNAZGFBVSc/wgjnadR0QkCR0EXBHQa/UCHrTW7gFUAJcA91hr97XW9sMvYMdba18EPgfOsNb2t9ZWBZQvranwpLeTgDZXn8dhmsoSEanX3wKa2pptrf04+uengEOAw40x440xU4Bi0EWcE0WFJ01Fp7KOOXcYbbt20lSWiMgWBDW1Zev4+F7gFGvt7sBDgHaCThAVnjQUnco6v6iQ6uMO01SWiEgDHAT8IcGv0dUYc2D0z6cD46J/XmKMaQacEnPfVaD90uJJhSc9DQVaaypLRGSb/M0zXiKvL/gtcLYx5mugNXAf/qjOFOBVYGLMfR8D7tei5fgx1tYeYZNUVlJsegN/+u0wWp90JMe7ziNSlxsHXLkku6pFW9c5ROrwGXBwyIYiroNIfGmEJ42UFJsmwIiObakaMpAjXecREUlBBwAXuQ4h8afCk16GAq0vP5N98/O08E1EZDvd7BmvjesQEl8qPGkiOpV19CEDiPTtyV6u84iIpLDWwD9ch5D4UuFJAxvOyjKGZecM5Zgsg3GdSUQkxY3wjLe36xASPyo86eEYoODcYfRo34adXIcREUkDWcA9nvH0C2SaUOFJcSXFpiNwfJtWLB18MEe4ziMikkYOAM5yHULiQ4UnhZUUG4O/eVX1xadzUONGNHWdSUQkzfzDM14T1yFkx6nwpLbdgf69e7Bu777s7zqMiEgaKgSucR1CdpwKT4oqKTb5+EOtSy84lSOzs8l2nUlEJE1d7Rmv0HUI2TEqPKnrcKBN8QG07NmVvq7DiIiksSboNPWUp8KTgkqKTQEwzBjm//o4BrvOIyKSAc7yjDfAdQjZfio8qekEIGv4EHrqNHQRkUAY4F+uQ8j2U+FJMSXFpgtQbAzzjjmUw1znERHJIEd5xjvQdQjZPio8KSR6GvpwoPJXg+nVuiXtXWcSEckwN7oOINtHhSe17IZ/KvqiIQMZ6DqMiEgGOsYz3r6uQ8i2U+FJESXFJgs4DVh+8tH0atOKjq4ziYhkKI3ypCAVntSxO9AZWHHsYVq7IyLi0PE6Yyv1qPCkgOjozsnAypOOYJd2BXRynUlEJMNplCfFqPCkht2ArsDy4wdpdEdEJAmUeMbb03UIaTgVniQXPTNrGFBxwuHsrH13RESSggFucB1CGk6FJ/n1BboDy044XKM7IiJJZJhnvN1ch5CGUeFJYjGjO6uGDKR7x7Z0cZ1JRER+oVGeFKLCk9x6AzsDS08q1uiOiEgS+pVnvD6uQ8jWqfAkqdjRnYP2olOn9hS5ziQiIpvJAi53HUK2ToUnee0afVt6/CC0q6eISPL6jWe85q5DyJap8CSh6OjOUGBV2wIa9e5OP9eZRESkXs2As1yHkC1T4UlOO+Ov31ly2rH0z8kh13UgERHZootdB5AtU+FJTkcBawH224N9HGcREZGt280znk4uSWIqPEmmpNgUAPviXxG9e6vmtHGdSUREGuQS1wGkfio8yecAwAKRow/SYmURkRQy1DNeR9chpG4qPEmkpNjkAMcAS7p3pnn3zvRynUlERBosFzjfdQipmwpPctkNaAFUnXoMe2dl6e9HRCTFXOAZL9t1CNmcfqAml8HA6twcsvbqw96uw4iIyDbrDJS4DiGbU+FJEiXFphPQB1h28tH0btKYZq4ziYjIdtHi5SSkwpM8DgHCgD1sXy1WFhFJYUd4xtvFdQjZlApPEigpNo2AI4BFO3ehRWF7ujmOJCIi288AZ7gOIZtS4UkO/YF8YP2xA+lrjOs4IiKyg4a7DiCbUuFxLHrdrOOAFQB79tZ1s0RE0kBvz3h7uA4hG6nwuNcNf1X/yl7dadW+DTs5ziMiIvGhUZ4kosLj3j5ADcCQQ9nNcRYREYmfU10HkI1yXAfIZCXFJhs4FFgKsEcvFR4R2XHVVPMojxImTIQIfenL4RzOa7zGPOZhsbShDSdxEvnkb/LYOczhdV7/5eNBDKIPfVjDGp7jOdaylmKK6UMfAJ7lWY7jOFrQItDPMUX09Iw3IGRDX7gOIio8rvUAmgHLdutJ67YFdHIdSERSXw45nM3Z5JNPmDCP8Ag96clgBtOIRgC8wztMYAKHcugmj21Pey7gArLJZhWruI/72JVdmcIU+tOffvTjKZ6iD334ju/oRCeVnS0bDqjwJAFNabm1N/7eOww+RKM7IhIfBvPLyE04+p/B/FJ2LJYaajBsfkpoHnlk418ZIfY+2WRTTfUvx8KE+YzPOIiDAvqsUpamtZKERngciV4o9BBgCcAeu6rwiEj8RIjwAA+wjGXsx350pjMAr/IqP/AD7WjH0Rxd52PnMIfXeI0VrGAYw8gmm93ZnZd4ia/4iqM4iolMZE/2JI+8ID+tVNTNM97+IRsa7zpIplPhcWdnoCmwpH9v2rZuRQfXgUQkfWSRxcVcTBVVjGIUC1lIBzpwEicRIcJbvMU0prEXe2322M505lIuZTGLeYVX6ElPGtGIM6J76VVRxTjGMZzhlFJKFVUcxEF0oUvQn2aqOBVQ4XFMU1ru7AtUAxx9sEZ3RCQxGtOYbnTjR3785VgWWfSjH9/wzRYf24525JHHIhZtcvxDPmQgA5nKVDrRiRM5kdGMTkj+NHGqZzxtKeuYCo8DJcUmFziI6HRWv1202aCIxM8a1lBFFeCfsTWd6bSlLUv9E0KxWL7jO9rSdrPHLmc5YX9pIStYwRKW0IpWv9y+lKWsYhXd6EY11ZjofzX+7hpSt86gxU6uaUrLjZ5AI2D9bj1p3apFHd91RES20ypW8SqvEiGCxbIbu7ELu/Aoj7KOdVgsHenIcRwHQDnlzGMexRQzi1mMYxxZZGEwHMdxNKXpL889mtEcwREA9KMfz/Ec4xnP4Rzu5HNNISXAx65DZDIVHjf2I7rZ4MED6OE4i4ikmY505CIu2uz4eZxX5/17R/8D2DP6X31OjTnpqBnNGMGIHUybMY50HSDTaUorYCXFJg84EFgM0KeHCo+ISAbYyzNeG9chMpkKT/B2AfKA6qwsTOeOdHcdSEREEs5AdC5QnFDhCd4eRDcbPGQAhfl50Z3AREQk3R3lOkAmU+EJUEmxMfgXC10GsO/ums4SEckgKjwOqfAEqy1QAP75orsUqfCIiGSQIs94PV2HyFQqPMHqgT+PS/Om5HZoo21JRUQyjEZ5HFHhCdZeREd3Dt+PouwNV+gTEZFModPTHVHhCUhJsckG9gSWA/Tvo+ksEZEMVOwZT7/sOqDCE5ydgHyi18/q0YWd3cYREREHWuGfvCIBU+EJzi8L1bp0pGlBC9q7DCMiIs5oWssBFZ7g7A2sAhi4D92NrpsrIpKpil0HyEQqPAEoKTb5QC9gJcDOXSl0m0hERBzaxzOefu0NmApPMLrhn44eAShsr8IjIpLBWhCzzEGCocITjF6ABTAG2hbQ0XEeERFxa4DrAJlGhScYA4hOZ+3Wk9Z5ueQ7ziMiIm7t7TpAplHhSbCSYpMLdAHWAOzZS9NZIiKiwhM0FZ7E2zB9FQHo0YVODrOIiEhy0JRWwFR4Eq8T0etngRYsi4gIAK0842kD2gCp8CTezkAN+AuW27XWCI+IiACa1gqUCk/i9SK64WDfnbVgWUREfqHCEyAVngSKLljuzIYFy701uiMiIr9Q4QmQCk9idSBmw8EeXbR+R0REfqGFywFS4UmsQmIWLO/UXiM8IiLyiwLPeD1ch8gUKjyJ1YPogmWA1i11hXQREdnE7q4DZAoVnsTqTXTBcotm5DZuRFPHeUREJLl0dx0gU6jwJEjtBcu9ulHgNpGIiCQhTWkFRIUncTZZsNy1UIVHREQ2o8ITEBWexGkX+0FhOxUeERHZjApPQFR4EqeAmDO02rZW4RERkc1084xntn432VEqPInTGVi34YOCFio8IiKymcZsvMi0JJAKT+IUAms3fNCquQqPiIjUSdNaAVDhSZwOQBX4Fw1t1pRWjvOIiEhyUuEJgApPApQUmzygFbAeoKiQ5jnZ5LhNJSIiSUqFJwAqPInRiujp6AA9umh0R0RE6qXNBwOgwpMYBYDd8EHnDlq/IyIi9dIITwBUeBKjgJivbYc2KjwiIlIvFZ4AqPAkRntiprRaNqeZwywiIpLcOrgOkAlUeBJjJ2JOSW+cT2OHWUREJLnleMZr7jpEulPhSYxORE9JB8jPp5HDLCIikvx0ckuCqfDEWUmxMfjDk7+M8DTKU+EREZEt0lrPBFPhib88IBcIbziQn6cpLRER2SIVngRT4Ym/RsSckg6QrxEeERHZMhWeBFPhib/G1Co8ebkqPCIiskUqPAmmwhN/m0D3B5kAACAASURBVJSbghbkZWXp6ywiIlukwpNg+kEcf5sUnrYFWr8jIiJbpcKTYCo88dcYMBs+KGih6SwREdkqnZaeYCo88deImMLTSoVHRES2TiM8CabCE39NiCk8LZppSktERLZKhSfBVHjirzlQ88sHTTXCIyIiW6XCk2AqPPHXkpjCk5dLjsMsIiKSGvTLcYKp8MRfM2IKj05JFxGRBsh2HSDd6Ydx/G0ypWXMxvU8IiIi9dDP4wTTFzj+NhnhyVbhERGRrdMIT4Kp8MRfLhDZ8IGmtEREpAFUeBJMP4zjL4uYa2mZLI3wiIjIVqnwJJgKT/xtWnhQ4RGprevB366OEAm7ziGSRPTzOMH0BY6/Tb6m1m565XQRgRF3v93t7FH3rs7qMG+u6ywiSUK/ACSYCk/8bTLCE4lsXM8jIhv12GNJyxvGPLjT4aFR82vy1ixznUfEMRWeBFPhib9NC49GeES2aOBp33YKfX5Lwc7Dxs4Mm5q1rvOIOKLCk2AqPAmmwiOydTm51vzm72VFV4y+zTbvVz7TYjUyKplG/+YTTIUn/jYpOJrSEmm41p0qG1/5wnNFwx95cAUFi+e7ziMSII3wJJgKT/xFiDkzKxLRCI/Itupz4PzWoU/+2+mgP74ytyanaqXrPCIBUOFJMBWe+Nuk8Kxdx3qHWURS2lHnfbXTXybc0qzL4M9mhgnr/yVJZ6tdB0h3Kjzxt0nhqVhNlcMsIikvv3E4+7d3vFN02Tu31zTu+dMsi9WoqaSj5a4DpDsVnvjb5JtxxRp01olIHLQvWt3kmtef7HrSPY8ujTRbvtB1HpE4W+E6QLpT4Ym/TUZ4VlSo8IjEU/8jZrX1Jt7ZYa8L3ppdk7Vules8InGiEZ4EU+GJvypiromydIWmtEQSoeQPE7r86dNbGnU49IuZESI1rvOI7CAVngRT4Ym/1UDOhg8WL9cIj0iiNGlRnXvRg6VFI169uzK38+w5rvOI7AAVngRT4Ym/VcQUnsoqamrC6LdPkQTq0mt5iz+/93Dnwf9+amG4ccUS13lEtoMKT4Kp8MRfBZAbe2D9eo3yiAThgJIfO4Qm3N6mz69Hzwqb9ZWu84hsAxWeBFPhib8KYkZ4ANZVax2PSFCyc6w59YaPuv7xo9uyCwZMnRkhog3dJBWo8CSYCk/8rSZm0TLAOo3wiASuRZu1+Zc//WLRWc/cvyqr3YK5rvOIbIVOS08wFZ74q6LWFuFr16nwiLiy816LWt0w9v6dDrvhhXk1eWv0W7QkK/3bTDAVnvhbS63NB9eu05SWiGuDfj2t8MYJt7bsceJHM8OmRr+ESLJR4UkwFZ7426zcVK5V4RFJBrn5kawz/zW66Pejb7PN+nw/U5epkCSxNmRDKuEJpsITf5v9o11RgXaDFUkibTpVNr7q5WeKTh350HLbaskC13kk42kPqQCo8MRfFTGXlgCYv0RDlSLJqO/B81rf9Ok9Hfe/4rU5NTlVK13nkYw13XWATKDCE3+bjfDMnq/CI5LMjrnwy87Xj7+l2U5Hjp8RIbzedR7JOCo8AVDhib+11Brh+e5nljnKIiIN1KhJOHvE3W93u/itO6sb9fh5tkXLeyQwKjwBUOGJs9IyW4N/eYm8DceWrmCd9uIRSQ0du1c0vfbNx7uceNfjiyNNVyxynUcyggpPAFR4EmMB0Cj2wKo1mtYSSSV7HTWjXWjCHe33OO+d2TVZ61a7ziNp7WfXATKBCk9izAMaxx5YsUqFRyTVZGXB0D9+1uXaj2/Jb3fQ5BkRIroQsCTCT64DZAIVnsSYC+THHli2QoVHJFU1a1Wde8nDr3Y776V7KnMK5+gUYomn5SEb0hmCAVDhSYyl1NptedEyFR6RVNe177IW148e2fnofzy9INxo1VLXeSQtaP1OQFR4EmMFtQrPvEW6MJxIujhw6A8dQxNva93rtLJZYVNd6TqPpDSt3wmICk9iLKfWqek/z9EIj0g6yc6x5rTQ2K5Xjb01u2X/b2ZaIhHXmSQlaYQnICo8iVEBRIj5+v4wkxWRiDb2EEk3Lduuzb/i2eeLznjqgQrTZuE813kk5ajwBESFJwFKy2wEWELMqenrq4msqUIL00TS1C57L2x147j7Cg/904vzanLXaERXGkpnaAVEhSdx5lNrL57Fy9BFCkXSXPFZUwtvmHBry27HfzwzTM0613kk6U12HSBTqPAkzlxq7cUzZwHzHWURkQDlNYpknf2f94ouf//2cNPeP8yyWE1nS11mhWxoiesQmUKFJ3EWANmxB76fieb3RTJI253WNPnjK093PeWBkctsy6Ua4ZXaJrkOkElUeBJnOf7C5V98MU0jPCKZqN/AuW1u+uzujvte9vqcmuy1Fa7zSNJQ4QmQCk/iLKDWqelzFrJmTSX6ZieSoY69dFLn68ff0qTT4RNnRAhXu84jzqnwBEiFJ3GWA2uB3NiDi5ZplEckkzVqWpNzwb1vdrvwzbvW5RXNmG21W0UmU+EJkApPgpSWWQv8CDSPPT57gdbxiAgU9ljZ7E/vPNbl+NueWBRusnKx6zwSuNkhG9Lfe4BUeBLrO6BZ7IEfZmqER0Q22mfIz+1vmnh7u93PfXd2Tdb6Na7zSGA0uhMwFZ7EmkWta2p9MU0jPCKyqawsGHbNp12uHXdLbtv9v5oZIRJ2nUkSToUnYCo8iTWfWguXZy9gzZoqVjnKIyJJrFnB+rxLH3ul6NwX/rsmu9PcOa7zSEKp8ARMhSexlgFV1F64vFSjPCJSv279lrb4S9lDnY+4+dkF4fzVS13nkYRQ4QmYCk8CRRcu/0SthcvacVlEGuKQU77reOPEW1vvcsqYmWFTXeU6j8TNnJANLXIdItOo8CReOdB0kwM/o6FqEWmQnFxrfn3zmKI/fHCbabF7+UyLjWz9UZLkxrsOkIlUeBJvdu0DYyYwKxxGixJFpMEKOlQ1+sPzzxWd/vgDK2m9SNPiqe191wEykQpP4s2j1sLlVWuoXrBk8yIkIrI1vfZbUBD6+N7Cg695eV5NTuUK13lku7znOkAmUuFJvGXUsePyDzOZ7iaOiKSDI8/9uvCGibe06Drk05lhwutc55EG+zlkQz+5DpGJVHgSLLpw+TugRezxiVPQP3gR2SF5jSJZ5972btFl794ebrzLT7MsVtepSH6aznJEhScYX1Br4fLHXzJ/3XrWOsojImmkfdfVTa4pfbLrsPseWRppvmyh6zyyRSo8jqjwBGOz0ZxIBDtnAT+7CCMi6WmPQbPbehPu6jDg4jdm12Sv1QanyScCjHYdIlOp8ARjAbAGyI89+O10TWuJSPydcPnnXf706S2NOx42aWaEcLXrPPKLL0M2pI0kHVHhCUBpmY0AXwIFscfHfaGFyyKSGE2a1+RceP/rReeX3r02t8ssnRWaHDSd5ZAKT3C+AvJiD3zzI8tXrUGnlYpIwnTeZUXzP//vkS5D/u+pheHGFYtd58lwOh3dIRWe4Eyn1n48ADPmapRna1ZUwCm/h97HQp/j4NMv/eN3PwW9hsBux8M1/9n8cd/9DP2HbnxrsQ/c8bh/27W3wB4nwlnXbrz/k6/BnU8k/vMRcWG/E37scNPnt7Xb7cz3ZoWz1q9xnScDVQHjXIfIZCo8ASkts8vx1/JscrbWlO+1jmdrfv8POOYQKH8LvnoF+uwMH4yH10bD16/BtDfgj7/d/HG9usPkV/y3SS9Ck8Yw9EhYuQo+mew/NhyBKd9D1Vp47FW45PTgPz+RoGRlwSl//rjrHz+6Nbf1PlNmRIhox/fgjAvZkPZLckiFJ1iTgFaxBz4Yz8+RCNo7ox4Vq2Hs53DeKf7HeXnQqgXc9xxcdz7kRycJ27fZ8vOM/gx27gJFO/nf9NdXg7V+0cnNgf88DJf/BnJzt/w8IumgRet1eb978qVuZ4+6d3VWh3lzXefJEJrOckyFJ1jfANmxBxYupWr+YmY6ypP0ps+Gdq3h3D/DXsNgxF9gTSV8PwM+mgT7D4fDzoSJU7b8PM+9Bacf5/+5eVM4+Sj/+bp3hpbNYOJUOPGIhH86Ikmlxx5LWt4w5sGdDg+Nml+Tt2aZ6zxp7mXXATKdCk+wZgCWWl/3L79lqpM0KaAmDF98AxefBl++DE2bwL8egpoaWF4Bnz0H/7kaTv0D9e4xu349lJbBrwZvPHbNCH+q69Zr4Ya74K+/g5Ev+M/zt/uC+dxEksXA077tFPr8loKdh46dGTY12hA1/ibpchLuqfAEqLTMVuIvXt7kMhOvf8C3kQgRN6mSW+cO/tv+e/ofn3K0X4A6d4RhR4ExsN8e/jTVkuV1P8fbH8GAvtCh7ea3ffmN/37XbvDEa/D87TD1B/hhRiI+G5HklZNrzW/+UVZ0xejbbPN+5TMtVt+T4meU6wCiwuPCRGoVnvmLqZy7ULsu16VjO+jSyT/jCvy1OH17wklHQNln/rHvf/bX5LQtqPs5nn1z43RWbTfcBX+9HKpr/AXM4JenSv2OKxmqdafKxle+8FzR8EceXEHB4vmu86SJ510HEBUeF6bVdXDSN3UfF7j7ejjjav808snl8OcL4LfDYPoc6HcCnHYVPP5Pf7Rn3iI49oKNj62sgvc+8UeDanv1fdh3dyhs7y+EPrA/7F7iP8+evYP7/ESSUZ8D57cOffLfTgdc+ercmpyqla7zpLDPQjakdZpJwFhdXDdQJcXGAP8AcoHVG463b02jB/7K1dlZKqEiklzWVWWHn7r26Nkz39unMJvsvK0/QmJcGbKh212HEI3wBK60zFrgQ6B17PFFy1g7e7725BGR5JPfOJx93l1vd7vk7TuqG+88fZbVThoNZYEXXIcQnwqPG19Rx67Ln0/V2Voikrw6dlvV9Jo3nuh64t2PLY40W77IdZ4U8HHIhua4DiE+FR43FgBzgeaxB98Yw3fhMNr5VESS2l5HzmznTbyzff8L3p5dk7Vules8SUxnZyURFR4HotNaY6i16/KylaybNZ8fnYQSEdlGJ/5hfJc/fXpLo/aHfDEjQqTGdZ4kEwFedB1CNlLhcedr6pjWmjBF01oikjqatKjOvfih0m4jXr27Mrfz7Nmu8ySRsSEbWuA6hGykwuNIaZldBMym1p48b4zh+5ow+k1JRFJKl17LW/z5vYe7DP73UwvDjSuWuM6TBDSdlWRUeNwaQ61prZWrWP/DDO3JIyKp6YCSHzuEJtzeps+vR88Km+pK13kcqQSecx1CNqXC49YU/GmtTaa23hzLRDdxRER2XHaONafe8FHXP350a3bBgKkzI0Qy7WSM50I2tMJ1CNmUCo9DpWV2CfAz0DL2+NiJzF28HG3pLiIprUWbtfmXP/1i0VnP3L8qq92Cua7zBOi/rgPI5lR43PuQWut4AD75QqM8IpIedt5rUasbxt6/08DrX5hXk7emnsv8po0JIRv6wnUI2ZwKj3uT8XfjzI49OOptpqxbjy5hKSJp4/DfTCu8ccKtLXuc+NHMsKlJ1+9v97oOIHVT4XGstMyuBD4D2sUeX11JzdQfmOwmlYhIYuTmR7LO/Nfoot+Pvs026/P9TEtaXdBxKTo7K2mp8CSHD4D82gdfeY/P0+pbgYhIVJtOlY2vevmZolNHPrTctlqSLvvVPBqyoXQduUp5KjzJ4SdgHrXW8nz9PUvnLuJnN5FERBKv78HzWt/06T0d9/t96dya7LUVrvPsAAvc5zqE1E+FJwlELzXxFrX25AEYM16Ll0Uk/Q256Iudrp/wn6Y7HTFhRoTwetd5tsO7IRua7jqE1E+FJ3l8CVQDubEHX36P8jVV6OJ8IpL2GjUJZ4+4561uF791Z3V+9xmzLCk1p6/FyklOhSdJlJbZSvy1PO1jj9eEsV9MY5KbVCIiwevYvaLpdW891vWEOx9fFGm6YpHrPA0wE3jTdQjZMhWe5PIRkEOtnZdHvc2kcISIm0giIm7sffSM9qEJd7Tf47fvzKrJWrfadZ4teCBkQ/oeneRUeJJIaZmdC3wPFMQenzWf1eXT+dpNKhERd7KyYOjVn3W99uNb8tseOHlmhEiyXVy5ArjfdQjZOhWe5PMO0Lz2wSdLGRuJpNaEtohIvDRrVZ176SOvFp330j2VOYVz5rjOE+OekA2l++7RaUGFJ/lMBVYDjWIPfvMjy7+bwRQ3kUREkkPXvstaXD96ZOej/vHMgnD+qqWO46wGbnOcQRpIhSfJlJbZauBdai1eBni6lLGRFDttQUQkEQ4a+n3H0Oe3te516gczw6a60lGMe0M25Lp0SQOp8CSncUAYfwHzL77+nqU/zGCqm0giIsklO8ea07wPi64ae2t2y/7fzLREglw4vAa4JcDXkx2kwpOESsvsCuA9oGPt2555Q6M8IiKxWrZdm3/Fs88XnfHUAxWmzcJ5Ab3s/SEbWhzQa0kcqPAkr/ej7zcZ5fnyW5b8NItvHOQREUlqu+y9sNWN4+4rPPS6l+bV5FYmciFxFfCfBD6/JIAKT5IqLbPL8EvPZqM8z77JWF1UVESkbsVnTym8YcItLbsd//HMMDXrEvASD4ZsaGECnlcSSIUnub2HvwlhduzBz6eyaPpsvnUTSUQk+eU1imSd/Z/3ii5/7/Zwk14/zrLE7dfEtcC/4/RcEiAVniRWWmaXAmVAp9q3PfcWH2qUR0Rky9p2XtPk6lef6nrKAyOX2RZLF8ThKR8O2dD8ODyPBEyFJ/n9D//vaZNRnvFfs3DGXL5zE0lEJLX0Gzi3zU3j7+6472Wvz6nJXluxnU+zHvhXPHNJcFR4klxpmV0MjKGOtTzPvcUYjfKIiDTcsZdO6nz9+FuadDr885kRwtXb+PCRIRtKpl2eZRuo8KSGd/BHeDYZ5fl0Mgu++1nX2BIR2RaNmtbkXHDvG0UXvn7XuryimbMbuNNHBeAlOJokkApPCigts4vwr6S+2SjPA6MYXVPDtv6WIiKS8Qp7rmz2p3ce7XL8bU8sCjdZubU9df4ZsqFFgQSThFDhSR1v4+/Js8nf2U+zqRg/hU/dRBIRSX37DPm5/U0Tb2/X75z/zarJWr+mjrvMAG4POJbEmbFaBJIySorNecABwNzY4y2akfugx+VNGtPMTTIRkfSwenne+seuOH7e4gn9umSRtWEZwekhG3rOaTDZYRrhSS2v4e/Lkxt7sGI11f/7hDI3kURE0kezgvV5lz3+creznr23Kr/Tgh+BT1V20oNGeFJMSbE5CSgBZsUez8rCPHQz57cr2HzPHhER2XbWYudNKdxvp1Pnfu46i+w4jfCknv8BlUCT2IORCPbJ13hL/VVEJD6M4TGVnfShwpNiSstsJfAs0L72bWMmMOfb6XwVfCoRkfRiLSuA61znkPhR4UlN44E5QEHtG/77NO+tryYRF8sTEckYxhCit9Vp6GlEhScFlZbZGuBpoBX+IuZfzF7Amg8nMMZFLhGRdGAtU4D/us4h8aXCsx2MMZcbY741xiw3xmxxyNMYc44x5p56blu9AzHKgQnUsRnh/aOYsHwlW9tES0RE6mAMv6O3DbvOIfGlwrN9LgGOtdYWWGudXEiutMxa4Hn8y03kxd5WXUPk4Zd4LRJp2H7pIiLyiwfpbT90HULiT4VnGxlj7gd6AKXGmD9sGL0xxrQzxrxkjJkYfTu4jsd2N8Z8Gr395h3NEr2w6Cuw+anoYz9n7sSpfLKjryEikikillnAH13nkMRQ4dlG1tqLgHnA4cDymJvuBG631u4LnAyMrOPhdwL3Re+zIE6R3geWAi1q33Dbo3ywvEJTWyIiDZFlOI/edpXrHJIYKjzxcyRwjzFmMlAKtDDGNK91n4PxTykHeDIeL1paZtcBTwBtqLWAuWod4ZEv8KqmtkREtiwS4UF62/dd55DEUeGJnyzgQGtt/+jbTtbW+ZtCIsrHFOAzoLD2DR9NYt6EKXycgNcUEUkL4TBzsrI0lZXuVHji53/AZRs+MMb0r+M+HwOnRf98RrxeOLqA+RlgPdC09u23P8YYnbUlIrI5a7HZ2Zyjqaz0p8ITP5cD+xhjvjbGfANcVMd9fg9caoyZCLSM54uXltmVwCP4OzBvPrX1oqa2RERqi0R4iN52tOsckni6eGgaKSk2Br9oDQDm1r79zxdyxAF7ckjgwUREklA4zOzsbPrS2+7InmiSIjTCk0a2NrV126Oa2hIRgU2mslR2MoQKT5qJTm09DHSg1tTW2vWEH/LP2oo4CScikiSiZ2WVuc4hwVHhSU9fAp9Qx1lb475g3qdfMS74SCIiyaEmzIzsbJ2VlWlUeNJQzNTWOuqY2rr1EcbMXciMoHOJiLgWibA+J5uhmsrKPCo8aaq0zFZQz9RWTRj7jwd4sbIKnYYpIhklHOEyetvJrnNI8FR40ttk/L1/dqp9w+wFrBn5Ii9qPY+IZIrVlYzK7Wcfcp1D3FDhSWPRqa1ngUrquNbW+58y64PxaP8JEUl7qyuZ3qwJ57rOIe6o8KS56NTWvfjX2sqtffudT/LJ9NmUBx5MRCQg66tZi2UIvW2V6yzijgpPBigts+XAKKBzXbfffB+vVqxmWbCpRESCsXI1I5rtbb93nUPcUuHJHO8AX1DHep6lK1h391M8XxOmJvhYIiKJs3QFI9sdaJ92nUPcU+HJEKVlNoJ/ra0KoKD27eO/ZuEbY3gr8GAiIglSsZqv27TiYtc5JDmo8GSQ0jK7CrgbaA7k1779kZf4ctqP6HRNEUl5a9dRkZ/HMfS2GrkWQIUn45SW2RnA4/hTW6b27X+/nzeXrmBB0LlEROIlEsFWVnFa/h52vusskjxUeDLT2Ohbl9o3rK6k5m/38ewabUooIilqwRKua32Afdt1DkkuKjwZKLo/z9PAfKBt7dt/mk3F7Y/x9Ppq1gUeTkRkB8yaz+OFA+3/uc4hyUeFJ0OVltkq4B78vXma1L59whQWPvoyz4e1E7OIpIiZ8/jk4y+0uaDUTYUng5WW2fnAQ0BHILv27W9+yPTXRlMaeDARkW00bxE/f/olR59+lbWus0hyUuGRScArQFfqWMT82Ct8NW4SY4IOJSLSUEtXsPStsRxx2lV2jesskrxUeDJcdD3Pa8A4/NKzmf97mA+n/ciXgQYTEWmA1ZVUjv6M40b8xf7sOoskNxUe2bAp4ePANOq5/MSNd/HGrPn8FGgwEZEtWLee6rETOfPUK+x411kk+anwCAClZXY9cD+wAGhf+/bqGiI33Mnz2qNHRJJBOIIdN4lrj73Qvuw6i6QGFR75RWmZXQ3cAawHWte+fXkF673/8szqSioCDyciEuOzydxz55Pc4TqHpA4VHtlEaZldAtyGf+mJZrVvnzGXVbc+ylNr11EVeDgREeCLb3jl3yO5IroGUaRBVHhkM6VldhZwF/6mhJtdc2vSNBbf9hhPqPSISNAmfM17N93D8OjaQ5EGU+GROpWW2Wn4e/TsBOTUvv2zr1ig0iMiQfr4C8b+7X6GlpbZatdZJPWo8MiWfAK8iH+6+mb/VlR6RCQoH05k/L9HMrS0THvtyPZR4ZF6RefH3wDKgCLq2JhQpUdEEq1sPJNufZRTSsvsMtdZJHWp8MgWRefJn8LfmLAbKj0iEqCy8Uy643FOLS2zc1xnkdSmwiNbVVpma4BHUekRkQDFlJ3prrNI6lPhkQZR6RGRIKnsSLyp8EiDqfSISBBUdiQRjNW+TbKNSopNDnAucAgwA9jsH9EBe9LxynM4s1E+TQKOJyIpbPRnTLrzCZUdiT8VHtkuDSk9fXtS8Kfz+U3L5ptfpkJEJFYkgn35PT564jXOVdmRRFDhke3WkNLTqR1N/vo7Tu/Qtu6rsIuIVFdTPfJF3n/7Iy5T2ZFEUeGRHdKQ0tOsCTk3X86wnbvSJ+B4IpLkKquovOVR3v58Kteo7EgiqfDIDospPYfil57NrnGTlYW58RIGD+jL/gHHE5EktWwly/96L29Pn80NKjuSaCo8EhclxSYbOBUYAswG6rzWze/O4IAjD2Kw2ez8LhHJJLMXMP+mu3l18XL+WVpmZ7vOI+lPhUfipqTYGOBI4DfAAqj71PThx9J3+BCG5mRvflFSEUl/U39g+s33MqpqHbeWltmlrvNIZlDhkbgrKTZ7A5cCK4CKuu5TfABdLhrO6Y3yaRxoOBFxauznTLv1UR61lvt1IVAJkgqPJERJsekJXIm/nmdJXffZY1faXDOCM1o0oyDQcCISuIjFvvw/Jj7xGg8AT5aW2TqnvUUSRYVHEqak2HTCLz0tgPl13aewPU3+cjGndO5A90DDiUhg1q5j7YPP8/H7n3IPUBq9KLFIoFR4JKFKik0r4HL8S1HMqus+WVmYa85j0IH9GajFzCLpZeESFvz9AcbNmMtdwLjSMv3QETdUeCThSopNY2AEsA8wkzpOW/fvR88zSxiWn6d1PSLp4POpfP2vh5i4vprbS8vsNNd5JLOp8Eggonv1DAcGs4XT1nftRstrR3Bqu9YUBplPROKnuobq597iwxfeYRpwe2mZnek6k4gKjwQmetr6UcCvgWXUcwZXozyyr7+IY/bszT5B5hORHbeigiX/GslH3/zIFODu0jJb50kLIkFT4ZHAlRSbXvinredTz2JmgN+UsPvQIzkhN4fcwMKJyHYrn863f72XyasreRd4rrTMrnOdSWQDFR5xoqTYFAAXAH3wp7jCdd1vQF/aXXEWp7ZqQdsg84lIw4XDhN8Yw7iHX+In4GHgUy1OlmSjwiPORNf1nBh9WwjUuQlZy+bk3XgxJbt0Y7cg84nI1q2uZOUdTzB2wteU409h6TIRkpRUeMS5kmKzJ3Ax/tlbi+q73zlD2fO4wzgmP49GgYUTkXp9+xNT/zWSactXMhZ4XDsnSzJT4ZGkUFJsOgCXAF2AOdRz6nr3zjS/8hxOKCpklyDzichGlWtZ/czrlJV+wHLgaWC0NhOUZKfCI0mjpNjkA6cBRwDzgLX13ffcYfQ/43IU7AAAC/BJREFU7jCOycslP6h8IgLf/cyUfz3El0tXsAK4p7TM/uA6k0hDqPBIUomeun4gcB7+1dbrPaV15y60+MM5nNC1Ez2DyieSqarWsmbU27z18ntUAtOAh0rL7ArXuUQaSoVHklJJsemCfxbXhimumvru+9uT2evYgQzWaI9IYnz3M1P+PZLxS5aTA7wEvFNaZuv9f1IkGanwSNIqKTZ5wBDgJGA1sLS++0ZHe0q6dmLnoPKJpLuqtax5/h3eful/rMHfPuKh0jJb5zXxRJKdCo8kvZJiU4Q/2rMTWxntOe9k9hqi0R6RHfb9DKb+eyTjFy8jG3gZf1SnzkvCiKQCFR5JCTGjPUOBVWxltOfSMxjcsyt9g8onki5WrWHFS//jvehandnASF0LS9KBCo+klJJi0w04nwaM9gwZSPfTj+VY7dIssnU1YWo+m8y4u5/i26p1NAZeAd7WqI6kCxUeSTnR0Z5j8Xdo3uLanrxcsi4czv6H7cthmuYSqdv02ZT/9xne/2EmzfF/kXhIozqSblR4JGXFjPYUAnPZwmhP1040u+R0juizM/2NCSafSLJbXsHiF97h3TfGsAJozsZRnfWOo4nEnQqPpLSY0Z4SYD3+Nbnq/Ud90F50OutEBhe2pyigiCJJZ+06Kkd/xgcjX+SbcJgOwCzg4dIyO8NxNJGEUeGRtFBSbDrh79LcH3+Kq2JL9//VMfQ+sZijWjSjdRD5RJJBOEx40jQ+u/dZPl62krbAOmAU/9/evT41dedxHH+fBMiFiwRBCIoXtN7bekHbqdXa7G2c7mTabrczO7uznT7aP2qfbae705l90E133VtNrbZbR6xWC14BF6mAIiZcE5Scsw9+h5KyyEUhwOHzmjmTIER/Gkw+/C7fL3ypujridQo84hlulebngfeAKqAHM+szrZJifL97l8NHmzgWDBAq0DBFCs5xoK2T1t//mU+vd1AMlAJJ4ONE0pnxhwMRr1DgEc9xe3L9GHOE3cEEnyc2NlxTTsn7b3PolX28EgwQLtAwRRad7eC0d3L1Tyc5c6GFUaAGaAM+0PKVrDYKPOJZ8Zi1FlOl+SgwAvTN9PXlpRS//xZNRw5wJBSktBBjFFkMto1zq5OWP/6VM5euMQhEgTSms/lFdTaX1UiBRzwvHrO2AL8CdmCakQ7N9PVlYYree5ODRw9yJByivBBjFFkIto1z4zZXPvyEs1duksYEHRtTKfmzRNIZW9oRiiwdBR5ZFeIxywe8CPwaqMbM9ozM9JhQAP97b3HgtSZeLQ1TUYBhijwV28a+1sHlDxKcvdrGAFALlACfAQl1NRdR4JFVxj3G/hLwNlCJOdE1PNNjgiX4f/sm+48f5tWyMGsKMEyROcnlyF1t5/If/sLZG7cZxASdYuAc8LdE0rm7tCMUWT4UeGRVcoNPE/AO5kRXP7MsdZUU4/tNnBePHeSlqkpqCzBMkWk9esxYyy2++fATvrrVyTCTQecL4GQi6fQs7QhFlh8FHlnV4jGrGDiICT7VzCH4AMRepuHEUQ5t28huvx//Ig9TBID+NL1fXqT5o7/z7dAINlAH+IGzmArJvUs7QpHlS4FHBIjHrCJgP/BLYB3wkFmKFwJsqKX03RPsb9pLk5a7ZDHkcuRuddJ68gzNp8/zHSbgRAEfcBr4RyLp3F/KMYqsBAo8Innc4LMPM+NTB6SAgdke5/Nhvfkjnou9zKGGOrapX5c8q6ER0s0tXPjoJJd6+hgFijDfkxamaOC/EklnxlILIjJJgUdkGvGY5cec6noH89P0GHCfGQoYTti9jcgvfkLT89vZrwrOMh+2g9PVQ9upr2hOfEabbeNgqiKvxXzvnQL+nUg6D5Z0oCIrkAKPyAzc4+zbgBhwCPPTdR+Qme2x4RBF7/yU3Ydf4PkNtTT6fPgWd7SyUg0M8bC1jZaPT3HpegdpzPdZDRDC7Cs7CTQnks6s+8tEZHoKPCJzFI9ZEcyR9hNABaaOTz8zdGefUFdN6OfH2XVgD3vra9js86FFr1VuaIR0axstyXO0nrvMxGbjAGYPmQVcAj4FbiaSTm6pxiniFQo8IvPk7vPZDfzMvc1hlrue2Kg034ZaSt84zq79u9hbV8NGn6Xws1oMjzJwrZ3W0+dpPfs13XmfqsKE6GHgn8BXWrYSWVgKPCLPIB6zosARTLPSAKZf0aybnCdsqqfsjePs2beTPbVradBmZ+8ZzTB0/TZXT5+n5fNmvst7yS3GzOYUAe2YZauWRNKZU3AWkflR4BFZAPGYFcSc7joBbMQscz1klirO+bZtpOLEMfbs3spzddVsVH2flSs9RP/tLtq/uMjVU+e4424+BhNuqjFtHx4DZ4DPgbuJpF6MRRaTAo/IAorHLAtT9fYF4HXMMWIbE35m7N2VryxM0fHDbNq3i8atDTRWraFOsz/LVybLSFcvt1vbaD97gY62Oz+o4eTHnLIKAuNAM6b1w0018xQpHAUekUXihp8o5nj7ccypGwez0Xl0Pr9X/TrCrx+mce92GjfV06gih0trPMd49306b/2XjnOXaT//LfemvJT6MftyQpg9XheB/wA3EkknW/ABi4gCj0ghuOFnPaaa82uYN0MbE35mPeI+1QvbWfvKARp3bqFxfS2bAyUEF3TA8gO2jd2fpre9i46LrbR/3kxXZoypJ6d8mOc1jHluvwG+BK4nks68n2MRWVgKPCIF5oafBuAAcAzTtR3Mklca/u+NdEaWBbu2EnlxB/VbG4jW11JfEyGqEPR0bBs7NUhf7wO6O+/Sc7WD7out3BseZXyaLy/FPH9+zOzdFUzIuZZIOnNewhSRxafAI7KE8pa9tmIC0B74frPyoHs91X9SNwRFGxuIrq+lfl0V0UCJKj/ny9nY6UHu9/TR09lN97V2ei60cm80M224AbPZOII5kWcBvcDXwDXgdiLpzGupUkQKR4FHZBlxu7dvBLYDTcAWTOCxMX29nukNdccWKvftJNoQpaa6kkikgkh5GZFwiHIv1wN69JixwWFSA0OkHg6Q6n3Aw+sd9Fxo4d40S1P5/JgZnFL34xFMQcArQHsi6aQWeegiskAUeESWsXjMKsWEnt2YAFTtfiqHOfI+zDyXwKYTLMG/fTOVm9cTqV9HpKaKyqo1RCoriJSXEikpJvCsf8ZiytnYI6MMDA6TSg2S6kuR6u0j1dVDqu0O6Xv9c94nFQTKmdyHk8PM3nyNqZXTk0g6s/ZTE5HlR4FHZIVwl7+qgM3utRPYxOQSmAMMsUAhKF/tWkJ11YQrKwitKSdYUUaoLEywLEQoHCIYChIMBQgFAwQDJYQCJQRLign6fPgtC59lYT1pBslxwHGwHQfHcbAfj/No7BGZsUdks4/IZMfIjmbJjGbJjmbIDo+SGRohOzhMJj1Itj9NprObofHcvJf+QkCZe2tjNh2ngFvADaAL6EwkncdP/y8nIsuFAo/ICuZ2dV+H2Qe0BdiBCUN+zB4TGxOCRuCJ+1IKxufDKvKb8JOzccZz2AV4CbKYnLkJYoKhhamNdNO97mJmb+ZcKFJEVhYFHhGPcUNQDVDP5EzQBsybvY15s7cwASgDZN1rJb8YFGP+fiH4fvltItgAPMAsSd0AuoFunaISWV0UeERWAXc5LIQ5YVTp3kYxtYGiTO4NmggJFqb1wXjelf9xIfgwrRiKMIEm/76fyWU7H2Yzdy/QA3yHqW+Ucq8BdRsXEQUeESEes3zAGkwQimD2Ck108C5zb0vda+Jou8MPZ4UmglL+x86UX5t4XP79qS9CPiZnoIYxy3HDmKW5IcxR/T4mA01ahf1EZDYKPCIyL244CmCCTzDvNoiZeZkILNaU+zaTASf//hhmSS0z5XZcDTVFZKEo8IiIiIjn+ZZ6ACIiIiKLTYFHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDxPgUdEREQ8T4FHREREPE+BR0RERDzvf/RcvOZltzhgAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# we will plot pie chart on Winning percentage in final\n",
    "match = final_matches.win_by.value_counts()\n",
    "labels=np.array(Toss.index)\n",
    "sizes = match.values\n",
    "colors = ['gold', 'purple']\n",
    "plt.figure(figsize = (10,8))\n",
    "plt.pie(sizes, labels=labels, colors=colors,\n",
    "        autopct='%1.1f%%', shadow=True,startangle=90)\n",
    "plt.title('Match Result',fontsize=20)\n",
    "plt.axis('equal',fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Toss=final_matches.toss_decision.value_counts()\n",
    "labels=np.array(Toss.index)\n",
    "sizes = Toss.values\n",
    "colors = ['#FFBF00', '#FA8072']\n",
    "plt.figure(figsize = (10,8))\n",
    "plt.pie(sizes, labels=labels, colors=colors,\n",
    "        autopct='%1.1f%%', shadow=True,startangle=90)\n",
    "plt.title('Toss Result',fontsize=20)\n",
    "plt.axis('equal',fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 1296x720 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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sBtwi+3H130/ADatp6wJ/NX2Fn2eey1wF/BP4AHbM0cZa0RELGikSQL4NrA/8J3ODtsv7zyW9Dngjgmev53t20YWXURETGikScL26ZJm9DsmScDLgO1HGUNERCy+NtskngncbPvKAccNnCRpjqRZDcYVERHVqKubJrIHcPgEx7e2fYOktYGTJV1u+/Tek2oCmQUwffr00UQaETFFtXInIWk54EXADwadY/uG+v0W4GhgywHnHWh7pu2Z06ZNG0W4ERFTVlvVTc8GLrc9t99BSatKWr3zGNgJuKTB+CIighEnCUmHA78BNpU0V9Lr66Hd6alqkvRIScfVzXWAMyVdCJwL/Nz2CaOMNSIiFjTq3k17DNi/V599NwC71sdXA5uPMraIiFi4jLiOiIiB2uzdFA16x7UbNVbWl2dc03f/Rtc+q7EYrpmxQEe4rji+12Acr2qsrIhRyJ1EREQMlCQREREDJUlERMRASRIRETFQkkRERAyUJBEREQMlSURExEBJEhERMVCSREREDJQR1xEt2Oi4axsr65pdZzRWVix9cicREREDJUlERMRASRIRETFQkkRERAyUJBEREQMlSURExEBJEhERMdBIk4SkgyXdIumSrn37SfqTpAvq164DnruzpCskXSXpfaOMMyIi+hv1ncS3gZ377P+C7S3q13G9ByUtC3wV2AV4LLCHpMeONNKIiFjASJOE7dOB2xfjqVsCV9m+2vZ9wBHACyY1uIiIWKi2puV4m6TXALOB99j+S8/x9YDru7bnAk/r90KSZgGzAKZPnz6CUCOWXhu98NpGyrnmmBmNlBOTr42G668DGwNbADcCn+tzjvrsc78Xs32g7Zm2Z06bNm3yooyIiOaThO2bbf/T9oPANylVS73mAht0ba8P3NBEfBERMU/jSULSul2b/wVc0ue084BNJG0kaQVgd+DYJuKLiIh5RtomIelwYFtgLUlzgX2BbSVtQak+uhZ4Uz33kcBBtne1/YCktwEnAssCB9u+dJSxRkTEgkaaJGzv0Wf3twacewOwa9f2ccAC3WMjIqI5GXEdEREDJUlERMRASRIRETFQkkRERAyUJBEREQO1NS1HRAQAr9ro2sbK+t41Mxora2mRO4mIiBgoSSIiIgZKkoiIiIGSJCIiYqBFbriWNA14IzCj+3m2Xzf5YUVExDgYpnfTT4AzgF8A/xxN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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# we will print name of top player in IPL\n",
    "plt.figure(figsize = (18,10))\n",
    "top_players = data.player_of_match.value_counts()[:10]\n",
    "fig, ax = plt.subplots()\n",
    "ax.set_ylim([0,20])\n",
    "ax.set_ylabel(\"Count\")\n",
    "ax.set_title(\"Top player of the match Winners\")\n",
    "top_players.plot.bar()\n",
    "sns.barplot(x = top_players.index, y = top_players, orient='v', palette=\"hsv\");\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "city          winner               \n",
       "Bangalore     Kolkata Knight Riders    1\n",
       "              Sunrisers Hyderabad      1\n",
       "Chennai       Chennai Super Kings      1\n",
       "              Kolkata Knight Riders    1\n",
       "Hyderabad     Mumbai Indians           2\n",
       "Johannesburg  Deccan Chargers          1\n",
       "Kolkata       Mumbai Indians           2\n",
       "Mumbai        Chennai Super Kings      2\n",
       "              Rajasthan Royals         1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We will print IPL Finals venues and winners along with the number of wins.\n",
    "final_matches.groupby(['city','winner']).size()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Mumbai Indians           4\n",
       "Chennai Super Kings      3\n",
       "Kolkata Knight Riders    2\n",
       "Rajasthan Royals         1\n",
       "Deccan Chargers          1\n",
       "Sunrisers Hyderabad      1\n",
       "Name: winner, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print number of season won by teams\n",
    "final_matches[\"winner\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>winner</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>bat</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Rajasthan Royals</td>\n",
       "      <td>field</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>field</td>\n",
       "      <td>Deccan Chargers</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>bat</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>bat</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>bat</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>bat</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>field</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>field</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>bat</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>field</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>bat</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    toss_winner toss_decision                 winner\n",
       "0                Mumbai Indians           bat         Mumbai Indians\n",
       "1              Rajasthan Royals         field       Rajasthan Royals\n",
       "2   Royal Challengers Bangalore         field        Deccan Chargers\n",
       "3           Chennai Super Kings           bat    Chennai Super Kings\n",
       "4           Chennai Super Kings           bat    Chennai Super Kings\n",
       "5           Chennai Super Kings           bat  Kolkata Knight Riders\n",
       "6                Mumbai Indians           bat         Mumbai Indians\n",
       "7         Kolkata Knight Riders         field  Kolkata Knight Riders\n",
       "8           Chennai Super Kings         field         Mumbai Indians\n",
       "9           Sunrisers Hyderabad           bat    Sunrisers Hyderabad\n",
       "10          Chennai Super Kings         field    Chennai Super Kings\n",
       "11               Mumbai Indians           bat         Mumbai Indians"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print toss winner, toss decision, winner in final matches.\n",
    "final_matches[['toss_winner','toss_decision','winner']].reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>winner</th>\n",
       "      <th>player_of_match</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>KH Pandya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Rajasthan Royals</td>\n",
       "      <td>YK Pathan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Deccan Chargers</td>\n",
       "      <td>A Kumble</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>SK Raina</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>M Vijay</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>MS Bisla</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>KA Pollard</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>MK Pandey</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>RG Sharma</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>BCJ Cutting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>SR Watson</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>JJ Bumrah</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   winner player_of_match\n",
       "0          Mumbai Indians       KH Pandya\n",
       "1        Rajasthan Royals       YK Pathan\n",
       "2         Deccan Chargers        A Kumble\n",
       "3     Chennai Super Kings        SK Raina\n",
       "4     Chennai Super Kings         M Vijay\n",
       "5   Kolkata Knight Riders        MS Bisla\n",
       "6          Mumbai Indians      KA Pollard\n",
       "7   Kolkata Knight Riders       MK Pandey\n",
       "8          Mumbai Indians       RG Sharma\n",
       "9     Sunrisers Hyderabad     BCJ Cutting\n",
       "10    Chennai Super Kings       SR Watson\n",
       "11         Mumbai Indians       JJ Bumrah"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print man of the match\n",
    "final_matches[['winner','player_of_match']].reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(final_matches[final_matches['toss_winner']==final_matches['winner']]['winner'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>runs by fours</th>\n",
       "      <th>fours</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batting_team</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Chennai Super Kings</th>\n",
       "      <td>8772</td>\n",
       "      <td>2193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Deccan Chargers</th>\n",
       "      <td>3828</td>\n",
       "      <td>957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delhi Capitals</th>\n",
       "      <td>968</td>\n",
       "      <td>242</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delhi Daredevils</th>\n",
       "      <td>8632</td>\n",
       "      <td>2158</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gujarat Lions</th>\n",
       "      <td>1840</td>\n",
       "      <td>460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kings XI Punjab</th>\n",
       "      <td>9832</td>\n",
       "      <td>2458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kochi Tuskers Kerala</th>\n",
       "      <td>680</td>\n",
       "      <td>170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kolkata Knight Riders</th>\n",
       "      <td>9736</td>\n",
       "      <td>2434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mumbai Indians</th>\n",
       "      <td>10352</td>\n",
       "      <td>2588</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pune Warriors</th>\n",
       "      <td>2100</td>\n",
       "      <td>525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rajasthan Royals</th>\n",
       "      <td>8140</td>\n",
       "      <td>2035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiant</th>\n",
       "      <td>788</td>\n",
       "      <td>197</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiants</th>\n",
       "      <td>684</td>\n",
       "      <td>171</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Royal Challengers Bangalore</th>\n",
       "      <td>9440</td>\n",
       "      <td>2360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sunrisers Hyderabad</th>\n",
       "      <td>5776</td>\n",
       "      <td>1444</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             runs by fours  fours\n",
       "batting_team                                     \n",
       "Chennai Super Kings                   8772   2193\n",
       "Deccan Chargers                       3828    957\n",
       "Delhi Capitals                         968    242\n",
       "Delhi Daredevils                      8632   2158\n",
       "Gujarat Lions                         1840    460\n",
       "Kings XI Punjab                       9832   2458\n",
       "Kochi Tuskers Kerala                   680    170\n",
       "Kolkata Knight Riders                 9736   2434\n",
       "Mumbai Indians                       10352   2588\n",
       "Pune Warriors                         2100    525\n",
       "Rajasthan Royals                      8140   2035\n",
       "Rising Pune Supergiant                 788    197\n",
       "Rising Pune Supergiants                684    171\n",
       "Royal Challengers Bangalore           9440   2360\n",
       "Sunrisers Hyderabad                   5776   1444"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print numbers of fours hit by team\n",
    "four_data=complete_data[complete_data['batsman_runs']==4]\n",
    "four_data.groupby('batting_team')['batsman_runs'].agg([('runs by fours','sum'),('fours','count')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# we will plot graph on four hit by players\n",
    "batsman_four=four_data.groupby('batsman')['batsman_runs'].agg([('four','count')]).reset_index().sort_values('four',ascending=0)\n",
    "ax=batsman_four.iloc[:10,:].plot('batsman','four',kind='bar',color='black')\n",
    "plt.title(\"Numbers of fours hit by playes \",fontsize=20)\n",
    "plt.xticks(rotation=50)\n",
    "plt.xlabel(\"Player name\",fontsize=15)\n",
    "plt.ylabel(\"No of fours\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# we will plot graph on no of four hit in each season\n",
    "ax=four_data.groupby('season')['batsman_runs'].agg([('four','count')]).reset_index().plot('season','four',kind='bar',color = 'red')\n",
    "plt.title(\"Numbers of fours hit in each season \",fontsize=20)\n",
    "plt.xticks(rotation=50)\n",
    "plt.xlabel(\"season\",fontsize=15)\n",
    "plt.ylabel(\"No of fours\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>runs by six</th>\n",
       "      <th>sixes</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batting_team</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Chennai Super Kings</th>\n",
       "      <td>5838</td>\n",
       "      <td>973</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Deccan Chargers</th>\n",
       "      <td>2400</td>\n",
       "      <td>400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delhi Capitals</th>\n",
       "      <td>522</td>\n",
       "      <td>87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delhi Daredevils</th>\n",
       "      <td>4806</td>\n",
       "      <td>801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gujarat Lions</th>\n",
       "      <td>930</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kings XI Punjab</th>\n",
       "      <td>5856</td>\n",
       "      <td>976</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kochi Tuskers Kerala</th>\n",
       "      <td>318</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kolkata Knight Riders</th>\n",
       "      <td>5580</td>\n",
       "      <td>930</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mumbai Indians</th>\n",
       "      <td>6576</td>\n",
       "      <td>1096</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pune Warriors</th>\n",
       "      <td>1176</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rajasthan Royals</th>\n",
       "      <td>4086</td>\n",
       "      <td>681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiant</th>\n",
       "      <td>534</td>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiants</th>\n",
       "      <td>408</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Royal Challengers Bangalore</th>\n",
       "      <td>6792</td>\n",
       "      <td>1132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sunrisers Hyderabad</th>\n",
       "      <td>3198</td>\n",
       "      <td>533</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             runs by six  sixes\n",
       "batting_team                                   \n",
       "Chennai Super Kings                 5838    973\n",
       "Deccan Chargers                     2400    400\n",
       "Delhi Capitals                       522     87\n",
       "Delhi Daredevils                    4806    801\n",
       "Gujarat Lions                        930    155\n",
       "Kings XI Punjab                     5856    976\n",
       "Kochi Tuskers Kerala                 318     53\n",
       "Kolkata Knight Riders               5580    930\n",
       "Mumbai Indians                      6576   1096\n",
       "Pune Warriors                       1176    196\n",
       "Rajasthan Royals                    4086    681\n",
       "Rising Pune Supergiant               534     89\n",
       "Rising Pune Supergiants              408     68\n",
       "Royal Challengers Bangalore         6792   1132\n",
       "Sunrisers Hyderabad                 3198    533"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print no of sixes hit by team\n",
    "six_data=complete_data[complete_data['batsman_runs']==6]\n",
    "six_data.groupby('batting_team')['batsman_runs'].agg([('runs by six','sum'),('sixes','count')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# we will plot graph of six hit by players\n",
    "batsman_six=six_data.groupby('batsman')['batsman_runs'].agg([('six','count')]).reset_index().sort_values('six',ascending=0)\n",
    "ax=batsman_six.iloc[:10,:].plot('batsman','six',kind='bar',color='green')\n",
    "plt.title(\"Numbers of six hit by playes \",fontsize=20)\n",
    "plt.xticks(rotation=50)\n",
    "plt.xlabel(\"Player name\",fontsize=15)\n",
    "plt.ylabel(\"No of six\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# we will plot graph on no of six hit in each season\n",
    "ax=six_data.groupby('season')['batsman_runs'].agg([('six','count')]).reset_index().plot('season','six',kind='bar',color = 'blue')\n",
    "plt.title(\"Numbers of fours hit in each season \",fontsize=20)\n",
    "plt.xticks(rotation=50)\n",
    "plt.xlabel(\"season\",fontsize=15)\n",
    "plt.ylabel(\"No of fours\",fontsize=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*** Top 10 Leading Run Scorer in IPL ***\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>batsman</th>\n",
       "      <th>batsman_runs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>V Kohli</td>\n",
       "      <td>5434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>SK Raina</td>\n",
       "      <td>5415</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>RG Sharma</td>\n",
       "      <td>4914</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>DA Warner</td>\n",
       "      <td>4741</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>4632</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>CH Gayle</td>\n",
       "      <td>4560</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>4477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>RV Uthappa</td>\n",
       "      <td>4446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>AB de Villiers</td>\n",
       "      <td>4428</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>G Gambhir</td>\n",
       "      <td>4223</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          batsman  batsman_runs\n",
       "0         V Kohli          5434\n",
       "1        SK Raina          5415\n",
       "2       RG Sharma          4914\n",
       "3       DA Warner          4741\n",
       "4        S Dhawan          4632\n",
       "5        CH Gayle          4560\n",
       "6        MS Dhoni          4477\n",
       "7      RV Uthappa          4446\n",
       "8  AB de Villiers          4428\n",
       "9       G Gambhir          4223"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We will print the top 10 leading run scorer in IPL\n",
    "batsman_score=Data.groupby('batsman')['batsman_runs'].agg(['sum']).reset_index().sort_values('sum',ascending=False).reset_index(drop=True)\n",
    "batsman_score=batsman_score.rename(columns={'sum':'batsman_runs'})\n",
    "print(\"*** Top 10 Leading Run Scorer in IPL ***\")\n",
    "batsman_score.iloc[:10,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>batsman</th>\n",
       "      <th>No_of Matches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>SK Raina</td>\n",
       "      <td>162</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>RG Sharma</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>RV Uthappa</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>V Kohli</td>\n",
       "      <td>143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      batsman  No_of Matches\n",
       "0    SK Raina            162\n",
       "1   RG Sharma            155\n",
       "2  RV Uthappa            153\n",
       "3     V Kohli            143\n",
       "4    S Dhawan            137"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# we will print no of matches played by batsman\n",
    "No_Matches_player= Data[[\"match_id\",\"player_dismissed\"]]\n",
    "No_Matches_player =No_Matches_player .groupby(\"player_dismissed\")[\"match_id\"].count().reset_index().sort_values(by=\"match_id\",ascending=False).reset_index(drop=True)\n",
    "No_Matches_player.columns=[\"batsman\",\"No_of Matches\"]\n",
    "No_Matches_player .head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Dismissals in IPL\n",
    "plt.figure(figsize=(18,10))\n",
    "ax=sns.countplot(Data.dismissal_kind)\n",
    "plt.title(\"Dismissals in IPL\",fontsize=20)\n",
    "plt.xlabel(\"Dismissals kind\",fontsize=15)\n",
    "plt.ylabel(\"count\",fontsize=15)\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "wicket_data=Data.dropna(subset=['dismissal_kind'])\n",
    "wicket_data=wicket_data[~wicket_data['dismissal_kind'].isin(['run out','retired hurt','obstructing the field'])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>bowler</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>SL Malinga</td>\n",
       "      <td>170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>A Mishra</td>\n",
       "      <td>156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Harbhajan Singh</td>\n",
       "      <td>150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>PP Chawla</td>\n",
       "      <td>149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>DJ Bravo</td>\n",
       "      <td>147</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>B Kumar</td>\n",
       "      <td>133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>R Ashwin</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>SP Narine</td>\n",
       "      <td>122</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>UT Yadav</td>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>RA Jadeja</td>\n",
       "      <td>108</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            bowler  count\n",
       "0       SL Malinga    170\n",
       "1         A Mishra    156\n",
       "2  Harbhajan Singh    150\n",
       "3        PP Chawla    149\n",
       "4         DJ Bravo    147\n",
       "5          B Kumar    133\n",
       "6         R Ashwin    125\n",
       "7        SP Narine    122\n",
       "8         UT Yadav    119\n",
       "9        RA Jadeja    108"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we will print ipl most wicket taking bowlers\n",
    "wicket_data.groupby('bowler')['dismissal_kind'].agg(['count']).reset_index().sort_values('count',ascending=False).reset_index(drop=True).iloc[:10,:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The highest number of match played in IPL season was 2013,2014,2015.\n",
    "\n",
    "The highest number of match won by Mumbai Indians i.e 4 match out of 12 matches.\n",
    "\n",
    "Teams which Bowl first has higher chances of winning then the team which bat first.\n",
    "\n",
    "After winning toss more teams decide to do fielding first.\n",
    "\n",
    "In finals teams which decide to do fielding first win the matches more then the team which bat first.\n",
    "\n",
    "In finals most teams after winning toss decide to do fielding first.\n",
    "\n",
    "Top player of match winning are CH gayle, AB de villers.\n",
    "\n",
    "It is interesting that out of 12 IPL finals,9 times the team that won the toss was also the winner of IPL.\n",
    "\n",
    "The highest number of four hit by player is Shikar Dhawan.\n",
    "\n",
    "The highest number of six hit by player is CH gayle.\n",
    "\n",
    "Top leading run scorer in IPL are Virat kholi, SK Raina, RG Sharma.\n",
    "\n",
    "The highest number of matches played by player name are SK Raina, RG Sharma.\n",
    "\n",
    "Dismissals in IPL was most by Catch out .\n",
    "\n",
    "The IPL most wicket taken blower is SL Malinga."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Thank You!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
