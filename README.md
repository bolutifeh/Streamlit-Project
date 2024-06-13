Capstone Project I
The United Kingdom conducts a population census every ten years; the most recent was in 2021. Such a census's objectives are to compare various individuals around the country and give the government precise demographic numbers for better planning, to create policies, and to allot certain financial resources.
You have a fictitious dataset. You are to think as a member of the local government team, deciding what kind of investments to make. 
The columns are defined as follows.
(1) House Number 
(2) Street Name.
(3) First Name of occupant.
(4) Surname of occupant.
(5) Age of occupant.
(6) Relationship to the “Head” of the household (anyone aged over 18 can be a “Head” – they are
simply the person who had the responsibility to fill in the census details)
(7) Marital status (one of Single, Married, Divorced, Widowed, or “NA” in the case of minors)
(8) Gender 
(9) Occupation 
(10) Infirmity 
(11) Religion 

Tasks
Clean the given data and identify the missing data. Decide on what to do with the missing data. Justify your decision in the comments section.
Carry out Exploratory Data Analysis (EDA) on each column. Ensure you supplement your EDA with visualizations (ensure your visualizations maximize Matplotlib, seaborn and Plotly)
Based on your discoveries from your EDA, which one of the following options should be invested in? Back up your recommendation using graphics and a few comments.
(i) Employment and training. If there is evidence of unemployment, we should re-train people for new skills.
(ii) Old age care. If there is evidence of increasing numbers of retired people in future years, the town will need to allocate more funding for end-of-life care.
(iii) Increase spending on schooling. If there is evidence of a growing population of school-aged children (new births, or families moving into the town), then schooling spending should increase.
(iv) General infrastructure. If the town is expanding, then services (waste collection, road
maintenance, etc.) will require more investment.
Capstone Project 2
Using the Dataset given in Capstone Project I. Do the following using the Streamlit:
Develop a search application that uses the street name (a drop-down item is preferred) to provide the following visualizations in relation to the total dataset.
Provide a line chart of the searched street name, the house number against the house population (number of persons who lives there). Hint: Filter down using the street name, then groupby house number, and finally, count.
Provide a barchart of the Marital Status of the selected street name.
Use a bar chart to show the distribution of gender across the top twenty (15) most populated streets.
Use scatterplot to show the spread of age in United Kingdom using the provide data (Be creative with, you can decide to make it more exhaustive than it sounds) 

Capstone Project 3
Convert the census data frame to a table and store it on an empty SQLite database (to be created by you). Using SQL commands, answer the following questions:
How many males and females are within the age range 70 – 100.
How many students live in Sagittarius Avenue?
Identify the population of every religion in the UK.
Finally, remove the ‘Jewish’ from your total population.
