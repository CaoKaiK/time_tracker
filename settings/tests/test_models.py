from django.test import TestCase

from settings.models import Activity, Tag

class ActivityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Activity.objects.create(activity_name='Test Activity', description='Test Description', productive=True) # pylint: disable=maybe-no-member
    
    # max lengths
    def test_activity_name_max_length(self):
        activity = Activity.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = activity._meta.get_field('activity_name').max_length
        self.assertEqual(max_length, 3)
    
    def test_description_max_length(self):
        activity = Activity.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = activity._meta.get_field('description').max_length
        self.assertEqual(max_length, 20)

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(tag_name='Red Test Tag', tag_hex='ff0000') # pylint: disable=maybe-no-member
    
    #max lengths
    def test_tag_name_max_length(self):
        tag = Tag.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = tag._meta.get_field('tag_name').max_length
        self.assertEqual(max_length, 20)

    def test_tag_hex_max_length(self):
        tag = Tag.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = tag._meta.get_field('tag_hex').max_length
        self.assertEqual(max_length, 6)