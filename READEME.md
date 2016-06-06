# final-app

# Deaths in Custody

## Elevator Pitch

There are frequent investigations into police accountability -- especially in the last year -- but relatively few studies into what happens behind bars. In 2012, 4,309 people died while being held in local jails or state prisons nationwide.

My app will navigate the Bureau of Justice's [Deaths in Custody data](http://www.bjs.gov/index.cfm?ty=dcdetail&iid=243) and allow users to compare county by county statistics or search for specific individuals.

## Inspirations & Prior Work

**1. [Death behind bars: Inmate suicides, overdoses among causes](http://www.desmoinesregister.com/story/news/investigations/2016/05/28/death-behind-bars-inmate-suicides-overdoses-among-causes/83671656/), via Des Moines Register**

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

**3. [How Many People Die in Police Custody in America?](https://www.vice.com/read/how-many-people-die-in-police-custody-in-america-265) via VICE** 

Vice wrote this piece in 2015 tying the rise in public interest in what happens behind bars to the death (in custody) of Black Lives Matter activist Sandra Bland. The article wrote, "Bland's death was officially ruled a suicide, but an investigation into 'lingering questions' is ongoing."

* The piece does a great job of acknowledging the "vague-ness" of deaths in custody. When someone kills themselves in a state-run prison, who is responsible? The guards, who may not have received suicide prevention training? The state, for defunding mental health prevention facilities? I'd like to touch *briefly* on some of these issues on the home page of my app.

* The article touches on data a couple of times, mentioning 4,309 deaths in custody nationwide in 2012. My app will tell similar statistics on a county by county level.

**4. [Annual report on deaths during or following police contact in 2014/15](http://www.ipcc.gov.uk/news/annual-report-deaths-during-or-following-police-contact-201415-published), via IPCC**

The Independent Police Complaints Commission (IPCC) is a British organization that publishes annual reports on police accountability across the UK. 

Their most recent report [full report here](http://www.ipcc.gov.uk/page/deaths-during-or-following-police-contact), published July 23, 2015 details 17 deaths in or following police custody, 1 fatal shooting, and 69 apparent suicides following custody, among other statistics. The numbers are shockingly low compared to the United States, which recorded 78 suicides just in the state of California.

* While the IPCC does an excellent job of internally reviewing the data, they don't publish any sort of interactive or visualization, which my app will most definitely include.
* The homepage here does a great job of summarizing hte most important findings from the data and linking to relevant reviews and reports.

**5. [The Next to Die](https://www.themarshallproject.org/next-to-die?ref=menu), via The Marshall Project**

The Next to Die is a news app developed by the Marshall Project to track inmates on death row. The app keeps track of inmates by counting down the days until they are scheduled to be executed and keeping track of any appeals or updates to the process.

![img](http://i.imgur.com/rgcxV82.png?1)

While not directly related to deaths in custody, *The Next to Die* does an excellent job of personalizing an issue many Americans would rather keep "out of sight, out of mind". Extraordinary attention is devoted to each inmate, while at the same time contextualizing the issue across the United States. (See graphics below.)

![img](http://i.imgur.com/uxhbGUa.png?1)

![img](http://i.imgur.com/Q89LLiU.png?1)

* *The Next to Die* has a great feature that tracks updates for each inmate. This isn't quite relevant to my research (dead inmates tend to have fewer updates), but I would love to incorporate some sort of feature that tracks news / fall-out from particular inmate deaths and any changes or reviews to the local or state penitentiary system.

* I like the clickable list of county names on the left hand side of the page rather than a drop down menu for each county. I also like how the blurb on "The History of the Death Penalty in XYZ State" is broken up with visualizations, with the option to "READ MORE BELOW" so that users can chose their own level of engagement.

# Data

My data comes from the [Deaths in Custody Reporting Program](http://www.bjs.gov/index.cfm?ty=dcdetail&iid=243), a program within the Bureau of Justice that collects data on deaths that occur during the arrest process or while inmates are in the custody of local jails or state prisons. I [found the data through MuckRock](https://www.muckrock.com/foi/california-52/california-12525-data-17354/) thanks to [Dan's explainer on how to filter MuckRock requests by Status==completed](http://blog.danwin.com/interesting-muckrocks/).

I will also use [income per capita](https://www.census.gov/hhes/www/income/data/historical/people/) and [geographic shapes](https://www.census.gov/geo/maps-data/data/tiger-data.html) from the Census.

Note: The BJS’s 2015 “Data Quality Profile” report shows that some states have not reported statistics to the federal government in a given year between 2003 and 2011, and a few states have not participated at all. (via [Jouralists Resource](http://journalistsresource.org/studies/government/criminal-justice/deaths-police-custody-united-states#sthash.mdzmobZC.dpuf))

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

Users can sort by days in custody (highest or lowest) or date of death.

# Views and Routes

## Front page

The front page of my app will include a map of inmate deaths by county across the state of California as well as a brief discussion of the issue,  related legislations/events like federal defunding of mental health institutions and support, and links to relevant articles/reading.

## Search results view

When users search by county, they'll be presented with relevant text from the top news articles about the issue as well as a graphic comparing county deaths with the state average and a table of most frequent causes of death and average days before death.

The results page will also include a table of aggregate data, e.g. all inmate deaths from a particular county.

# Deployment

I will use Heroku to deploy my app because it's the PaaS I have the most experience with using and it worked excelently for my First News App, which involved similar (if slightly more simple) datasets and filters.




