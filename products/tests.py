# from django.test import TestCase
# from django.core.files.uploadedfile import SimpleUploadedFile
# from PIL import Image
# from io import BytesIO
# from products.models import Product
#
#
# class ProductModelTest(TestCase):
#     def setUp(self):
#         # Create a sample image for testing
#         self.image = Image.new('RGB', (1000, 1000), color='red')
#         self.image_file = BytesIO()
#         self.image.save(self.image_file, 'png')
#         self.image_file.name = 'test.png'
#         self.image_file.seek(0)
#
#         # Create a sample product for testing
#         self.product = Product.objects.create(
#             name='Test Product',
#             description='This is a test product',
#             price=10.99,
#             quantity=5,
#             image=SimpleUploadedFile(self.image_file.name, self.image_file.getvalue())
#         )
#
#     def test_image_upload(self):
#         # Test that the original image was uploaded correctly
#         self.assertEqual(self.product.image.width, 1000)
#         self.assertEqual(self.product.image.height, 1000)
#
#     def test_resized_image_generation(self):
#         # Test that the resized image was generated correctly
#         self.product.save()
#         self.assertTrue(self.product.resize_image)
#
#         resized_image = Image.open(self.product.resize_image.path)
#         self.assertEqual(resized_image.width, 500)
#         self.assertEqual(resized_image.height, 500)
