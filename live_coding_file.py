import streamlit as st
from statsmodels.stats.proportion import proportion_confint
st.title('Business Ads Costing Example DSI')
st.write('Use this app to figure out how good is the spam takedown machine on FB')

num_spam_takedowns = st.number_input('Number of spam takedown samples', value=500)
num_successes = st.number_input('Est number of successful takedown samples', value=300)
sample_cost = st.number_input('Cost of 1 Sample in $', value=1)
time_window = st.selectbox('How often do you want this metric?', ['Weekly','Biweekly','Monthly'])
#inputs
#confidence interval
#get the estimated precision of the group
upper_val, lower_val = proportion_confint(count=num_successes, nobs=num_spam_takedowns)
confint_width = abs(upper_val - lower_val)
cost = num_spam_takedowns * sample_cost
if time_window == 'Weekly':
    cost = cost*52
elif time_window == 'Monthly':
    cost = cost*26
st.write(upper_val)
st.write(lower_val)
st.write(confint_width)
st.write(cost)