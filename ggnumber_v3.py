#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import re


def count_occurences_in_text(word, text):
    """
    Return the number of occurences of the passed word (case insensitive) in text
    """
    count = 0
    text_without_puntuation = (
        re.sub(r"[.!,;?\"\'<>./'?«@»#$%^&*_~]", " ", text).lower().split()
    )
    print(text_without_puntuation)
    for x in text_without_puntuation:
        if word.lower() == x:
            count += 1
    return count

    # This does not pass the unittests:
    # return text.count(word)


class TestCountOccurencesInText(unittest.TestCase):
    def test_count_occurences_in_text(self):
        """
        Test the count_occurences_in_text function
        """
        text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
    Yes is is true, I like PYTHON
    and my name is GEORGES"""
        # test with a little text.
        self.assertEqual(3, count_occurences_in_text("Georges", text))
        self.assertEqual(3, count_occurences_in_text("GEORGES", text))
        self.assertEqual(3, count_occurences_in_text("georges", text))
        self.assertEqual(0, count_occurences_in_text("george", text))
        self.assertEqual(3, count_occurences_in_text("python", text))
        self.assertEqual(3, count_occurences_in_text("PYTHON", text))
        self.assertEqual(2, count_occurences_in_text("I", text))
        self.assertEqual(0, count_occurences_in_text("n", text))
        self.assertEqual(1, count_occurences_in_text("true", text))
        # regard ' as text:
        # self.assertEqual(
        # 0, count_occurences_in_text("maley", "John O'maley is my friend")
        # )

        # Test it but with a BIG length file. (we once had a memory error with this...)
        text = (
            """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
            * 500
        )
        text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
        text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
        text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
        text += (
            """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
            * 500
        )
        text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
        text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
        text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
        text += (
            """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
            * 500
        )
        text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
        text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
        text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
        text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
        text += (
            """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
            * 500
        )
        text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
        text += (
            """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
            * 500
        )

        self.assertEqual(3, count_occurences_in_text("Georges", text))
        self.assertEqual(3, count_occurences_in_text("GEORGES", text))
        self.assertEqual(3, count_occurences_in_text("georges", text))
        self.assertEqual(0, count_occurences_in_text("george", text))
        self.assertEqual(3, count_occurences_in_text("python", text))
        self.assertEqual(3, count_occurences_in_text("PYTHON", text))
        self.assertEqual(2, count_occurences_in_text("I", text))
        self.assertEqual(0, count_occurences_in_text("n", text))
        self.assertEqual(1, count_occurences_in_text("true", text))
        self.assertEqual(
            0,
            count_occurences_in_text(
                "reflexion mirror",
                "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "'reflexion mirror'",
                "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida",
            ),
        )

        #self.assertEqual(
        # 1,
        # count_occurences_in_text(
        # "reflexion mirror",
        # "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida",
        # ),
        # )
        # self.assertEqual(
        # 1,
        # count_occurences_in_text(
        # "reflexion mirror", 'Reflexion Mirror" in Sopchoppy, Florida'
        # ),
        # )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "reflexion mirror",
                "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "reflexion mirror",
                "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "legitimate",
                "who is approved by OILS is completely legitimate: their employees are of legal working age",
            ),
        )
        self.assertEqual(
            0,
            count_occurences_in_text(
                "legitimate their",
                "who is approved by OILS is completely legitimate: their employees are of legal working age",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "get back to me",
                "I hope you will consider this proposal, and get back to me as soon as possible",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "skin-care",
                "enable Delavigne and its subsidiaries to create a skin-care monopoly",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "skin-care monopoly",
                "enable Delavigne and its subsidiaries to create a skin-care monopoly",
            ),
        )
        self.assertEqual(
            0,
            count_occurences_in_text(
                "skin-care monopoly in the US",
                "enable Delavigne and its subsidiaries to create a skin-care monopoly",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "get back to me", "When you know:get back to me"
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "don't be left",
                """emergency alarm warning.
    Don't be left unprotected. Order your SSSS3000 today!""",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "don",
                """emergency alarm warning.
    Don't be left unprotected. Order your don SSSS3000 today!""",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "take that as a 'yes'", "Do I have to take that as a 'yes'?"
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "don't take that as a 'yes'", "I don't take that as a 'yes'?"
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "take that as a 'yes'", "I don't take that as a 'yes'?"
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text("don't", "I don't take that as a 'yes'?"),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "attaching my c.v. to this e-mail",
                "I am attaching my c.v. to this e-mail.",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist",
                "'''Linguist Specialist Found Dead on Laboratory Floor'''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist Specialist",
                "'''Linguist Specialist Found Dead on Laboratory Floor'''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Laboratory Floor",
                "'''Linguist Specialist Found Dead on Laboratory Floor'''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Floor",
                "'''Linguist Specialist Found Dead on Laboratory Floor'''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Floor",
                "''Linguist Specialist Found Dead on Laboratory Floor''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Floor",
                "__Linguist Specialist Found Dead on Laboratory Floor__",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Floor",
                "'''''Linguist Specialist Found Dead on Laboratory Floor'''''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist",
                "'''Linguist Specialist Found Dead on Laboratory Floor'''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist",
                "''Linguist Specialist Found Dead on Laboratory Floor''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist",
                "__Linguist Specialist Found Dead on Laboratory Floor__",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Linguist",
                "'''''Linguist Specialist Found Dead on Laboratory Floor'''''",
            ),
        )
        self.assertEqual(
            1,
            count_occurences_in_text(
                "Floor",
                """Look: ''Linguist Specialist Found Dead on Laboratory Floor'' is the headline today.""",
            ),
        )


SAMPLE_TEXT_FOR_BENCH = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
 Bob Carter
"""


def doit():
    """
    Run count_occurences_in_text on a few examples
    """
    i = 0
    for x in range(400):
        i += count_occurences_in_text("word", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("sugar", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("help", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("heavily", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("witfull", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("dog", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("almost", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("insulin", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("attaching", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("asma", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("neither", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("won't", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("green", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurences_in_text("parabole", SAMPLE_TEXT_FOR_BENCH)
    print(i)


# Start the tests
if __name__ == "__main__":
    # I need to be fast as well:
    import profile

    profile.run("doit()")

    # I need to pass the test:
    unittest.main()
