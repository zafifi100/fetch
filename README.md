# fetch

# Hello! My name is Zaid Afifi and this is an introduction to my predictive receipt count project

## For the model, I decided to use a feedforward model to acheive a low computational cost, and augmented the data:
### - I added a sin/cos component for the month section of the date after converting to a pandas timestamp
### - I added a prev_count feature to enable a feedback loop, trying to replace an LSTM
### - I had other features, but after performing PCA, I removed them due to their low impact
### - I kept the nodes the same across the 2 layers in the model to reduce gradient loss
### - I also decided to add a dropout layer to reduce overfitting chance
### - I used MAE for my loss function due to easier interprebility than MSE
### - The lowest MAE I achieved was just under 6%
### - I shouldve implemented more testing methods, I just included a line of best fit scatter plot


## For Deployment
### - I wrote an html file to work with a .py file I used.
### - I saved the model from my jupyter notebook and used it in the .py
### - I couldve done a manual MLP, but for simplicity's sake, I just saved it as a .h5


## HOW TO USE
### - I built a Dockerfile that hopefully has all of the dependencies taken care of 
### - docker build -t myapp .
### - docker run -p 5000:5000 myapp
### - the site should look like: <img width="1248" alt="image" src="https://github.com/zafifi100/fetch/assets/114939084/dda79eb8-ef92-4c89-a2e9-6808ce457870">

