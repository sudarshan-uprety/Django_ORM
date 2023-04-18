from task1.models import SoccerVenue,PlayerMast,GoalDetails,MatchMast,PenaltyShootout,MatchDetails,PlayerInOut,PlayerBooked
from django.db.models import Count,F,Value


#Q.1  From the following table, write a SQL query to count the number of venues for EURO cup 2016. Return number of venues.
SoccerVenue.objects.all().count()


#Q.2 From the following table, write a SQL query to count the number of countries that participated in the 2016-EURO Cup.
PlayerMast.objects.all().distinct('team_id').count()


#Q.3 From the following table, write a SQL query to find the number of goals scored within normal play during the EURO cup 2016.
GoalDetails.objects.all().count()


#Q.4 From the following table, write a SQL query to find the number of matches that ended with a result.
MatchMast.objects.filter(results='WIN').count()


#Q.5 From the following table, write a SQL query to find the number of matches that ended in draws.
MatchMast.objects.filter(results='DRAW').count()


#Q.6 From the following table, write a SQL query to find out when the Football EURO cup 2016 will begin.
MatchMast.objects.filter(match_no=1).values('play_date')


#Q.7 From the following table, write a SQL query to find the number of self-goals scored during the 2016 European Championship.
GoalDetails.objects.filter(goal_type='O').count()


#Q.8 From the following table, write a SQL query to count the number of matches ended with a results in-group stage.
MatchMast.objects.filter(play_stage='G',results='WIN').count()


#Q.9 From the following table, write a SQL query to find the number of matches that resulted in a penalty shootout.
PenaltyShootout.objects.distinct('match_no').count()


#Q.10 From the following table, write a SQL query to find number of matches decided by penalties in the Round 16.
MatchMast.objects.filter(play_stage='R',decided_by='P').count()


#Q.11 From the following table, write a SQL query to find the number of goals scored in every match within a normal play schedule. Sort the result-set on match number. Return match number, number of goal scored.
GoalDetails.objects.values('match_no').annotate(total=Count('*')).order_by('match_no')


#Q.12 From the following table, write a SQL query to find the matches in which no stoppage time was added during the first half of play. Return match no, date of play, and goal scored.
MatchMast.objects.filter(stop1_sec='0').values('match_no', 'play_date', 'goal_score')


#Q.13 From the following table, write a SQL query to count the number of matches that ended in a goalless draw at the group stage. Return number of matches.
MatchDetails.objects.filter(win_lose='D',goal_score='0',play_stage='G').values('match_no').distinct().count()


#Q.14 From the following table, write a SQL query to calculate the number of matches that ended in a single goal win, excluding matches decided by penalty shootouts. Return number of matches. 
MatchDetails.objects.filter(win_lose='W',goal_score='1',decided_by='N').count()


#Q.15 From the following table, write a SQL query to count the number of players replaced in the tournament. Return number of players as "Player Replaced".


# Error in table player_in_out i.e class PlayerInOut, so I have not solved this questions


#Q.19 From the following table, write a SQL query to count the total number of goalless draws played in the entire tournament. Return number of goalless draws.
MatchDetails.objects.filter(win_lose='D', goal_score=0).values('match_no').distinct().aggregate(count=Count('match_no'))


#Q.20 From the following table, write a SQL query to calculate the total number of players who were replaced during the extra time.
PlayerInOut.objects.filter(in_out='I',play_schedule='ET').count()


#Q.21 From the following table, write a SQL query to count the number of substitutes during various stages of the tournament. Sort the result-set in ascending order by play-half, play-schedule and number of substitute happened. Return play-half, play-schedule, number of substitute happened. 
PlayerInOut.objects.filter(in_out='I').values('play_half', 'play_schedule').annotate(count=Count('*')).order_by('play_half', 'play_schedule','count')


#Q.22 From the following table, write a SQL query to count the number of shots taken in penalty shootouts matches. Number of shots as "Number of Penalty Kicks". 
PenaltyShootout.objects.aggregate(num_penalties=Count('*'))['num_penalties']


#Q.23 From the following table, write a SQL query to count the number of shots that were scored in penalty shootouts matches. Return number of shots scored goal as "Goal Scored by Penalty Kicks".
print('Goal Scored by Penalty Kicks',PenaltyShootout.objects.filter(score_goal='Y').count())


#Q.24 From the following table, write a SQL query to count the number of shots missed or saved in penalty shootout matches. Return number of shots missed as "Goal missed or saved by Penalty Kicks".
print('Goal missed or saved by Penalty Kicks: ',PenaltyShootout.objects.filter(score_goal='N').count())

#Q.25 From the following table, write a SQL query to find the players with shot numbers they took in penalty shootout matches. Return match_no, Team, player_name, jersey_no, score_goal, kick_no.
PenaltyShootout.objects.select_related('team','player').annotate(match_number=F('match_no'),country_name=F('team__country_name'),player_name=F('player__player_name'),jersey_no=F('player__jersey_no'),goal_score=Value('score_goal'),Kick_number=F('kick_no')).values('match_no','country_name','player_name','jersey_no','score_goal','kick_no')


#Q.26 From the following table, write a SQL query to count the number of penalty shots taken by each team. Return country name, number of shots as "Number of Shots".
PenaltyShootout.objects.select_related('team').annotate(country_name=F('team__country_name'),count=Count('*')).values('country_name').annotate(count=Count('*'))


#Q.27 From the following table, write a SQL query to count the number of bookings in each half of play within the normal play schedule. Return play_half, play_schedule, number of booking happened. 
PlayerBooked.objects.filter(play_schedule='NT').values('play_half','play_schedule').annotate(count=Count('*'))


#Q.28 From the following table, write a SQL query to count the number of bookings during stoppage time.
PlayerBooked.objects.filter(play_schedule='ST').count()


#Q.29 From the following table, write a SQL query to count the number of bookings that happened in extra time. 
PlayerBooked.objects.filter(play_schedule='ET').count()