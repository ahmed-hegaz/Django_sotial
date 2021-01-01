from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals
        
# class UserProfileConfig(AppConfig):
#     name = 'UserProfile'

#     def ready(self):
#         import UserProfile.signals