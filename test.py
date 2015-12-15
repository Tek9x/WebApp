import json

test = {"title": "Simpsons Roasting", "url": "www.google.com"}

Database = {"Simpsons": {"Season One": {"Episode One": {}}}}

Season_One_Title = ["Simpsons Roasting on an Open Fire", "Bart the Genius", "Homer's Odyssey", "There's No Disgrace Like Home", "Bart the General", "Moaning Lisa", "The Call of the Simpsons"
    , "The Telltale Head"
    , "Life on the Fast Lane"
    , "Homer's Night Out"
    , "The Crepes of Wrath"
    , "Krusty Gets Busted"
    , "Some Enchanted Evening"]

Season_One_Url = [
    '/playback?url=http://videomega.tv/cdn.php?ref=05607808206507308008405207404804807405208408007306508207805'
    , '/playback?url=http://videomega.tv/cdn.php?ref=071067083056077050068056048056056048056068050077056083067071'
    , '/playback?url=http://videomega.tv/cdn.php?ref=069078048086057057069084071051051071084069057057086048078069'
    , '/playback?url=http://videomega.tv/cdn.php?ref=080076052086079070086068068057057068068086070079086052076080'
    , '/playback?url=http://videomega.tv/cdn.php?ref=054084085073078083057074050049049050074057083078073085084054'
    , '/playback?url=http://videomega.tv/cdn.php?ref=048069076078074055071086049057057049086071055074078076069048'
    , '/playback?url=http://videomega.tv/cdn.php?ref=069073074050055057056082070048048070082056057055050074073069'
    , '/playback?url=http://videomega.tv/cdn.php?ref=053065048077068056082075055057057055075082056068077048065053'
    , '/playback?url=http://videomega.tv/cdn.php?ref=053076074073050051081080087056056087080081051050073074076053'
    , '/playback?url=http://videomega.tv/cdn.php?ref=051051049070087065084072050050050050072084065087070049051051'
    , '/playback?url=http://videomega.tv/cdn.php?ref=069082067076065081081086057050050057086081081065076067082069'
    , '/playback?url=http://videomega.tv/cdn.php?ref=077085066066074085067070057057057057070067085074066066085077'
    , '/playback?url=http://videomega.tv/cdn.php?ref=083072082069081075077083068051051068083077075081069082072083']

# Print opening HTML tags -------------------------
print "<htm><body><table>"

for i in range(0, len(Season_One_Title)) and range(0, len(Season_One_Url)):
    print "<tr><td>" + Season_One_Title[i] + "</td><td>" + Season_One_Url[i] + "</td></tr>"

# Print closing HTML tags -------------------------
print "</table></body></html>"
