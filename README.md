# Content Based Recommender System

<div style="text-align:center;margin:0 auto;">
<img src="https://github.com/cjcarvajal/content-based-recommender-system/blob/master/resources/demo.gif" width="600" style="display:block; margin:auto;">	
</div>

## What it does?

A content recommender system, in contrast to a collaborative filtering system, depends on the content of the items (as you might guess) instead of the ratings given by other users to the same items. One question rises and is how the system knows the content of an item? There is no magic here, the system needs metadata about the items to know their content, so each time a new item enters the system it needs to have this metadata in order to be recommended. For this demo, the items are movies, and the content is described by **keywords** that describe the content, for example an item like **Jurassic Park** has "dinosaur" as a keyword on its metadata. The system, compares the metadata of all items and returns the more similar items.

A content recommender system may be as broad as it's needed, for example, in the movie context, one could add the actors, director or soundtrack composer (please be [Ennio Morricone](https://www.youtube.com/watch?v=Kmh6rdRhcOw&t=1s) or [Hans Zimmer](https://www.youtube.com/watch?v=OzLhXesNkCI)) as metadata.

Lets see some example of the system running, if we search for an item by id, we meet a well known movie:

<div style="text-align:center">
<img src="https://github.com/cjcarvajal/content-based-recommender-system/blob/master/resources/img1.png" width="600" style="display:block; margin:auto;">	
</div>

Then if we ask the system about recommendations related to that item we get the following:

<div style="text-align:center">
<img src="https://github.com/cjcarvajal/content-based-recommender-system/blob/master/resources/img2.png" width="600" style="display:block; margin:auto;">	
</div>

A disadvantage of the content recommender approach is that you miss the [serendipity](https://dl.acm.org/citation.cfm?id=3009209.3009262) feature and you just get "more of the same", nevertheless is a great approach to tackle the [cold start](https://en.wikipedia.org/wiki/Cold_start_(computing)) issue, and of course, you could combine this approach with others to create a hybrid system, you could read more [here](https://leantechblog.wordpress.com/2018/01/03/how-does-netflix-or-spotify-knows-what-you-like-a-briefing-on-recommender-systems/).

## How it works?

There are just three components, the controller, the persistence manager and the similarity calculator.

* **rest_controller.py** it uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework to expose two endpoints, an item query which receives the internal item id an returns its name, and a recommendations query, which also, receives an item id that represents the item liked by the user and returns similar-by-content items.

* **persistence_manager.py** it loads into memory the files with the items names and metadata and isolate the access to them.

* **cosine_similarity_calculator.py** here is where the magic take place, using [sklearn](https://scikit-learn.org/stable/) the metadata is translated to vectors, then the similarity between all vectors is calculated using cosine metric, these calculation is stored in a matrix and its possible to get the most similar vectors to a specific one, later this vectors are translated to items which are then returned as recommendations.

You just need to start the rest_controller.py and voila!, I also added a Postman collection so you could use the exposed enpoints.

## Where do I got the data?

The files keywords.csv and titles.csv are prepocessed from original ones. The original files belongs to [Kaggle](https://www.kaggle.com/), specifically to [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset), the intellectual property of this files and all right reserved belongs to Kaggle.