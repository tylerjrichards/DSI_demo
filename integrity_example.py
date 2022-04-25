from statsmodels.stats.proportion import proportion_confint
import streamlit as st

st.title('Costing Example: Business Ads')
st.write('To use this app, input your assumptions and get the confidence intervals below')
n_trials = st.number_input('How many samples do you want to get?', value=500)
n_successes = st.number_input('How many do you think will be correct?', value=400)
cost_per_sample = st.number_input('How much do you think it will cost per sample? (in $)', value=1)
n_metrics_per_year = st.selectbox('How often do you want this metric?', ['Weekly', 'Biweekly', 'Monthly'])
proportion_output = proportion_confint(count=n_successes, nobs=n_trials, method='wilson')

lower_val = round(100*proportion_output[0], 1)
upper_val = round(100*proportion_output[1], 1)
ci_width = round(upper_val-lower_val, 1)
precision = round(100*(n_successes / n_trials))

st.write(f'Your precision is {precision}%, and your CI will be between {lower_val}% and {upper_val}%, a width of {ci_width}%')
cost = n_trials*cost_per_sample
if n_metrics_per_year == 'Weekly':
    cost = cost*52
if n_metrics_per_year == 'Biweekly':
    cost = cost*26
if n_metrics_per_year == 'Monthly':
    cost = cost*12

st.write(f'This metric will cost an average of ${cost} per year')