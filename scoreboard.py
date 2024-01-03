
old_data="""
Top 10
1. KMG 279
2. KMG 296
3. KMG 300
4. KMG 350
5. KMG 361
6. MMT 427
7. KMG 521
8. KMG 582
9. KMG 771
10. KMG 823
"""
contender='KMG'
contender_score=324

def read_data(input):
    line=''
    scores=[]
    for x in input:
        if x=="\n":
            scores.append(line)
            line=''
            continue
        line+=x
        continue
    
    return scores
def parse_scores(input:str):
    # position=[]
    initials=[]
    score=[]
    for x in input:
        if (x != '') and (x != 'Top 10'):
            line=x.split()
            #remove period from position
            # Can remove this entirely because arrays lol
            #            position.append(line[0].replace(".",""))
            initials.append(line[1])
            score.append(int(line[2]))
    return initials,score
def arrange_scoreboard(initials:list,score:list):
    # Combine initials and score into a list of tuples
    scoreboard = list(zip(initials, score))

    # Sort the scoreboard based on score in descending order
    scoreboard.sort(key=lambda x: x[1], reverse=False)

    # Separate the sorted initials and score into separate lists
    sorted_initials, sorted_score = zip(*scoreboard)
    return list(sorted_initials), list(sorted_score)
def update_scores(initials,score,new_person,new_score):
    
    for x in range(len(score)):
        if new_score < score[x]:
            initials.insert(x,new_person)
            score.insert(x,new_score)
            print('Score updated! {} is ranked {}! Bumping out {}'.format(new_person,x+1,initials[x+1]))
            break
    if len(initials) > 10:
        initials.pop()
        score.pop()
    return initials,score



def format_scoreboard(initials,score):
    scoreboard=""
    for x in range(len(initials)):
        line=(f"{x+1}. {initials[x]} {score[x]}")
        scoreboard+=line+'\n'

    return scoreboard



data=read_data(old_data)
# print(data)

initials_data,score_data=parse_scores(data)
# for line,line_no in enumerate(y):
#     print(line,line_no)
initials_data,score_data=(arrange_scoreboard(initials_data,score_data))
initials_data,score_data=(update_scores(initials_data,score_data,contender.upper(),contender_score))
print('Top 10')
print(format_scoreboard(initials_data,score_data))
