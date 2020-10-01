"""
Made to pick groups for Catan Cup 2020.
Makes sure captains are on different teams, and players with different win experience are on different teams.

(There must be an easier way. This code is inefficient but it works.)
"""
#%%
import numpy as np
import pandas as pd
## Choose the seed number
lucky_number = 21 # 0<= n <= 2**32-1
np.random.seed(lucky_number)

#%%


captains = ["김기환", "조나단", "조예람", "이하나"] # Captains have proof of victory
s_tier = ["조안나","정예종","윤하영"] # S-tier players claim, but have no proof of victory. They should not be in same group

competitors = [
"이민정",
"황혜진",
"전한나",
"김준영",
"이지호",
"임요섭",
"고예빈",
"박병준",
"박재완",
"윤혜영"
] # Players without a win
competitors_per_group = 2
all_players = competitors + s_tier + captains


#%% This is what we would run if every group was same size

# players_remaining = np.array(range(0, len(competitors)))
# s_tier_remaining = np.array(range(len(competitors), len(competitors)+len(s_tier)))
# captains_remaining = np.array(range(len(competitors)+len(s_tier), len(all_players)))

# ## Making the groups

# groupA = np.random.choice(players_remaining, competitors_per_group, replace = False)
# players_remaining = np.setdiff1d(players_remaining, groupA)
# groupA = np.append(groupA, np.random.choice(s_tier_remaining, 1, replace = False))
# s_tier_remaining = np.setdiff1d(s_tier_remaining, groupA)
# groupA = np.append(groupA, np.random.choice(captains_remaining, 1, replace = False))
# captains_remaining = np.setdiff1d(captains_remaining, groupA)

# groupB = np.random.choice(players_remaining, competitors_per_group, replace = False)
# players_remaining = np.setdiff1d(players_remaining, groupB)
# groupB = np.append(groupB, np.random.choice(s_tier_remaining, 1, replace = False))
# s_tier_remaining = np.setdiff1d(s_tier_remaining, groupB)
# groupB = np.append(groupB, np.random.choice(captains_remaining, 1, replace = False))
# captains_remaining = np.setdiff1d(captains_remaining, groupB)


# groupC = np.random.choice(players_remaining, competitors_per_group, replace = False)
# players_remaining = np.setdiff1d(players_remaining, groupC)
# groupC = np.append(groupC, np.random.choice(s_tier_remaining, 1, replace = False))
# s_tier_remaining = np.setdiff1d(s_tier_remaining, groupC)
# groupC = np.append(groupC, np.random.choice(captains_remaining, 1, replace = False))
# captains_remaining = np.setdiff1d(captains_remaining, groupC)

# groupD = np.append(players_remaining, s_tier_remaining)
# groupD = np.append(groupD, captains_remaining)

# all_players = pd.Series(all_players)
# print("Group A:\n", all_players.loc[groupA],"\n\n")
# print("Group B:\n", all_players.loc[groupB],"\n\n")
# print("Group C:\n", all_players.loc[groupC],"\n\n")
# print("Group D:\n", all_players.loc[groupD],"\n\n") # subtract 1 because started range at 1. minor inefficiency, fix later.

# %% 
captains = ["김기환", "조나단", "조예람", "이하나"] # Captains have proof of victory
captain_with_5 = np.random.randint(0,2) # One of 김기환 or 조나단 will have 5 players
s_tier = ["조안나", "정예종", "윤하영"] # Tier A players claim, but have no proof of victory. They should not be in same group

players_remaining = np.array(range(0, len(competitors)))
s_tier_remaining = np.array(range(len(competitors), len(competitors)+len(s_tier)))
captains_remaining = np.array(range(len(competitors)+len(s_tier), len(all_players)))

## Making the groups. groupA will have 5 players but no s-tier player

groupA = np.random.choice(players_remaining, competitors_per_group+2, replace = False)
players_remaining = np.setdiff1d(players_remaining, groupA)
groupA = np.append(groupA, captains_remaining[captain_with_5])
captains_remaining = np.setdiff1d(captains_remaining, groupA)

groupB = np.random.choice(players_remaining, competitors_per_group, replace = False)
players_remaining = np.setdiff1d(players_remaining, groupB)
groupB = np.append(groupB, np.random.choice(s_tier_remaining, 1, replace = False))
s_tier_remaining = np.setdiff1d(s_tier_remaining, groupB)
groupB = np.append(groupB, np.random.choice(captains_remaining, 1, replace = False))
captains_remaining = np.setdiff1d(captains_remaining, groupB)

groupC = np.random.choice(players_remaining, competitors_per_group, replace = False)
players_remaining = np.setdiff1d(players_remaining, groupC)
groupC = np.append(groupC, np.random.choice(s_tier_remaining, 1, replace = False))
s_tier_remaining = np.setdiff1d(s_tier_remaining, groupC)
groupC = np.append(groupC, np.random.choice(captains_remaining, 1, replace = False))
captains_remaining = np.setdiff1d(captains_remaining, groupC)

groupD = np.append(players_remaining, s_tier_remaining)
groupD = np.append(groupD, captains_remaining)

all_players = pd.Series(all_players)
print("Group A:\n", all_players.loc[groupA],"\n\n")
print("Group B:\n", all_players.loc[groupB],"\n\n")
print("Group C:\n", all_players.loc[groupC],"\n\n")
print("Group D:\n", all_players.loc[groupD],"\n\n") # subtract 1 because started range at 1. minor inefficiency, fix later.

# %%
