from django.test import TestCase

from settings.models import Activity, Tag
from tracker.models import Customer, Group, Project, Element


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(customer_name='Customer', country='Country', city='City', street='Street', postal='Postal') # pylint: disable=maybe-no-member

    # max lengths
    def test_customer_name_max_length(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = customer._meta.get_field('customer_name').max_length
        self.assertEqual(max_length, 50)

    def test_country_max_length(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = customer._meta.get_field('country').max_length
        self.assertEqual(max_length, 50)

    def test_city_max_length(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = customer._meta.get_field('city').max_length
        self.assertEqual(max_length, 50)

    def test_street_max_length(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = customer._meta.get_field('street').max_length
        self.assertEqual(max_length, 50)

    def test_postal_max_length(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = customer._meta.get_field('postal').max_length
        self.assertEqual(max_length, 20)
    # __str__
    def test_object_name(self):
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        expected_object_name = f'{customer.customer_name}'
        self.assertEquals(expected_object_name, str(customer))
    
class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(customer_name='Customer', country='Country', city='City', street='Street', postal='Postal') # pylint: disable=maybe-no-member
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        Group.objects.create(group_name='Test Group', customer_id=customer, active=True) # pylint: disable=maybe-no-member

    # max lengths
    def test_group_name_max_length(self):
        group = Group.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = group._meta.get_field('group_name').max_length
        self.assertEqual(max_length, 20)

    # __str__
    def test_object_name(self):
        group = Group.objects.get(id=1) # pylint: disable=maybe-no-member
        expected_object_name = f'{group.group_name}'
        self.assertEquals(expected_object_name, str(group))
    
class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(customer_name='Customer', country='Country', city='City', street='Street', postal='Postal') # pylint: disable=maybe-no-member
        customer = Customer.objects.get(id=1) # pylint: disable=maybe-no-member
        Project.objects.create(project_name='Test Group', customer_id=customer, active=True) # pylint: disable=maybe-no-member

    # max lengths
    def test_project_name_max_length(self):
        project = Project.objects.get(id=1) # pylint: disable=maybe-no-member
        max_length = project._meta.get_field('project_name').max_length
        self.assertEqual(max_length, 20)

    # __str__
    def test_object_name(self):
        project = Project.objects.get(id=1) # pylint: disable=maybe-no-member
        expected_object_name = f'{project.project_name}'
        self.assertEquals(expected_object_name, str(project))

class ElementModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        a1 = Activity.objects.create(activity_name='TG1', description='Engineering', productive=True)
        a2 = Activity.objects.create(activity_name='TG2', description='Sales')

        t1 = Tag.objects.create(tag_name='Testing', tag_hex='000000')
        t2 = Tag.objects.create(tag_name='Test2', tag_hex='111111')

        c = Customer.objects.create(customer_name='Test Customer', country='Test Country')
        
        g1 = Group.objects.create(group_name='Test Group', customer_id=c)
        g2 = Group.objects.create(group_name='No Customer')

        p1 = Project.objects.create(project_name='Test Project', customer_id=c)
        p2 = Project.objects.create(project_name='No Customer')

        e1 = Element.objects.create(group=g1, activity=a1, code_act_type='012', description='has code')
        e2 = Element.objects.create(group=g2, activity=a1, description='No act code')
        e3 = Element.objects.create(project=p1, activity=a2, description='No act code')

        e4 = Element.objects.create(activity=a1, description='No Proj No group')

    def test_code_act_type_max_length(self):
        e = Element.objects.get(id=1)
        max_length = e._meta.get_field('code_act_type').max_length
        self.assertEqual(max_length, 3)

    def test_receiver_ccenter_max_length(self):
        e = Element.objects.get(id=1)
        max_length = e._meta.get_field('receiver_ccenter').max_length
        self.assertEqual(max_length, 5)

    def test_description_max_length(self):
        e = Element.objects.get(id=1)
        max_length = e._meta.get_field('description').max_length
        self.assertEqual(max_length, 20)

    def test_wbs_element_max_length(self):
        e = Element.objects.get(id=1)
        max_length = e._meta.get_field('wbs_element').max_length
        self.assertEqual(max_length, 20)

    # properties
    def test_activity_type_has_code_act_type(self):
        e1 = Element.objects.get(id=1)
        act_type = e1.activity_type
        self.assertEqual(act_type,f'{e1.activity.activity_name}{e1.code_act_type}')
    
    def test_activity_type_has_no_code(self):
        e2 = Element.objects.get(id=2)
        act_type = e2.activity_type
        self.assertEqual(act_type, None)

    def test_project_or_group_name_is_group(self):
        e2 = Element.objects.get(id=2)
        name = e2.project_or_group_name
        self.assertEqual(name, e2.group.group_name)

    def test_project_or_group_name_is_project(self):
        e3 = Element.objects.get(id=3)
        name = e3.project_or_group_name
        self.assertEqual(name, e3.project.project_name)
    
    def test_project_or_group_name_is_none(self):
        e4 = Element.objects.get(id=4)
        name = e4.project_or_group_name
        self.assertEqual(name,None)