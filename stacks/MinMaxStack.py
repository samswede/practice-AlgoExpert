import unittest

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = [] # List List int
        self.stack = []

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # Before we can pop, we need to sync the minMaxStack with the stack.
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        pass

    def getMin(self):
        if len(self.minMaxStack) == 0:
            return None
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        if len(self.minMaxStack) == 0:
            return None
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]



class TestProgram(unittest.TestCase):

    def test_case_1(self):
      minMaxStack = MinMaxStack()
      minMaxStack.push(5)
      self.assertEqual(minMaxStack.getMin(), 5)
      self.assertEqual(minMaxStack.getMax(), 5)
      self.assertEqual(minMaxStack.peek(), 5)
      minMaxStack.push(7)
      self.assertEqual(minMaxStack.getMin(), 5)
      self.assertEqual(minMaxStack.getMax(), 7)
      self.assertEqual(minMaxStack.peek(), 7)
      minMaxStack.push(2)
      self.assertEqual(minMaxStack.getMin(), 2)
      self.assertEqual(minMaxStack.getMax(), 7)
      self.assertEqual(minMaxStack.peek(), 2)
      self.assertEqual(minMaxStack.pop(), 2)
      self.assertEqual(minMaxStack.pop(), 7)
      self.assertEqual(minMaxStack.getMin(), 5)
      self.assertEqual(minMaxStack.getMax(), 5)
      self.assertEqual(minMaxStack.peek(), 5)
      self.assertEqual(minMaxStack.pop(), 5)
      self.assertEqual(minMaxStack.getMin(), None)
      self.assertEqual(minMaxStack.getMax(), None)
      self.assertEqual(minMaxStack.peek(), None)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)