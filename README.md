# fetch

# Hello! My name is Zaid Afifi and this is an introduction to my predictive receipt count project

## For the model, I decided to use a feedforward model to acheive a low computational cost, and augmented the data:
### I added a sin/cos component for the month section of the date after converting to a pandas timestamp
### I added a prev_count feature to enable a feedback loop, trying to replace an LSTM
### - I had other features, but after performing PCA, I removed them due to their low impact
### - I kept the nodes the same across the 2 layers in the model to reduce gradient loss
### - I also decided to add a dropout layer to reduce overfitting chance
### - I used MAE for my loss function due to easier interprebility than MSE
### - The lowest MAE I achieved was just under 6%
