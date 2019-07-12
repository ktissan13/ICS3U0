# Election
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

# Awbrey votes
Awbrey_New_York = 314159
Awbrey_New_Jersey = 89008
Awbrey_Connecticut = 213451

Total_Awbrey_Votes = Awbrey_New_York + Awbrey_New_Jersey + Awbrey_Connecticut

# Martinez Votes
Martinez_New_York = 271860
Martinez_New_Jersey = 121032
Martinez_Connecticut = 231034

Total_Martinez_Votes = Martinez_New_York + Martinez_New_Jersey + Martinez_Connecticut

Total_Votes = Total_Awbrey_Votes + Total_Martinez_Votes

Awbrey_percent = (Total_Awbrey_Votes/Total_Votes)*100
Martinez_percent = (Total_Martinez_Votes/Total_Votes)*100

print("%-10s %13s %13s"%("Candidate", "Votes", "Percentage"))
print("%-10s %13s %13s"%("Awbrey", Total_Awbrey_Votes, "%.2f"%Awbrey_percent+"%"))
print("%-10s %13s %13s"%("Martinez", Total_Martinez_Votes, "%.2f"%Martinez_percent+"%"))
print()
print("%-10s %10s"%("TOTAL VOTES: ", Total_Votes))
