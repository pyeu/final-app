# final-app

# Deaths in Custody

## Elevator Pitch

Transparency, deaths in custory...



## Inspirations & Prior Work

**1. [Death behind bars: Inmate suicides, overdoses among causes](http://www.desmoinesregister.com/story/news/investigations/2016/05/28/death-behind-bars-inmate-suicides-overdoses-among-causes/83671656/) (Des Moines Register)**

This article by the Des Moines Register discusses the issues around inmate deathes in Iowa, specifically the prevalence of mental health related deaths after Iowa's closure of mental health facilities in 2015. Number of cases per year is relatively static, the article says, but that does not make the issue any less pressing.

The article emphasizes that the Bureau of Justice Statistics data includes no informaiton about whether health facility might have contributed to more jajil and prison deaths, or whether mental illness was a factor. 

However, [this paper](http://law.stanford.edu/wp-content/uploads/sites/default/files/child-page/632655/doc/slspublic/Report_v12.pdf) titled "When did prisons become acceptable mental healthcare facilities" published by Stanford Law School argues the same correlation between closure of mental health facilities under Reagan and an increase in inmate death is happening in California.

* The most obvious difference between this article and my app is that my app will explore statistics for California, not Iowa.
* This piece by the Des Moines Register does not allow users to explore the data themselves. My app will include a map element and link to relevant articles about the death, allowing users to draw their own conclusions based on the data.

**2. [OpenJustice from the California DOJ](http://openjustice.doj.ca.gov)**

In the interest of transparancy, California's Department of Justice recently unveiled their own data journalism-esc website exploring data around issues of crime and law enforcement. 

[This article by AP](http://www.nbcbayarea.com/news/local/California-Department-of-Justice-to-Unveil-Website-With-Law-Enforcement-Data-323932901.html) announces the unveiling of CA DOJ's new website.

The [Open Justice page on Deaths in Custody](http://openjustice.doj.ca.gov/death-in-custody/overview) helps breakdown the data with charts and graphics -- some examples below:

![img](http://i.imgur.com/9HgsD81.png?1)
Breakdown of inmate deaths by race/ethnicity.

![img](http://i.imgur.com/uTfadrj.png?1)
Deaths Per Law Enforcement Agency over time.

* The DOJ's website is an **awesome** step in the right direction, however it does not include any sort of exploratory element along with the graphics. My app will allow users to choose search terms and explore the published data along with visualizations.
* The website doesn't include any sort of mapping element, something I plan to include as  part of my app.

**3. Something here** 


*
*

**4. And here**

*
*

**5. And here...**

* 
*

# Data

My data comes from the [Deaths in Custody Reporting Program](http://www.bjs.gov/index.cfm?ty=dcdetail&iid=243), a program within the Bureau of Justice that collects data on deaths that occur during the arrest process or while inmates are in the custody of local jails or state prisons. I [found the data through MuckRock](https://www.muckrock.com/foi/california-52/california-12525-data-17354/) thanks to [Dan's explainer on how to filter MuckRock requests by Status==completed](http://blog.danwin.com/interesting-muckrocks/).

I will also use [income per capita](https://www.census.gov/hhes/www/income/data/historical/people/) and [geographic shapes](https://www.census.gov/geo/maps-data/data/tiger-data.html) from the Census.

## must contain at least one join

Deaths in Custody records the county of death, and I'll use this field to join to the Census's income per capita and geographic shapes.

## categorical variable

The data currently has a variable "custody offense" of numbers that correspond to various offenses -- I will join this dataset to the index of offenses and create a new text variable "offense" listing the individual's initial offense.

## continuous variable

I'm adding a variable called "days in custody" that measures the number of days from initial arrest until death.

## summarization

At the very least, my app will summarize deaths by county.

# Filtering Options

1. My app includes a partial text search allowing the user to search by last name.
2. There will also be a drop down menu so users can search for inmate death by county.

Users can sort by days in custody or date of death.

# Views and Routes

## Front page

The front page of my app will include a map of inmate deaths by county across the state of California as well as a brief discussion of the issue and related mental health crisis, and links to relevant articles/reading.

## Search results view

By county searches will include brief text from relevant news articles...

# Deployment

I will use Heroku to deploy my app because it's the PaaS I have the most experience with using and it worked excelently for my First News App, which involved similar (if slightly more simple) datasets and filters.




