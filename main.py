from drafter import *
from drafter.llm import *
from dataclasses import dataclass

set_gemini_server("https://drafter-gemini-proxy.devikar.workers.dev")


@dataclass
class Trip:
    time_of_year: list[str]
    location: str
    description: str
 
Trips = [
    Trip(
        ["January", "February", "March", "April"],
        "Tortuguero National Park, Costa Rica",
        "Experience responsible wildlife viewing in the wet, humid lowlands. Eco-lodges focus on zero-carbon footprints, supporting local communities, and turtle conservation programs. Nesting sea turtles can be seen Mar-Oct for varying species, " \
        "but the months provided offer the best overall experience."
    ),
    Trip(
        ["May", "June", "September", "October"],
        "Galapagos Islands, Ecuador",
        "Visit under strictly regulated tourism guidelines. Small-ship cruises ensure minimal environmental impact. Tour operators contribute directly to park conservation and local science initiatives, allowing up-close wildlife encounters."
    ),
    Trip(
        ["July", "August"],
        "Banff National Park, Canada",
        "Explore the Canadian Rockies with a focus on sustainable transport (shuttles) to minimize traffic and emissions. Numerous certified 'green' hotels and emphasis on Leave No Trace principles in backcountry hiking."
    ),
    Trip(
        ["March", "April", "November", "December"],
        "Patagonia (Torres del Paine), Chile",
        "Hike and camp with regulated park access that limits capacity to protect fragile ecosystems. Eco-camps and refugios utilize renewable energy and strict waste management protocols. Best during shoulder seasons for fewer crowds."
    ),
    Trip(
        ["September", "October", "November"],
        "Amazon Rainforest (Iquitos Region), Peru",
        "Stay in remote eco-lodges that are owned and operated by indigenous communities. Tourism income directly funds health, education, and anti-logging efforts, supporting sustainable use of the forest."
    ),
    Trip(
        ["June", "July", "August"],
        "Acadia National Park, Maine, USA",
        "Utilize the efficient Island Explorer bus system, running on propane, to reduce vehicle traffic. Stay at locally owned inns that prioritize energy efficiency and locally sourced food, supporting small coastal towns."
    ),
    Trip(
        ["December", "January", "February"],
        "Tikal National Park, Guatemala",
        "Explore Mayan ruins surrounded by rainforest, staying in eco-friendly accommodations outside the park. Tourism revenue helps fund archaeological preservation and biodiversity protection, blending culture and conservation."
    ),
    Trip(
        ["April", "May", "June"],
        "Osa Peninsula, Costa Rica",
        "Visit one of the world's most biodiverse regions. Eco-lodges are deeply involved in reforestation and community employment, offering low-impact activities like canopy tours and birdwatching."
    ),
    Trip(
        ["October", "November", "March", "April"],
        "Valdés Peninsula, Argentina",
        "Observe marine wildlife (whales, penguins) from regulated distance and with expert guides. Strict conservation rules limit access, ensuring minimal disturbance to critical breeding grounds. Shoulder seasons offer great viewing opportunities."
    ),
    Trip(
        ["July", "August"],
        "Haida Gwaii, British Columbia, Canada",
        "Engage in community-based tourism guided by the Haida Nation. Tours are centered on cultural preservation, traditional land stewardship, and education on respectful interaction with the ancient rainforest and coast."
    ),
    Trip(
        ["June", "July", "August"],
        "Yellowstone National Park, Wyoming, USA",
        "Focus on interpretive tours led by naturalists. The park prioritizes wildlife protection through mandatory viewing distances and educational signage, promoting stewardship of geothermal features and megafauna."
    ),
    Trip(
        ["December", "January", "February"],
        "Cabo Polonio, Uruguay",
        "Visit a remote coastal town with no paved roads and no connection to the national electricity grid. Stay in simple, solar-powered accommodations, supporting local fishers and a low-impact lifestyle near a sea lion colony."
    ),
    Trip(
        ["May", "June"],
        "Cloud Forest (Mindo), Ecuador",
        "Participate in sustainable birdwatching and chocolate production tours. Local businesses emphasize fair trade and conservation of the unique cloud forest habitat, a hotspot for endemic species."
    ),
    Trip(
        ["September", "October"],
        "Copper Canyon (Barrancas del Cobre), Mexico",
        "Travel via the historic railway, reducing carbon output compared to flying. Engage in tourism guided by the indigenous Raramuri people, ensuring cultural sensitivity and direct economic benefit to the community."
    ),
    Trip(
        ["March", "April"],
        "Sian Ka'an Biosphere Reserve, Quintana Roo, Mexico",
        "Explore protected mangrove ecosystems and ruins with certified guides. Limited access and strict regulations protect the Mesoamerican Barrier Reef system and coastal wetlands from mass tourism."
    ),
    Trip(
        ["November", "December"],
        "Fernando de Noronha, Brazil",
        "Access is highly restricted and subject to conservation fees that fund the park. The island prioritizes responsible diving, snorkeling, and turtle protection, maintaining a pristine marine environment."
    ),
    Trip(
        ["May", "June", "September", "October"],
        "Bay Islands (Utila), Honduras",
        "A destination for ethical scuba diving and marine conservation. Dive shops actively participate in coral reef monitoring and whale shark research, focusing on education and low-impact water activities."
    ),
    Trip(
        ["June", "July", "August"],
        "Denali National Park, Alaska, USA",
        "Vehicle access is almost entirely restricted; visitors must use park buses. This rigorous restriction minimizes human impact on the vast wilderness and protects wildlife like caribou and grizzlies."
    ),
    Trip(
        ["March", "April", "October", "November"],
        "Tayrona National Natural Park, Colombia",
        "Hike and stay in small eco-huts managed under park regulations. Tourism capacity is limited, and the park periodically closes for environmental recovery, respecting the land's spiritual importance to indigenous groups."
    ),
    Trip(
        ["July", "August"],
        "Iguazú National Park, Argentina/Brazil",
        "Visit the stunning waterfalls using designated walkways and electric vehicles. The parks on both sides strictly manage visitor flow and infrastructure to protect the surrounding Atlantic Forest biodiversity."
    ),
    Trip(
        ["December", "January", "February"],
        "Belize Barrier Reef, Belize",
        "Stay at small, self-sufficient eco-resorts on the Cayes. Dive and snorkel with licensed guides who enforce marine protected area rules, contributing to the preservation of the world's second-largest barrier reef."
    ),
    Trip(
        ["September", "October"],
        "Atacama Desert, Chile",
        "Experience astrotourism with observatories focused on minimal light pollution and environmental impact. Tours often partner with local communities to manage water usage and cultural site preservation."
    ),
    Trip(
        ["May", "June"],
        "Big Bend National Park, Texas, USA",
        "A dark sky sanctuary focused on primitive camping and respectful backcountry access. Its remote location and low visitor density ensure a low environmental footprint and support regional conservation efforts."
    ),
    Trip(
        ["March", "April"],
        "Sierra Gorda Biosphere Reserve, Querétaro, Mexico",
        "Engage in community-based conservation tourism, staying in rustic cabins. Funds support local land stewardship, monitoring of endangered species (like the military macaw), and sustainable agriculture."
    ),
    Trip(
        ["November", "December"],
        "The Pantanal, Brazil",
        "The world's largest tropical wetland, best visited during the dry season. Stays are primarily at ecologically focused *fazendas* (ranches) that balance cattle ranching with wildlife preservation and low-density photographic safaris."
    )
]

