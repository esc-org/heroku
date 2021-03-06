import tweepy
import os
import time
import json

auth = tweepy.OAuthHandler(os.getenv('TW_CK'), os.getenv('TW_CS'))
API = tweepy.API(auth)


def main():
    if os.getenv('MEMBER_FETCHED'):
        if float(os.getenv('MEMBER_FETCHED')) + 900 >= time.time():
            resdict = json.loads(os.getenv('MEMBER_RESDICT'))
            return resdict
    resdict = {'users': []}
    for user in tweepy.Cursor(
        API.list_members, slug=os.getenv('TWLIST_SLUG'), owner_screen_name='laddge_'
    ).items():
        d = {
            'name': user.name,
            'screen_name': user.screen_name,
            'image': user.profile_image_url_https.replace('_normal', ''),
            'description': user.description,
        }
        resdict['users'].append(d)
    os.environ['MEMBER_RESDICT'] = json.dumps(resdict)
    os.environ['MEMBER_FETCHED'] = str(time.time())
    print('updated members dict')
    return resdict


if __name__ == '__main__':
    print(main())
