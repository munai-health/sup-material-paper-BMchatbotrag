''' Lets reproduce a graphic '''
import matplotlib.pyplot as plt
import plot_likert
import pandas as pd

my_color_scheme =[
    plot_likert.colors.TRANSPARENT,
    "#7b3294",
    "#c2a5cf",
    "#999999",
    "#a6dba0",
    "#008837",
]

''' Our questions'''
questions = {'Q1': 'Q1 - I would like to use', 'Q2': 'Q2 - Unnecessarily complex', 'Q3': 'Q3 - Easy to use', 
             'Q4': 'Q4 - Need technical knowledge', 'Q5': 'Q5 - System well integrated', 'Q6': 'Q6 - System Inconsistent', 
             'Q7': 'Q7 - Learn to use it quickly', 'Q8': 'Q8 - Complicated to use', 'Q9': 'Q9 - Felt confident using', 
             'Q10': 'Q10 - Need to learn\nseveral new things'}

''' Computing the precomputed counts'''
precomputed_counts = pd.DataFrame(
    {'Strongly disagree': {questions['Q1']: 0.0, questions['Q2']: 50.0, questions['Q3']: 0.0, questions['Q4']: 81.0, questions['Q5']: 0, questions['Q6']: 19.0, questions['Q7']: 0.0, questions['Q8']: 69.0, questions['Q9']: 0.0, questions['Q10']: 75.0},
     'Disagree': {questions['Q1']: 12.0, questions['Q2']: 25.0, questions['Q3']: 0.0, questions['Q4']: 12.0, questions['Q5']: 0, questions['Q6']: 38.0, questions['Q7']: 0.0, questions['Q8']: 31.0, questions['Q9']: 6.0, questions['Q10']: 19.0},
     'Neither agree nor disagree': {questions['Q1']: 38.0, questions['Q2']: 12.0, questions['Q3']: 0.0, questions['Q4']: 6.0, questions['Q5']: 25.0, questions['Q6']: 25.0, questions['Q7']: 0.0, questions['Q8']: 0.0, questions['Q9']: 19.0, questions['Q10']: 0.0},
     'Agree': {questions['Q1']: 19.0, questions['Q2']: 12.0, questions['Q3']: 31.0, questions['Q4']: 0.0, questions['Q5']: 50.0, questions['Q6']: 6.0, questions['Q7']: 31.0, questions['Q8']: 0.0, questions['Q9']: 38.0, questions['Q10']: 0.0},
     'Strongly agree': {questions['Q1']: 31.0, questions['Q2']: 0.0, questions['Q3']: 69.0, questions['Q4']: 0.0, questions['Q5']: 25.0, questions['Q6']: 12.0, questions['Q7']: 69.0, questions['Q8']: 0.0, questions['Q9']: 38.0, questions['Q10']: 6.0}})

''' Plotting and saving'''
ax = plot_likert.plot_counts(precomputed_counts, plot_likert.scales.agree, colors=my_color_scheme, plot_percentage=True, bar_labels=True, bar_labels_color='black', compute_percentages=True, figsize=(8, 10), xtick_interval=50)
plt.savefig('chart-likert-updated.pdf', dpi=300, bbox_inches='tight') 