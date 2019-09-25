# Content Based Recommender System

## What it does?

A content recommender system, in contrast to a collaborative filtering system, depends on the content of the items (as you might guess) instead of the ratings given by other users to the same items. One question rises and is how the system knows the content of an item? There is no magic here, the system needs metadata about the items to know their content, so each time a new item enters the system it needs to have this metadata in order to by recommended. For this demo, the items are movies, and the content is described by **keywords** that describe the content, for example an item like Jurassic Park has "dinosaur" as a keyword on its metadata. The system, compares the metadata of all items and returns the more similar items.

A content recommender system may be as broad as it's needed, for example, in the movie context, one could add the actors, director or soundtrack composer (please be Ennio Morricone or Hans Zimmer) as metadata.

Lets see some example of the system running, if we search for an item by id, we meet a well known movie:

<div style="text-align:center">
<img src="https://github.com/cjcarvajal/content-based-recommender-system/blob/master/resources/img1.png" width="600" style="display:block; margin:auto;">	
</div>

Then if we ask the system about recommendations related to that item we get the following:

<div style="text-align:center">
<img src="https://github.com/cjcarvajal/content-based-recommender-system/blob/master/resources/img2.png" width="600" style="display:block; margin:auto;">	
</div>

## How it works?

## Where do I get the data?

The files keywords.csv and titles.csv are prepocessed from original ones. The original files belongs to [Kaggle](https://www.kaggle.com/), specifically to [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset), the intellectual property of this files and all right reserved belongs to Kaggle.