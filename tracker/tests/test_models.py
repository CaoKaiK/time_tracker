from django.test import TestCase

from tracker.models import Customer, Group, Project

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

