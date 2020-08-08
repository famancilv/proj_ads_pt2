import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
import re

# ---------------------------------------------------------------------
# Project Ads: Data Cleaning Code.
# ---------------------------------------------------------------------
# Author: Frida Mancilla
# Contact: famancil@ucsd.edu
# Date: 06/02/2020
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Cleaning Data
# ---------------------------------------------------------------------
def clean_data(ads18, ads19):
    '''
    Cleans the data accordingly to project03. Takes in two dfs, ads18
    and ads19. Output is a cleaned/unified df, ads.
    '''
    
    # 1. in order to easily differentiate and compare date from two years, we are going to create a column 'Year' before concat.
    ads18.insert (0, 'Year', 2018)
    ads19.insert(0, 'Year', 2019)
    
    # 2. now we can concadenate both data sets ---------------------------------------------------------------
    ads = pd.concat([ads18, ads19])
    
    # 3. convering to pd.DateTime ----------------------------------------------------------------------------
    #('Z' at end of Start/EndTime means UTC timezone)
    ads.StartDate = pd.to_datetime(ads.StartDate)
    ads.EndDate = pd.to_datetime(ads.EndDate)
    
    #### 4. FILLING IN NAN values according to readme file ##### ----------------------------------------------
    # Gender column: If nan means ALL genders all targeted
    ads.Gender = ads.Gender.fillna('ALL')

    # Age Bracket: If nan means all ages
    ads.AgeBracket = ads.AgeBracket.fillna('all')

    # Interest column: If nan means no particular interest was targeted
    ads.Interests = ads.Interests.fillna('None')
    
    # AdvancedDemographics: If nan means no 3rd party data segments were used
    ads.AdvancedDemographics = ads.AdvancedDemographics.fillna('None')

    # OsType columns: if nan means all were targeted
    ads.OsType = ads.OsType.fillna('ALL')

    # Language columns: if nan means no specific language was targeted
    ads.Language = ads.Language.fillna('None') #NOTE: language needs some cleaning

    # Target Connection Type column: If nan means no particular connection type was targeted
    ads['Targeting Connection Type'] = ads['Targeting Connection Type'].fillna('None')

    # Targeting Carrier (ISP) column: If nan means all carriers were targeted
    ads['Targeting Carrier (ISP)'] = ads['Targeting Carrier (ISP)'].fillna('All')
    
    # 5. Cleaning Age Brackets ----------------------------------------------------------------------------
    
    # NOTICE vals in Gender: '18-', '16-', '19-'...

    strings = ads[ads.AgeBracket.str.match('[0-9]{2}-$')].AgeBracket.unique()
    # going thru every string and replacing thru '-' with '+'
    for s in strings:
        ads.AgeBracket = ads.AgeBracket.replace({s: s[:2]+'+'})
    
    return ads