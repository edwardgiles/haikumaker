from itertools import cycle
from queue import Queue
import re
import random
# This is a block of text extracted from http://en.wikipedia.org/wiki/Poetry
srctxt = """Poetry is a form of literature that uses aesthetic and rhythmic qualities of language such as phonaesthetics
 sound symbolism, and metre to evoke meanings in addition to, or in place of, the prosaic ostensible meaning. Poetry has
 a long history, dating back to the Sumerian Epic of Gilgamesh. Early poems evolved from folk songs such as the Chinese
 Shijing, or from a need to retell oral epics, as with the Sanskrit Vedas, Zoroastrian Gathas, and the Homeric epics,
 the Iliad and the Odyssey. Ancient attempts to define poetry, such as Aristotle's Poetics, focused on the uses of
 speech in rhetoric, drama, song and comedy. Later attempts concentrated on features such as repetition, verse form and
 rhyme, and emphasized the aesthetics which distinguish poetry from more objectively informative, prosaic forms of
 writing. From the mid-20th century, poetry has sometimes been more generally regarded as a fundamental creative act
 employing language. Poetry uses forms and conventions to suggest differential interpretation to words, or to evoke
 emotive responses. Devices such as assonance, alliteration, onomatopoeia and rhythm are sometimes used to achieve
 musical or incantatory effects. The use of ambiguity, symbolism, irony and other stylistic elements of poetic diction
 often leaves a poem open to multiple interpretations. Similarly figures of speech such as metaphor, simile and metonymy
 create a resonance between otherwise disparate images-a layering of meanings, forming connections previously not
 perceived. Kindred forms of resonance may exist, between individual verses, in their patterns of rhyme or rhythm. Some
 poetry types are specific to particular cultures and genres and respond to characteristics of the language in which the
 poet writes. Readers accustomed to identifying poetry with Dante, Goethe, Mickiewicz and Rumi may think of it as
 written in lines based on rhyme and regular meter; there are, however, traditions, such as Biblical poetry, that use
 other means to create rhythm and euphony. Much modern poetry reflects a critique of poetic tradition, playing with and
 testing, among other things, the principle of euphony itself, sometimes altogether forgoing rhyme or set rhythm. In
 today's increasingly globalized world, poets often adapt forms, styles and techniques from diverse cultures and
 languages. Classical thinkers employed classification as a way to define and assess the quality of poetry. Notably,
 the existing fragments of Aristotle's Poetics describe three genres of poetry the epic, the comic, and the tragic and
 develop rules to distinguish the highest-quality poetry in each genre, based on the underlying purposes of the genre.
 Later aestheticians identified three major genres: epic poetry, lyric poetry, and dramatic poetry, treating comedy and
 tragedy as subgenres of dramatic poetry."""
source = cycle(srctxt)

def read_word():
    builder = list()
    for c in source:
        if c.isalpha():
            builder.append(c)
            break
        else:
            continue
    for c in source:
        if c.isalpha():
            builder.append(c)
        else:
            break
    return ''.join(builder)

A = re.compile("[aeiouy]+")
B = re.compile("[aeiouy][lr]?[^aeiouy]e[^lrmn]|ely")
C = re.compile("oe[tm]|ses|omedy|aic")
def count_syllables(t):
    tx = t.lower() + " "
    return len(A.findall(tx)) - len(B.findall(tx)) + len(C.findall(tx))

def get_line(target_syllables):
    word_queue = Queue()
    syllable_count = 0
    while not syllable_count == target_syllables:
        while syllable_count < target_syllables:
            temp_w = read_word()
            syllable_count += count_syllables(temp_w)
            word_queue.put(temp_w)
        while syllable_count > target_syllables:
            temp_w = word_queue.get()
            syllable_count -= count_syllables(temp_w)
    word_queue.put("&&")
    return ' '.join(iter(word_queue.get, '&&'))

get_line(random.randint(0, 200))
while True:
    print(get_line(5))
    print(get_line(7))
    print(get_line(5))
    input("")