@dataclass
class State:
    continent: str
    region: str
    month: str
    best_trip: Trip
    conversation: list[LLMMessage]
    



continents = ["North America", "South America"]    
@route
def index(state: State) -> Page:
    state.region = ""
    return Page(state, content = [
        bold("Welcome to EcoTrip Americas!"),
        Image("https://curiositysavestravel.com/wp-content/uploads/2021/01/Sustainable-Ecotourism-benefits.png", 900,300),
        "Select your home continent below:",
        SelectBox(name = "continent",
                  options = continents,
                  default = None
                  ),
        "Here is your current proposed trip!",
        "Location:",
        str(state.best_trip.location),
        "Description:",
        str(state.best_trip.description),
        Button("Next", "find_country")
        ])

@route
def find_country(state: State, continent: str) -> Page:
    north_american_countries = ["United States", "Canada", "Mexico"]
    south_american_countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
                                "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
    state.continent = continent
    if continent == "North America":
        return Page(state, content = [
            "Choose your country here:",
            SelectBox(name = "NA_country",
                      options = north_american_countries,
                      default = None
                      ),
            Button("Next", "break_NA_country")
            ])
    elif continent == "South America":
        return Page(state, content = [
            "Choose your country here:",
            SelectBox(name = "SA_country",
                      options = south_american_countries,
                      default = None
                      ),
            Button("Next", break_SA_country)
            ])

