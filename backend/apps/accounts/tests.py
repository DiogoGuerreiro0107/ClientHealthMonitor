from django.test import TestCase
from django.db import IntegrityError, transaction
from apps.accounts.models import AppUser, AppUserRole

class UserTestCase(TestCase):
    
    def test_default_user_creation(self):
        AppUser.objects.create_user(email="test@test.pt", password="test@1234")
        user = AppUser.objects.get(email="test@test.pt")
        self.assertEqual(user.email, "test@test.pt")
        self.assertTrue(user.check_password("test@1234"))
        self.assertEqual(user.role, AppUserRole.VIEWER)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_get_user_by_email(self):
        AppUser.objects.create_user(email="test@test.pt", password="test")
        user = AppUser.objects.get(email="test@test.pt")
        self.assertEqual(user, AppUser.objects.get_user_by_email("test@test.pt"))
    
    def test_email_normalization(self):
        AppUser.objects.create_user(email="test@TeST.Pt", password="test@1234")
        user = AppUser.objects.get(email="test@test.pt")
        self.assertEqual(user.email, "test@test.pt")
        
    def test_user_creation_accepts_roles(self):
        AppUser.objects.create_user(email="test1@test.pt", password="test", role=AppUserRole.VIEWER)
        AppUser.objects.create_user(email="test2@test.pt", password="test", role=AppUserRole.TECHNICIAN)
        AppUser.objects.create_user(email="test3@test.pt", password="test", role=AppUserRole.ADMIN)
        
        user1 = AppUser.objects.get(email="test1@test.pt")
        self.assertEqual(user1.email, "test1@test.pt")
        self.assertEqual(user1.role, AppUserRole.VIEWER)
        
        user2 = AppUser.objects.get(email="test2@test.pt")
        self.assertEqual(user2.email, "test2@test.pt")
        self.assertEqual(user2.role, AppUserRole.TECHNICIAN)
        
        user3 = AppUser.objects.get(email="test3@test.pt")
        self.assertEqual(user3.email, "test3@test.pt")
        self.assertEqual(user3.role, AppUserRole.ADMIN)
    
    def test_default_superuser_creation(self):
        AppUser.objects.create_superuser(email="test@test.pt", password="test@1234")
        user = AppUser.objects.get(email="test@test.pt")
        self.assertEqual(user.email, "test@test.pt")
        self.assertTrue(user.check_password("test@1234"))
        self.assertEqual(user.role, AppUserRole.ADMIN)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
    def test_duplicate_account_exception(self):
        AppUser.objects.create_user(email="test@test.pt", password="test@1234")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                AppUser.objects.create_user(
                    email="test@test.pt",
                    password="test@1234",
                )

    def test_empty_password_exception(self):
        with self.assertRaises(ValueError):
            AppUser.objects.create_user(email="test@test.pt", password="")

    def test_empty_email_exception(self):
        with self.assertRaises(ValueError):
            AppUser.objects.create_user(email="", password="test")

    def test_invalid_role_exception(self):
        with self.assertRaises(ValueError):
            AppUser.objects.create_user(email="test@test.pt", password="test", role="B")
            
        with self.assertRaises(ValueError):
            AppUser.objects.create_superuser(email="test@test.pt", password="test", role="B")
            
        with self.assertRaises(ValueError):
            AppUser.objects.create_superuser(email="test@test.pt", password="test", role=AppUserRole.VIEWER)
            
        with self.assertRaises(ValueError):
            AppUser.objects.create_superuser(email="test@test.pt", password="test", role=AppUserRole.TECHNICIAN)

    def test_staff_flag_validation(self):
        with self.assertRaises(ValueError):
            AppUser.objects.create_user(email="test@test.pt", password="test", role=AppUserRole.ADMIN, is_staff=True)
            
        with self.assertRaises(ValueError):
            AppUser.objects.create_superuser(email="test@test.pt", password="test", role=AppUserRole.ADMIN, is_staff=False)

    def test_superuser_validation(self):
        with self.assertRaises(ValueError):
            AppUser.objects.create_user(email="test@test.pt", password="test", role=AppUserRole.ADMIN, is_superuser=True)
            
        with self.assertRaises(ValueError):
            AppUser.objects.create_superuser(email="test@test.pt", password="test", role=AppUserRole.ADMIN, is_superuser=False)

    def test_missing_email_exception(self):
        with self.assertRaises(ValueError):
            AppUser.objects.get_user_by_email("test@test.pt")