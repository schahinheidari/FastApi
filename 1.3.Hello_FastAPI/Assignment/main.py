from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return "Hi! Welcome to my API." + "\n" + "The Solar System API provides information for thousands of all solar system planets and their moons."

list_planets = [
    {"name": "Mercury"},
    {"name": "Venus"},
    {"name": "Earth"},
    {"name": "Mars"},
    {"name": "Jupiter"},
    {"name": "Saturn"},
    {"name": "Uranus"},
    {"name": "Neptune"},
]

@app.get("/list_planets")
def get_planets():
    return {"planets": list_planets}

@app.get("/planets/{planet_name}")
def planets(planet_name):
    planets = [
	{"position": "1",
	 "name": "Mercury",
	 "image": "http://space-facts.com/wp-content/uploads/mercury-transparent.png",
	 "velocity": "47",
	 "distance": "58",
	 "description": "Mercury is the closest planet to the Sun and due to its proximity it is not easily seen except during twilight. For every two orbits of the Sun, Mercury completes three rotations about its axis and up until 1965 it was thought that the same side of Mercury constantly faced the Sun. Thirteen times a century Mercury can be observed from the Earth passing across the face of the Sun in an event called a transit, the next will occur on the 9th May 2016."
	},
	{"position": "2",
	 "name": "Venus",
	 "image": "http://space-facts.com/wp-content/uploads/venus-transparent.png",
	 "velocity": "35",
	 "distance": "108",
	 "description": "Venus is the second planet from the Sun and is the second brightest object in the night sky after the Moon. Named after the Roman goddess of love and beauty, Venus is the second largest terrestrial planet and is sometimes referred to as the Earth’s sister planet due the their similar size and mass. The surface of the planet is obscured by an opaque layer of clouds made up of sulphuric acid."
	},
	{"position": "3",
	 "name": "Earth",
	 "image": "http://space-facts.com/wp-content/uploads/earth-transparent.png",
	 "velocity": "29",
	 "distance": "149",
	 "description": "Earth is the third planet from the Sun and is the largest of the terrestrial planets. The Earth is the only planet in our solar system not to be named after a Greek or Roman deity. The Earth was formed approximately 4.54 billion years ago and is the only known planet to support life."
	},
	{"position": "4",
	 "name": "Mars",
	 "image": "http://space-facts.com/wp-content/uploads/mars-transparent.png",
	 "velocity": "24",
	 "distance": "227",
	 "description": "Mars is the fourth planet from the Sun and is the second smallest planet in the solar system. Named after the Roman god of war, Mars is also often described as the “Red Planet” due to its reddish appearance. Mars is a terrestrial planet with a thin atmosphere composed primarily of carbon dioxide."
	},
	{"position": "5",
     "name": "Jupiter",
	 "image": "http://space-facts.com/wp-content/uploads/jupiter-transparent.png",
	 "velocity": "13",
	 "distance": "778",
	 "description": "The planet Jupiter is the fifth planet out from the Sun, and is two and a half times more massive than all the other planets in the solar system combined. It is made primarily of gases and is therefore known as a “gas giant”."
	},
	{"position": "6",
	 "name": "Saturn",
	 "image": "http://space-facts.com/wp-content/uploads/saturn-transparent.png",
	 "velocity": "9",
	 "distance": "1426",
	 "description": "Saturn is the sixth planet from the Sun and the most distant that can be seen with the naked eye. Saturn is the second largest planet and is best known for its fabulous ring system that was first observed in 1610 by the astronomer Galileo Galilei. Like Jupiter, Saturn is a gas giant and is composed of similar gasses including hydrogen, helium and methane."
	},
	{"position": "7",
	 "name": "Uranus",
	 "image": "http://space-facts.com/wp-content/uploads/uranus-transparent.png",
	 "velocity": "6",
	 "distance": "2870",
	 "description": "Uranus is the seventh planet from the Sun. While being visible to the naked eye, it was not recognised as a planet due to its dimness and slow orbit. Uranus became the first planet discovered with the use of a telescope. Uranus is tipped over on its side with an axial tilt of 98 degrees. It is often described as “rolling around the Sun on its side.”"
	},
	{"position": "8",
	 "name": "Neptune",
	 "image": "http://space-facts.com/wp-content/uploads/neptune-transparent.png",
	 "velocity": "5",
	 "distance": "4498",
	 "description": "Neptune is the eighth planet from the Sun making it the most distant in the solar system. This gas giant planet may have formed much closer to the Sun in early solar system history before migrating to its present position."
	},
	{"position": "9",
	 "name": "Sun",
	 "image": "http://pngimg.com/uploads/sun/sun_PNG13424.png",
	 "velocity": "220",
	 "distance": "0",
	 "description": "The Sun (or Sol), is the star at the centre of our solar system and is responsible for the Earth’s climate and weather. The Sun is an almost perfect sphere with a difference of just 10km in diameter between the poles and the equator. The average radius of the Sun is 695,508 km (109.2 x that of the Earth) of which 20–25% is the core."
	}
]
    for planet in planets:
        if planet["name"] == planet_name:
            return planet
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                              detail="Planet not found!")

planets_data = [
    {"name": "Mercury", "image": "http://space-facts.com/wp-content/uploads/mercury-transparent.png"},
    {"name": "Venus", "image": "http://space-facts.com/wp-content/uploads/venus-transparent.png"},
    {"name": "Earth", "image": "http://space-facts.com/wp-content/uploads/earth-transparent.png"},
    {"name": "Mars", "image": "http://space-facts.com/wp-content/uploads/mars-transparent.png"},
    {"name": "Jupiter", "image": "http://space-facts.com/wp-content/uploads/jupiter-transparent.png"},
    {"name": "Saturn", "image": "http://space-facts.com/wp-content/uploads/saturn-transparent.png"},
    {"name": "Uranus", "image": "http://space-facts.com/wp-content/uploads/uranus-transparent.png"},
    {"name": "Neptune", "image": "http://space-facts.com/wp-content/uploads/neptune-transparent.png"},
    {"name": "Sun", "image": "http://pngimg.com/uploads/sun/sun_PNG13424.png"},
]

@app.get("/planets/{planet_name}/image")
def get_planet_image(planet_name: str):
    """Find planet in list and return image URL."""
    for planet in planets_data:
        if planet["name"].lower() == planet_name.lower():
            return RedirectResponse(url=planet["image"])
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                              detail="Planet not found!")
    return {"error": "Planet not found"}
