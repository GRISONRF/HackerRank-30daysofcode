""" 
The people who buy ads on our network don't have enough data about how ads are working for
their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page
after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = [
  "3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a
user clicked on one of our ads:
ad_clicks = [
 #"IP_Address,Time,Ad_Text",
 "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
 "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
 "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
 "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
 "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
 "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
       
The client also sent over the IP addresses of all their users.
       
all_user_ips = [
 #"User_ID,IP_Address",
 "2339985511,122.121.0.155",
 "234111110,122.121.0.1",
 "3123122444,92.130.6.145",
 "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
 "8321125440,82.1.106.8",
 "99911063,92.130.6.144"
]
       
Write a function to parse this data, determine how many times each ad was clicked,
then return the ad text, that ad's number of clicks, and how many of those ad clicks
were from users who made a purchase.


Expected output:
Bought Clicked Ad Text
1 of 2  2017 Pet Mittens
0 of 1  The Best Hollywood Coats
3 of 3  Buy wool coats for your pets """



def adsConversionRate(completedPurchaseUserIds, adClicks, allUserIps):















completedPurchaseUserIds = ["3123122444","234111110", "8321125440", "99911063"]


adClicks= ["122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
 "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
 "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
 "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
 "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
 "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"]

allUserIps = ["2339985511,122.121.0.155",
 "234111110,122.121.0.1",
 "3123122444,92.130.6.145",
 "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
 "8321125440,82.1.106.8",
 "99911063,92.130.6.144"]

print(adsConversionRate(completedPurchaseUserIds, adClicks, allUserIps))



# def adsConversionRate(completedPurchaseUserIds, adClicks, allUserIps):

#     #make completedPurchaseUserIds into a set for fast lookup
#     bought_ids = set(completedPurchaseUserIds) # (id)
#     #dict conversion to store conversion rates for each id  
#     conversion = {}  #{text : [how many bought][clicks] }
#     #dict id_to_ip to map user id to ip
#     id_to_ip = {}  #{id : ip}

#     #iterate over alluserips, split into id and ip and add them into the dict
#     for users in allUserIps:
#         id, user_ip = users.split(',')
#         id_to_ip[user_ip] = id
#     # print(id_to_ip)

#     #iterate over adClicks, split each entry to get the ip address and ad text
#     for click in adClicks:
#         #check if text is already in 'conversion' dict
#         ip, time, text = click.split(',')
#         # print(id_to_ip.get(ip))
#         if text in conversion: #check if this user make a purchase      
#              #add 1 to the clicks 
#             conversion[text][1] += 1
#             # if this ip is in bought ids,
#             if id_to_ip.get(ip) in bought_ids:
#               #add 1 to the bought list inside of conversion -[0]list
#                 conversion[text][0] +=1
                
#         else: #if text it not in conversion
#             #check if user is in bought_is
#             if id_to_ip.get(ip) in bought_ids:
#                 conversion[text] = [1,1]
#             else:        
#                 conversion[text] = [0,1]


#     print(conversion)
#     for ad_text, ratio in conversion.items():
#         print(f'{ratio[0]} of {ratio[1]} {ad_text}')