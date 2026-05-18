TRADITIONS = {
    "kenya": [
        {
            "title": "Maasai Jumping Dance",
            "type": "Traditional Practice",
            "description": "A ceremonial dance performed by Maasai warriors where participants jump high into the air to demonstrate strength and endurance."
        },
        {
            "title": "Story of Luanda Magere",
            "type": "Folktale",
            "description": "A legendary Luo warrior believed to have possessed a body made of stone and supernatural strength."
        },
        {
            "title": "Naming Ceremonies",
            "type": "Tradition",
            "description": "Many Kenyan communities celebrate childbirth through blessings, songs, and naming rituals."
        }
    ],

    "japan": [
        {
            "title": "Hanami",
            "type": "Festival Tradition",
            "description": "The tradition of viewing cherry blossoms during spring with family and friends."
        },
        {
            "title": "Tanabata",
            "type": "Folklore Festival",
            "description": "A festival based on the legend of two celestial lovers separated by the Milky Way."
        }
    ]
}


def get_heritage_by_country(country_name):
    return TRADITIONS.get(country_name.lower(), [])