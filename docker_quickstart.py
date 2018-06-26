from instapy import InstaPy
import os

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

insta_username = os.getenv('INSTA_USERNAME', '')
insta_password = os.getenv('INSTA_PASSWORD', '')

dont_like = os.getenv('INSTA_DONT_LIKE', '').split(',')
ignore_words = os.getenv('INSTA_IGNORE_WORDS', '').split(',')
friend_list = os.getenv('INSTA_FRIEND_LIST', ',').split(',')

follow_user_followers = os.getenv('INSTA_FOLLOW_USER_FOLLOWERS', ',').split(',')

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
bot.login()
bot.set_relationship_bounds(enabled=True,
             potency_ratio=-1.21,
              delimit_by_numbers=True,
               max_followers=4590,
                max_following=5555,
                 min_followers=45,
                  min_following=77)

# For 50% of the 30 newly followed, move to their profile
# and randomly choose 5 pictures to be liked.
# Take into account the other set options like the comment rate
# and the filtering for inappropriate words or users
bot.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
bot.follow_user_followers(follow_user_followers, amount=10, randomize=False, interact=True, sleep_delay=60)

bot.unfollow_users(amount=200, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)

#bot.set_do_comment(True, percentage=10)
#bot.set_comments(['Cool!', 'Awesome!', 'Nice!'])
#bot.set_dont_include(friend_list)
#bot.set_dont_like(dont_like)
#bot.set_ignore_if_contains(ignore_words)
#bot.like_by_tags(['dog', '#cat'], amount=100)

bot.end()