"""
Examples :

>>> data = {
    "hobbies": ["Reading", "Hiking", "Travelling"],
    "age": "30",
    "marks": "34",
    "nums": [1, 2, 3, 4]
}
>>> expr = "hobbies + hobbies"
>>> parse(data, expr)
"['Reading', 'Hiking', 'Travelling', 'Reading', 'Hiking', 'Travelling']"

>>> data = {
    "hobbies": ["Reading", "Hiking", "Travelling"],
    "age": "30",
    "marks": "34",
    "nums": [1, 2, 3, 4]
}
>>> expr = "age + marks"
>>> parse(data, expr)
"3034"

>>> data = {
    "hobbies": ["Reading", "Hiking", "Travelling"],
    "age": "30",
    "marks": "34",
    "nums": [1, 2, 3, 4]
}
>>> expr = "nums[1] + nums[3]"
>>> parse(data, expr)
"6"

>>> data = {
    "hobbies": ["Reading", "Hiking", "Travelling"],
    "age": "30",
    "marks": "34",
    "nums": [1, 2, 3, 4]
}
>>> expr = '"he is " + age + " but still he got " + marks + " marks"'
>>> parse(data, expr)
"he is 30 but still he got 34 marks"


"""