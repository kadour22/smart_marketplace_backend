# # chat/models.py
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Q

# class Conversation(models.Model):
#     participant_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_1')
#     participant_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_2')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = ['participant_1', 'participant_2']
#         ordering = ['-updated_at']

#     def __str__(self):
#         return f"Chat between {self.participant_1.username} and {self.participant_2.username}"

#     @classmethod
#     def get_or_create_conversation(cls, user1, user2):
#         if user1.id > user2.id:
#             user1, user2 = user2, user1
        
#         conversation, created = cls.objects.get_or_create(
#             participant_1=user1,
#             participant_2=user2
#         )
#         return conversation

#     def get_other_participant(self, user):
#         return self.participant_2 if self.participant_1 == user else self.participant_1


# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['timestamp']

#     def __str__(self):
#         return f"{self.sender.username}: {self.content[:50]}"
