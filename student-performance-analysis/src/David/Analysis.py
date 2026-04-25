# Loading cleaned data
df.to_csv("cleaned_data.csv", index=False)

## Core Task
# Average math score
avg_math_score = df["math score"].mean()
# Print average math scores
print("Average Math Score;", avg_math_score)

# average reading score
avg_reading_score = df["reading score"].mean()
# Print average math scores
print("Average Reading Score;", avg_reading_score)

# average writing score
avg_writing_score = df["writing score"].mean()
# Print average math scores
print("Average Writing Score;", avg_writing_score)

