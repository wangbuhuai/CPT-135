# Created by Dayu Wang (dwang@stchas.edu) on 2022-06-04

# Last updated by Dayu Wang (dwang@stchas.edu) on 2022-06-04


def are_anagrams(s, t):
    """ Tests whether two strings are anagrams
        :param s: first string to test
        :type s: str
        :param t: second string to test
        :type t: str
        :return: True if the two strings are anagrams; False otherwise
        :rtype: bool
    """
    return sorted(s) == sorted(t)


def is_palindromic(s):
    """ Tests whether a string is a palindrome
        :param s: string to test
        :type s: str
        :return: True if the string is palindromic; False otherwise
        :rtype: bool
    """
    # If the reversed string is the same as original, then it is palindromic.
    return s == s[::-1]


def majority_element(li):
    """ Finds the majority element for a list of integers
        :param li: non-empty list guaranteed to have a majority element
        :type li: List[int]
        :return: majority element of the list
        :rtype: int
    """
    # For sorted list, majority element is always the middle element.
    return sorted(li)[len(li) // 2]


def remove_whitespaces(s):
    """ Removes all the whitespaces in a string
        :param s: a string to remove the whitespaces in it
        :type s: str
        :return: a copy of input string with all whitespaces removed
        :rtype: str
    """
    # Split the string using whitespaces,
    # then join the tokens using empty string.
    return ''.join(s.split())


def longest_increasing_segment(li):
    """ Finds the length of the longest increasing segment in a list
        :param li: a list to find the length of its longest increasing segment
        :type li: List[int]
        :return: length of the longest increasing segment in the list
        :rtype: int
    """
    begin = 0  # Beginning index of current increasing segment
    end = 0  # End index of current increasing segment
    length = 1  # Length of current longest increasing segment
    for i in range(1, len(li) + 1):
        if i < len(li) and li[i] > li[i - 1]:
            # If current value is greater than the previous value,
            # then current increasing segment is growing.
            end = i  # 'i' is the new end index.
        else:
            # If current value is smaller than the previous value,
            # then a whole increasing segment is found.
            size = end - begin + 1
            # If the segment just found is longer than the longest seen so far,
            # then "length" needs to be updated.
            if size > length:
                length = size
            # Initialize the next increasing segment.
            begin = end = i
    return length


class Cuboid:
    # Constructor
    def __init__(self, length=0, width=0, height=0):
        """ Constructs a Cuboid object
            :param length: initial length of the cuboid
            :type length: int
            :param width: initial width of the cuboid
            :type width: int
            :param height: initial height of the cuboid
            :type height: int
            :return: None
        """
        # Data fields
        self._length = length
        self._width = width
        self._height = height

    # Getters

    def get_length(self):
        """ Returns the length of the cuboid
            :return: length of the cuboid
            :rtype: int
        """
        return self._length

    def get_width(self):
        """ Returns the width of the cuboid
            :return: width of the cuboid
            :rtype: int
        """
        return self._width

    def get_height(self):
        """ Returns the height of the cuboid
            :return: height of the cuboid
            :rtype: int
        """
        return self._height

    # Setters

    def set_length(self, length):
        """ Updates the length of the cuboid
            :param length: updated length of the cuboid
            :type length: int
            :return: None
        """
        self._length = length

    def set_width(self, width):
        """ Updates the width of the cuboid
            :param width: updated width of the cuboid
            :type width: int
            :return: None
        """
        self._width = width

    def set_height(self, height):
        """ Updates the height of the cuboid
            :param height: updated height of the cuboid
            :type height: int
            :return: None
        """
        self._height = height

    # Methods

    def volume(self):
        """ Calculates the volume of the cuboid
            :return: calculated volume of the cuboid
            :rtype: int
        """
        return self.get_length() * self.get_width() * self.get_height()

    def surface_area(self):
        """ Calculates the surface area of the cuboid
            :return: calculated surface area of the cuboid
            :rtype: int
        """
        face_1 = self.get_length() * self.get_width()
        face_2 = self.get_length() * self.get_height()
        face_3 = self.get_width() * self.get_height()
        return 2 * (face_1 + face_2 + face_3)


class Pair:
    # Constructor
    def __init__(self, first='', second=0):
        """ Constructs a Pair object
            :param first: first value in the pair
            :type first: str
            :param second: second value in the pair
            :type second: int
            :return: None
        """
        # Data fields
        self._first = first
        self._second = second

    # Getters

    def get_first(self):
        """ Returns the first value in the pair
            :return: first value in the pair
            :rtype: str
        """
        return self._first

    def get_second(self):
        """ Returns the second value in the pair
            :return: second value in the pair
            :rtype: int
        """
        return self._second

    # Setters

    def set_first(self, first):
        """ Updates the first value in the pair
            :param first: updated first value in the pair
            :type first: str
            :return: None
        """
        self._first = first

    def set_second(self, second):
        """ Updates the second value in the pair
            :param second: updated second value in the pair
            :type second: int
            :return: None
        """
        self._second = second

    # Method

    def __str__(self):
        """ Customizes the output format of the pair
            :return: a string representing the output format of the pair
            :rtype: str
        """
        return "(%s, %d)" % (self.get_first(), self.get_second())


def make_pair(first, second):
    """ Forms a Pair object from a string and an integer
        :param first: first value (string) in the pair
        :type first: str
        :param second: second value (integer) in the pair
        :type second: int
        :return: a Pair object formed by the string and integer
        :rtype: Pair
    """
    return Pair(first, second)


class Currency:
    # Constructor
    def __init__(self, dollar=0, cent=0):
        """ Constructs a Currency object
            :param dollar: initial dollar amount
            :type dollar: int
            :param cent: initial cent amount
            :type cent: int
            :return: None
        """
        # Data fields
        self._dollar = dollar
        self._cent = cent

        self._reduce()  # Reduce the dollar and cent amounts to irreducible form.

    # Getters

    def get_dollar(self):
        """ Returns the dollar amount
            :return: dollar amount
            :rtype: int
        """
        return self._dollar

    def get_cent(self):
        """ Returns the cent amount
            :return: cent amount
            :rtype: int
        """
        return self._cent

    # Setters

    def set_dollar(self, dollar):
        """ Updates the dollar amount
            :param dollar: updated dollar amount
            :type dollar: int
            :return: None
        """
        self._dollar = dollar

    def set_cent(self, cent):
        """ Updates the cent amount
            :param cent: updated cent amount
            :type cent: int
            :return: None
        """
        self._cent = cent
        if cent >= 100:
            self._reduce()

    # Methods

    def _reduce(self):
        """ Reduces the dollar and cent amount to irreducible form
            :return: None
        """
        self.set_dollar(self.get_dollar() + self.get_cent() // 100)
        self.set_cent(self.get_cent() % 100)

    def __str__(self):
        """ Customizes the output format of the Currency object
            :return: a string representing the output format of the Currency object
            :rtype: str
        """
        return "$%d.%02d" % (self.get_dollar(), self.get_cent())


class Rectangle:
    # Constructor
    def __init__(self, width=0, height=0):
        """ Constructs a Rectangle object
            :param width: initial width of the rectangle
            :type width: int
            :param height: initial height of the rectangle
            :type height: int
            :return: None
        """
        # Data fields
        self._width = width
        self._height = height

    # Getters

    def get_width(self):
        """ Returns the width of the rectangle
            :return: width of the rectangle
            :rtype: int
        """
        return self._width

    def get_height(self):
        """ Returns the height of the rectangle
            :return: height of the rectangle
            :rtype: int
        """
        return self._height

    # Setters

    def set_width(self, width):
        """ Updates the width of the rectangle
            :param width: updated width of the rectangle
            :type width: int
            :return: None
        """
        self._width = width

    def set_height(self, height):
        """ Updates the height of the rectangle
            :param height: updated height of the rectangle
            :type height: int
            :return: None
        """
        self._height = height

    # Methods

    def area(self):
        """ Calculates the area of the rectangle
            :return: calculated area of the rectangle
            :rtype: int
        """
        return self.get_width() * self.get_height()

    def __lt__(self, other):
        """ Overloads operator '<' to compare with another rectangle
            :param other: another rectangle to compare
            :type other: Rectangle
            :return: True if this rectangle has smaller area; False otherwise
            :rtype: bool
        """
        return self.area() < other.area()


class TimeSpan:
    # Constructor
    def __init__(self, hour=0, minute=0):
        """ Constructs a TimeSpan object
            :param hour: initial number of hours
            :type hour: int
            :param minute: initial number of minutes
            :type minute: int
            :return: None
        """
        # Data fields
        self._hour = hour
        self._minute = minute

        self._reduce()  # Reduce hour and minute to irreducible form.

    # Getters

    def get_hour(self):
        """ Returns the number of hours in the time span
            :return: number of hours in the time span
            :rtype: int
        """
        return self._hour

    def get_minute(self):
        """ Returns the number of minutes in the time span
            :return: number of minutes in the time span
            :rtype: int
        """
        return self._minute

    # Setters

    def set_hour(self, hour):
        """ Updates the number of hours in the time span
            :param hour: updated number of hours in the time span
            :type hour: int
            :return: None
        """
        self._hour = hour

    def set_minute(self, minute):
        """ Updates the number of the minutes in the time span
            :param minute: updated number of minutes in the time span
            :type minute: int
            :return: None
        """
        self._minute = minute
        if minute >= 60:
            self._reduce()  # Reduce hour and minute to irreducible form.

    # Methods

    def _reduce(self):
        """ Reduces hour and minute to irreducible form
            :return: None
        """
        self.set_hour(self.get_hour() + self.get_minute() // 60)
        self.set_minute(self.get_minute() % 60)

    def __eq__(self, other):
        """ Overloads operator "==" to compare two TimeSpan objects
            :param other: another time span to compare
            :type other: TimeSpan
            :return: True if the two time spans are equal; False otherwise
            :rtype: bool
        """
        return self.get_hour() == other.get_hour() \
            and self.get_minute() == other.get_minute()

    def __add__(self, other):
        """ Overloads operator '+' to add two TimeSpan objects
            :param other: another time span to add to this object
            :type other: TimeSpan
            :return: addition result
            :rtype: TimeSpan
        """
        result = TimeSpan()
        result.set_hour(self.get_hour() + other.get_hour())
        result.set_minute(self.get_minute() + other.get_minute())
        return result
