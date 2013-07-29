from models import *

API_URL = 'https://api.vineapp.com/'
MEDIA_URL = 'http://media.vineapp.com/'

HEADERS = {
    'User-Agent': 'com.vine.iphone/1.0.3 (unknown, iPhone OS 6.0.1, iPhone, Scale/2.000000)',
    'Accept-Language': 'en, sv, fr, de, ja, nl, it, es, pt, pt-PT, da, fi, nb, ko, zh-Hans, zh-Hant, ru, pl, tr, uk, ar, hr, cs, el, he, ro, sk, th, id, ms, en-GB, ca, hu, vi, en-us;q=0.8'
}

OPTIONAL_PARAMS = ['size', 'page', 'anchor']

ENDPOINTS = {

    # Auth
    'login': {
        'endpoint': 'users/authenticate',
        'request_type': 'post',
        'url_params': [],
        'required_params': ['username', 'password'],
        'optional_params': [],
        'model': User
    },
    'logout': {
        'endpoint': 'users/authenticate',
        'request_type': 'delete',
        'url_params': [],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'signup': {
        'endpoint': 'users',
        'request_type': 'post',
        'url_params': [],
        'required_params': ['username', 'password', 'email', 'authenticate'],
        'optional_params': [],
        'default_params': [('authenticate', 1)],
        'model': User
    },

    # Profile
    'get_me': {
        'endpoint': 'users/me',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': [],
        'model': User
    },
    'get_user': {
        'endpoint': 'users/profiles/%s',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': User
    },
    'update_user': {
        'endpoint': 'users/%s',
        'request_type': 'post',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': ['description', 'location', 'locale', 'private', 'phoneNumber'],
        'model': User
    },
    'set_explicit': {
        'endpoint': 'users/%s/explicit',
        'request_type': 'post',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'unset_explicit': {
        'endpoint': 'users/%s/explicit',
        'request_type': 'delete',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },

    # User actions
    'follow': {
        'endpoint': 'users/%s/followers',
        'request_type': 'post',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'unfollow': {
        'endpoint': 'users/%s/followers',
        'request_type': 'delete',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'block': {
        'endpoint': 'users/%s/blocked/%s',
        'request_type': 'post',
        'url_params': ['from_user_id', 'to_user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'unblock': {
        'endpoint': 'users/%s/blocked/%s',
        'request_type': 'delete',
        'url_params': ['from_user_id', 'to_user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'get_pending_notifications_count': {
        'endpoint': 'users/%s/pendingNotificationsCount',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'get_notifications': {
        'endpoint': 'users/%s/pendingNotificationsCount',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },

    # User lists
    'get_followers': {
        'endpoint': 'users/%s/followers',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': UserCollection
    },
    'get_following': {
        'endpoint': 'users/%s/following',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': [],
        'model': UserCollection
    },

    # Posts
    'like': {
        'endpoint': 'posts/%s/likes',
        'request_type': 'post',
        'url_params': ['post_id'],
        'required_params': [],
        'optional_params': [],
        'model': None #likeId
    },
    'unlike': {
        'endpoint': 'posts/%s/likes',
        'request_type': 'delete',
        'url_params': ['post_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'comment': {
        'endpoint': 'posts/%s/comments',
        'request_type': 'post',
        'url_params': ['post_id'],
        'required_params': ['comment', 'entities'],
        'optional_params': [],
        'model': Comment
    },
    'uncomment': {
        'endpoint': 'posts/%s/comments/%s',
        'request_type': 'delete',
        'url_params': ['post_id', 'comment_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'revine': {
        'endpoint': 'posts/%s/repost',
        'request_type': 'post',
        'url_params': ['post_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'unrevine': {
        'endpoint': 'posts/%s/repost/%s',
        'request_type': 'delete',
        'url_params': ['post_id', 'revine_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'report': {
        'endpoint': 'posts/%s/complaints',
        'request_type': 'post',
        'url_params': [],
        'required_params': [],
        'optional_params': [],
        'model': None
    },
    'post': {
        'endpoint': 'posts',
        'request_type': 'post',
        'url_params': [],
        'required_params': ['videoUrl', 'thumbnailUrl', 'description', 'entities'],
        'optional_params': ['forsquareVenueId', 'venueName', 'channelId'],
        'model': None
    },
    'delete_post': {
        'endpoint': 'posts/%s',
        'request_type': 'delete',
        'url_params': ['post_id'],
        'required_params': [],
        'optional_params': [],
        'model': None
    },

    # Timelines
    'get_post': {
        'endpoint': 'timelines/posts/%s',
        'request_type': 'get',
        'url_params': ['post_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_user_timeline': {
        'endpoint': 'timelines/users/%s',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_user_likes': {
        'endpoint': 'timelines/users/%s/likes',
        'request_type': 'get',
        'url_params': ['user_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_tag_timeline': {
        'endpoint': 'timelines/users/%s',
        'request_type': 'get',
        'url_params': ['tag_name'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_main_timeline': {
        'endpoint': 'timelines/graph',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_popular_timeline': {
        'endpoint': 'timelines/popular',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_ontherise_timeline': {
        'endpoint': 'timelines/trending',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_editorpicks_timeline': {
        'endpoint': 'timelines/promoted',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_channel_popular_timeline': {
        'endpoint': 'timelines/channels/%s/popular',
        'request_type': 'get',
        'url_params': ['channel_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_channel_recent_timeline': {
        'endpoint': 'timelines/channels/%s/recent',
        'request_type': 'get',
        'url_params': ['channel_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },
    'get_venue_timeline': {
        'endpoint': 'timelines/venues/%s',
        'request_type': 'get',
        'url_params': ['venue_id'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': PostCollection
    },

    # Tags
    'get_trending_tags': {
        'endpoint': 'tags/trending',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': [],
        'model': TagCollection
    },

    # Channels
    'get_featured_channels': {
        'endpoint': 'channels/featured',
        'request_type': 'get',
        'url_params': [],
        'required_params': [],
        'optional_params': [],
        'model': ChannelCollection
    },

    # Search
    'search_tags': {
        'endpoint': 'tags/search/%s',
        'request_type': 'get',
        'url_params': ['tag_name'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': TagCollection
    },
    'search_users': {
        'endpoint': 'users/search/%s',
        'request_type': 'get',
        'url_params': ['query'],
        'required_params': [],
        'optional_params': OPTIONAL_PARAMS,
        'model': UserCollection
    },

}