@route
def break_NA_country(state: State, NA_country: str) -> Page:
        if NA_country == "United States":
            return Page(state, content = [
                "Enter your state here:",
                TextBox(name = "NA_region", default = ""),
                Button("Next", "find_month_US"),
                ])
        elif NA_country == "Canada":
            return Page(state, content = [
                "Enter your Province here:",
                TextBox(name = "Canada_region", default = ""),
                Button("Next", "find_month_CA"),
                ])
        else:
            state.region = "Mexico"
            return find_month(state)

@route
def break_SA_country(state: State, SA_country: str) -> Page:
    brazil_regions = ["North", "Northeast", "Center-west", "Southeast", "South"]
    if SA_country == "Brazil":
        return Page(state, content = [
            Image("https://cdn.mappr.co/wp-content/uploads/2022/08/brazil-regions-map.png", 400,300),
            "Choose the region of Brazil which you are from:",
            SelectBox(name = "brazil_region",
                      options = brazil_regions,
                      default = None
                      ),
            Button("Next", "find_month_B")
            ])
    elif SA_country == "Argentina":
        return Page(state, content = [
            "Choose the region of Argentina which you are from:",
            SelectBox(name = "argentina_region",
                      options = ["Northern Argentina", "Southern Argentina"],
                      default = None
                      ),
            Button("Next", "find_month_A")
            ])
    else:
        state.region = SA_country
        return find_month(state) 
 
@route
def find_month_US(state: State, NA_region: str) -> Page:
    state.region = NA_region
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return Page(state, content = [
        "Choose the month in which you wish to travel:",
        SelectBox(name = "month",
                  options = months,
                  default = None
                  ),
        Button("Next", "store_month_US")
        ])

@route
def find_month_CA(state: State, Canada_region: str) -> Page:
    state.region = Canada_region
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return Page(state, content = [
        "Choose the month in which you wish to travel:",
        SelectBox(name = "month",
                  options = months,
                  default = None
                  ),
        Button("Next", "store_month_CA")
        ])

@route
def find_month_B(state: State, brazil_region: str) -> Page:
    state.region = brazil_region
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return Page(state, content = [
        "Choose the month in which you wish to travel:",
        SelectBox(name = "month",
                  options = months,
                  default = None
                  ),
        Button("Next", "store_month_B")
        ])

@route
def find_month_A(state: State, argentina_region: str) -> Page:
    state.region = argentina_region
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return Page(state, content = [
        "Choose the month in which you wish to travel:",
        SelectBox(name = "month",
                  options = months,
                  default = None
                  ),
        Button("Next", "store_month_A")
        ])

@route
def find_month(state: State) -> Page:
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return Page(state, content = [
        "Choose the month in which you wish to travel:",
        SelectBox(name = "month",
                  options = months,
                  default = None
                  ),
        Button("Next", "store_month")
        ])

@route
def store_month_US(state: State, month: str) -> Page:
    state.month = month
    return pick_best_trip(state, state.month)

@route
def store_month_CA(state: State, month: str) -> Page:
    state.month = month
    return pick_best_trip(state, state.month)

@route
def store_month_B(state: State, month: str) -> Page:
    state.month = month
    return pick_best_trip(state, state.month)

@route
def store_month_A(state: State, month: str) -> Page:
    state.month = month
    return pick_best_trip(state, state.month)

