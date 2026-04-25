# Loading cleaned data
df = pd.read_csv("cleaned_data.csv")

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

pass_count = 0
math_scores = df ["math score"]. to_list()
for i, score in enumerate (math_scores,start=1):
    if score >= 50:
       print ("student" , i, "Passed")
       pass_count +=1
    else:
        print (("student"),i , "Failed")
print ("Total passed:",pass_count)


