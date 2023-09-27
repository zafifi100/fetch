# fetch

# Hello! My name is Zaid Afifi and this is an introduction to my predictive receipt count project

## For the model, I decided to use a feedforward model to acheive a low computational cost, and augmented the data:
## - I added a sin/cos component for the month section of the date after converting to a pandas timestamp
## - I added a prev_count feature to enable a feedback loop, trying to replace an LSTM