@route
def store_month(state: State, month: str) -> Page:
    state.month = month
    return pick_best_trip(state, state.month)


conversation = []

conversation.append(LLMMessage("user", "Hello, Gemini!"))
'''
@route
def index(state: State) -> Page:
    """
    Main page of the chatbot application.
    Shows API key setup if not configured, otherwise shows the chat interface.
    """
    return show_chat(state)
'''

def show_chat(state: State) -> Page:
    """Display the chat interface with conversation history."""
    content = [
        f"Chatbot using Gemini",
        "---"
    ]

    # Show conversation history
    if state.conversation:
        for msg in state.conversation:
            if msg.role == "user":
                content.append(f"You: {msg.content}")
            elif msg.role == "assistant":
                content.append(f"Bot: {msg.content}")
        content.append("---")

    # Input for new message
    content.extend([
        "Your message:",
        TextArea("user_message", "", rows=3, cols=50),
        LineBreak(),
        Button("Send", send_message),
        Button("Clear Conversation", clear_conversation),
    ])

    return Page(state, content)


@route
def send_message(state: State, user_message: str) -> Page:
    """Send a message to the LLM and get a response."""
    if not user_message.strip():
        return show_chat(state)

    # Add user message to conversation
    user_msg = LLMMessage("user", user_message)
    state.conversation.append(user_msg)

    result = call_gemini(state.conversation)

    # Handle the result
    if isinstance(result, LLMResponse):
        # Success! Add the response to conversation
        assistant_msg = LLMMessage("assistant", result.content)
        state.conversation.append(assistant_msg)
    else:
        # Error occurred
        error_msg = LLMMessage("assistant", f"Error: {result.message}")
        state.conversation.append(error_msg)
    return show_chat(state)


@route
def clear_conversation(state: State) -> Page:
    """Clear the conversation history."""
    state.conversation = []
    return show_chat(state)


@route
def pick_best_trip(state: State, month: str) -> Page:
    """Use Gemini to find the best matching trip based on user location and month."""
    state.month = month
    
    # Find trips available in the selected month
    available_trips = [trip for trip in Trips if month in trip.time_of_year]

    if not available_trips:
        return Page(state, content = [
            "Sorry, no trips available in " + month + ".",
            Button("Go Back", "find_month")
        ])
    
    # If only one trip available, use it
    if len(available_trips) == 1:
        state.best_trip = available_trips[0]
        return show_best_trip(state)
    
    # Use Gemini to find the closest trip to the user's location
    prompt = f"""The user is from {state.region}. They want to travel in {month}. Here are the available trip options:"""
    
    for i, trip in enumerate(available_trips):
        prompt += f"\n{i+1}. {trip.location}: {trip.description}"


    prompt += f"\n\nWhich of these trips would be closest to or most appealing from {state.region}? Answer with just the location name (e.g., 'California' or 'Costa Rica')."
    
    conversation = [LLMMessage("user", prompt)]
    result = call_gemini(conversation)

    if isinstance(result, LLMResponse):
        # Extract the best trip from Gemini's response
        response_text = result.content.lower()
        best_trip = None
        
        for trip in available_trips:
            if trip.location.lower() in response_text:
                best_trip = trip
                break
        
        # Fallback to first trip if Gemini's response doesn't match
        if not best_trip:
            best_trip = available_trips[0]
        
        state.best_trip = best_trip
        return show_best_trip(state)
    else:
        # Fallback to first available trip if Gemini fails
        state.best_trip = available_trips[0]
        return show_best_trip(state)

@route
def show_best_trip(state: State) -> Page:
    """Display the recommended trip."""
    if state.best_trip is None:
        return Page(state, content = [
            "No trip selected.",
            Button("Start Over", "index")
        ])
    trip = state.best_trip
    return Page(state, content = [
        "Your Recommended Trip!",
        "---",
        "Location: " + trip.location,
        "Best months: " + ", ".join(trip.time_of_year),
        "---",
        trip.description,
        "---",
        Button("Start Over", "index")
    ])


start_server(State("", "", "", Trip([], "", ""), []))
   
