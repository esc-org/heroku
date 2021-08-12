import tweepy
import os

auth = tweepy.OAuthHandler(os.getenv('TW_CK'), os.getenv('TW_CS'))
API = tweepy.API(auth)


def main():
    resdict = {'users': []}
    for user in tweepy.Cursor(
        API.list_members, slug=os.getenv('TWLIST_SLUG'), owner_screen_name='laddge_'
    ).items():
        d = {
            'name': user.name,
            'screen_name': user.screen_name,
            'image': user.profile_image_url.replace('_normal', ''),
            'description': user.description,
        }
        resdict['users'].append(d)
    return resdict


if __name__ == '__main__':
    print(main())
