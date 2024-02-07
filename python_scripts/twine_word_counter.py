import re
import pyperclip

CLEANR = re.compile("<.*?>")


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, " ", raw_html)
    return cleantext


text = """
Advanced Creative Writing Sample
<div class="title">Skincare for Vampires</div>\
<div class="subtitle handwriting">(and other things that may be of interest to you ♥)</div>\
<div class="subtitle handwriting">(sample ♥)</div>\
<div id="menu">[[Start->intro_1]]</div>
<<set $seen_bed_text = false>>\
[[You look at the magic mirror.->intro_2]]
After you complained that you hated the way you looked, your old adventuring companion, Princesss Philomena the Third, gifted you this magic mirror.

She either did not know, or did not remember, that vampires cannot see themselves in mirrors.
* <<link "<q>Mirror mirror on the wall, how do I prepare for the 143th Blood Ball?</q>" "mirror_rhyme">><</link>>
* <<link "<q>Mirror mirror on the wall can you just tell me what I need to do to prepare for this stupid ball thing since I have no idea what to do but I need to go because why on Earth she would invite me but I don't want to look stupid?</q>" "mirror_no_rhyme">><</link>>
* <<link "(You decide to procrastinate, so you will talk to the mirror later.)" "day_1_hub" >><</link>>
You do not see your <<linkreplace "reflection..." t8n>>reflection, because you are a [[vampire->intro_3]].<</linkreplace>>
But you are not sure how magic mirrors work, so maybe magic mirrors aren't supposed to show your [[reflection->intro_4]].
Still, you want to get this magic mirror working, because <<linkreplace "▒▒▒▒" t8n>><<linkreplace "\[the person you would rather forget\]" t8n>><<linkreplace "Beau" t8n>>your ex<</linkreplace>><</linkreplace>><</linkreplace>> has invited you to <<linkreplace "the 143th Blood Ball..." t8n>>the 143th Blood Ball, and you only have [[five days to prepare for it->day_1_hub]].<</linkreplace>>
<b>Evening, Day 1. [[Your Flat->flat]].</b>

The [[magic mirror->magic_mirror]] is in front of you. Your [[half-broken bed->bed]] is lying at the corner.
Your flat is a total mess. From the swords piling at the washbasin, to the dragon skulls stacked in your bathtub, the magical loot you have gathered from your adventures is strewn all over the place, without a care—because you don't care.

Most of the time, you're fighting monsters somewhere in the West, and you barely spend any time <<return "here">>.
<<if visited("magic_mirror") > 0 and $seen_bed_text is false >>When Princesss Philomena gifted you the magic mirror via a teleportation spell, she rounded the coordinates you gave her to the nearest twenty-five decimal places, instead of at least twenty-seven decimal places, so the magic mirror teleported on top of your bed instead of a more sensible location.

Thankfully, you leaped just in time to catch the mirror and prevent your half-broken bed from becoming a fully-broken bed, but it is still half-broken.
<<set $seen_bed_text = true >>\

* [[(You don't think you should sleep, because you need to talk to the magic mirror.)->day_1_hub]]
<<else>>\
* [[(You don't think you should sleep, because you need to talk to the magic mirror.)->day_1_hub]]\
<</if>>\
Suddenly, green vapour whirls within the mirror's depths, and the face of a white woman with blond hair swirls into view. She glares at you.

The mirror may be satisfied by your attempt at rhyming, but not how you did not keep in meter. Or perhaps, the mirror is simply dissatisfied with you as a person.

<<return "←">>
After you finish your sentence, green vapour whirls within the mirror's depths, and the face of a white woman with blond hair swirls into view. She glares at you.

Perhaps the mirror is dissatisfied by your lack of effort in rhyming, or perhaps the mirror is simply dissatisfied with you as a person.

<<return "←">>
"""

text = text.strip()  # Remove leading and trailing whitespace

text_to_remove = [
    "Advanced Creative Writing Sample",
    '<<back "←">',
    '<<linkreplace "',
    '" t8n>>',
    "<</linkreplace>>",
]

for t in text_to_remove:
    text = text.replace(t, "")  # Replace with empty string to ensure complete removal

text = re.sub(r"\\\[", " [", text)  # Fix escaped brackets
text = re.sub(r"\\\]", "] ", text)  # Fix escaped brackets

text = cleanhtml(text)  # Remove HTML tags and replace them with spaces

res = len(re.findall(r"\w+", text))
word_count = str(res)

text = text.strip()  # Remove leading and trailing whitespace

text = re.sub(r"[ ]+", " ", text)  # Replace multiple spaces with a single space

# pyperclip.copy(text)  # Uncomment to copy to clipboard

print(text, "\n")
print(word_count)
