import streamlit as st

# Define poems and images
poems = [
    "Shirley Toulson (1924-2018) was a poet, teacher, educational journalist, editor and author of many books. She was an innovative writer. She had a huge passion for writing and opted writing as career. She is a highly acclaimed poet about British Walks, ancient tracks and traditions.",
    "The poem ""A Photograph"" explores the themes of transience of human life, death, and the mysteries surrounding them. The poet reflects on the photograph of her mother, expressing a sense of longing and missing her. In the image, there is an acquaintance with a picture of a sea-beach featuring three girls, including the poet's mother. The sea depicted in the photograph remains relatively unchanged, serving as a backdrop to the memory of the mother, who has passed away.",
    "The cardboard shows me how it was when the two girl cousins went paddling, each one holding one of my mother's hands, and she the big girl – some twelve years or so. All three stood still to smile through their hair at the uncle with the camera. A sweet face, my mother's, that was before I was born. And the sea, which appears to have changed less, washed their terribly transient feet.",

]

images = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png"
]

def main():
    st.title("A Photograph by Shirley Toulson")
    st.image(images[0])
    st.header("About Shirley Toulson")
    st.image(images[1])
    st.write("""
        Shirley Toulson (1924-2018) was a poet, teacher, educational journalist, editor, and author of many books. She was an innovative writer who had a huge passion for writing and opted for it as a career. Toulson is highly acclaimed for her poetry about British walks, ancient tracks, and traditions.
        """)
    st.header("Theme")
    st.image(images[2])
    st.write("""
        The poem 'A Photograph' explores the themes of transience of human life, death, and the mysteries surrounding them. The poet reflects on the photograph of her mother and the feelings of missing her. There is a juxtaposition between the unchanging sea and the transient nature of human life, particularly emphasized by the untimely death of the poet's mother despite the sea remaining constant.
        """)
    st.header("Synopsis")
    st.image(images[3])
    st.write("""
        The cardboard shows me how it was
        When the two girl cousins went paddling,
        Each one holding one of my mother’s hands,
        And she the big girl – some twelve years or so.
        All three stood still to smile through their hair
        At the uncle with the camera. A sweet face,
        My mother’s, that was before I was born.
        And the sea, which appears to have changed less,
        Washed their terribly transient feet.
        """)
    st.header("First Stage – CHILDHOOD")
    st.image(images[4])
    st.write("""
        Photograph of the poet’s mother
        At the beach
        Enjoying her sea holidays
        Cousins – Betty and Dolly
        The poet’s mother’s age – twelve years or so
        Uncle clicked the photograph
        Sea has changed less
        Mother’s life has changed
        """)
    st.header("Some twenty – thirty – years later")
    st.image(images[5])
    st.write("""
        She’d laugh at the snapshot. “See Betty
        And Dolly,” she’d say, “and look how they
        Dressed us for the beach.” The sea holiday
        Was her past, mine is her laughter. Both wry
        With the laboured ease of loss.
        """)
    st.header("Twenty or thirty years later…")
    st.image(images[6])
    st.write("""
        Memories of the poet
        The poet’s mother laughing at the photograph
        Laughing at the dress
        Sea holiday – an event of past
        Laughter is real and pleasant for the poet
        Sense of loss
        Lost her happy moments of childhood
        """)
    st.header("Now she’s been dead nearly as many years")
    st.write("""
        As that girl lived. And of this circumstance
        There is nothing to say at all.
        Its silence silences.
        """)
    st.header("Thank You")
    st.image(images[7])

if __name__ == "__main__":
    main()
