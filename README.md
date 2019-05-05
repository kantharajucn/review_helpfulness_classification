# Amazon review helpfulness classification

Now a days online reviews are taking major role in decision making when people want to purchase online.
Eventhough there are reviews written by many users who purchased the product, people are unable to find which is the useful review to make correct decision. The real reason behind the issue is that many useful reviews are hiding benith and there are not considered for the decision making process. Many people read only top ten or twenty review which are visible.

  From few years companies like Yelp, Amazon have introduced `Is this review helpful?` question in their website and people can press `thumbs up` or `thumbs down` based on this count they sort the reviws in such a way that reviews with more helpful rate are displayed on the top and the reviews with less helpful votes will be in the buttom. The problem with this mechanism is that people give votes only to the top reviews, reviews which are in button do not receive any votes weven though they are good reviews.
  
  In this project, I have tried to classify the reviews as Helpful or not Helpful using traditional Machine learning and Reccurent Neural networks.
  
 ## Dataset
 I have used 50000 reviews from publicly available Amazon product revierws. Please download from the [link](http://jmcauley.ucsd.edu/data/amazon/).
 
 ## Requirements
 1. Use tensorflow docker image with python 3.x with Jupyter notebook.
 2. Install extra libraries Keras and sklearn.
 3. Install pydot
 4. Download glove word wmbeding `glove.6b.100d.txt` and store into the folder `word_embeding`
 
 ## Usage
 Run the notebook and the final model will be stored in `model` directory.
 
