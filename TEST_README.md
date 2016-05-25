# Concept and documentation

## App name: ["Title IX"](projects.chronicle.com/titleix/) by The Chronicle of Higher Ed

## Elevator pitch

Sexual assault on college campuses has long been an issue. More recently, colleges and universities across the United States are getting in trouble for failing to adequately address the issue.

*"Over the past year and a half, the number of colleges finding themselves in the cross hairs of the U.S. Department of Education’s Office for Civil Rights over their handling of sexual-assault cases has nearly tripled, to 161."* - Chronicle

Let's build an "investigation tracker" that allows readers to look through a database about current federal Title IX violations.

## Inspirations and Prior Work

It looks like there's nothing out there that does this yet...

# Data

## Data sources

Initial info (who's under investigation, when was the investigation opened, etc):

1. The US Department of Education puts our press releases listing the higher education institutions with open Title IX sexual violence investigations.

Here's the [first release](http://www.ed.gov/news/press-releases/us-department-education-releases-list-higher-education-institutions-open-title-ix-sexual-violence-investigations)(May 2014) naming 55 colleges and universities under investigation. As of now, there are 235 open investigations at 185 institutions.

Updates to investigations might be found:

1. On Twitter accounts of students, particularly involved in action
2. Office of Civil Rights press releases
3. PACER, WestLaw filings (e.g. male student whom Stanford found responsible for sexual assault recently sued university)
4. News (google, campus publications)

## Scraping the data

The initial data is in an HTML table as part of a press release from the Department of Education that needs to scraped and organized to as to be able to distinguish (1) between colleges and (2) between multiple investigations happening at the same college/university.

# Filtering options

## Attributes to search/find by
* Allow user to search by college or keyword
* Filter for investigations with documents available
* Filter by state
* Search for tags (e.g. complaint, administrative closure, insufficient evidence)
* Fileter by public / private institutions
* Filter using a range of dates

# Views and Routes

INDEX view:
* The home page will summarize nation-wide trends, including the number of investigations pending and resolved.
* Display a graph over time of number of investigations opened per month per year
* Have a brief summary of the issue and what's at stake

RESULTS view:
* Will feature all the cases related to a single college or university
* Include bullet points of the "campus context" (here's [Stanford University](http://projects.chronicle.com/titleix/campus/Stanford-University/))
* Include links to news articles (on campus and off campus) about the issue and investigations opened
* Include an **obvious** "I want updates!" button so that interested users can be notified if more information appears

# Visualizations

## Graphs

A line graph showing number of open and resolved investigations over time.
![img](http://i.imgur.com/Qf1JxiT.png?1)

## Tables

A visualization showing the top 5 colleges with the most open cases.
![img](http://i.imgur.com/TwUIvFY.png?1)


# Deployment
Put it on heroku?


