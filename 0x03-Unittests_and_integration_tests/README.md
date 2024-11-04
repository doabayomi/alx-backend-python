# Python Unittest Quick Notes

## PropertyMock
- **`PropertyMock`** is used to mock a property of a class within tests.
- It is particularly useful when you need to mock a `@property` in an instance.
- **Example**:
  ```python
  from unittest.mock import PropertyMock, patch

  class MyClass:
      @property
      def my_property(self):
          return "original_value"

  with patch.object(MyClass, 'my_property', new_callable=PropertyMock) as mock_prop:
      mock_prop.return_value = "mocked_value"
      instance = MyClass()
      print(instance.my_property)  # Outputs: "mocked_value"
  ```

## Patch
- **`patch`** temporarily replaces the target object with a mock, useful for isolating tests from dependencies.
- Can be used as a **decorator**, **context manager**, or in `setUp`/`tearDown` methods.
- **Example as a decorator**:
  ```python
  from unittest.mock import patch

  @patch('module.function_to_mock')
  def test_example(mock_func):
      mock_func.return_value = "mocked result"
      result = module.function_to_mock()
      assert result == "mocked result"
  ```

- **Example as a context manager**:
  ```python
  with patch('module.function_to_mock') as mock_func:
      mock_func.return_value = "mocked result"
      result = module.function_to_mock()
      assert result == "mocked result"
  ```

## setUpClass and tearDownClass
- **`setUpClass`** and **`tearDownClass`** are class-level setup and teardown methods in `unittest`.
- **`setUpClass`** runs once before any tests in the class, while **`tearDownClass`** runs once after all tests have finished.
- Often used for expensive setup/teardown tasks (e.g., establishing database connections).
- **Example**:
  ```python
  import unittest

  class MyTestClass(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
          cls.resource = "Set up resource"

      @classmethod
      def tearDownClass(cls):
          cls.resource = None

      def test_example(self):
          self.assertEqual(self.resource, "Set up resource")
  ```

--- 

**Summary**:
- **`PropertyMock`** mocks properties.
- **`patch`** replaces objects or functions temporarily.
- **`setUpClass` / `tearDownClass`** manage resources at the class level for setup and teardown.
```

