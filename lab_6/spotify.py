songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]

def add_song(songs_list):
    title = input("Enter song title: ").strip()
    artist = input("Enter artist: ").strip()
    
    try:
        minutes = int(input("Enter duration (minutes): "))
        seconds = int(input("Enter duration (seconds): "))
    except ValueError:
        print("Invalid input for duration. Please enter whole numbers.")
        return

    total_seconds = (minutes * 60) + seconds
    
    new_song = {
        "title": title,
        "artist": artist,
        "duration": total_seconds,
        "plays": 0
    }
    
    songs_list.append(new_song)
    print(f"\nSuccess! '{title}' by {artist} has been added.")

def record_listen(songs_list):
    if not songs_list:
        print("\nYour song library is currently empty.")
        return

    target = input("Enter song title: ").strip().lower()
    found = False
    
    for song in songs_list:
        if song["title"].lower() == target:
            song["plays"] += 1
            found = True
            print(f"Recorded a listen for '{song['title']}'! Current plays: {song['plays']}")
            break
            
    if not found:
        print(f"Error: Song '{target.title()}' not found in the library.")

def generate_wrapped(songs_list):
    if not songs_list:
        print("\nYour library is empty. Add some songs before generating Wrapped!")
        return

    total_songs = len(songs_list)
    total_plays = sum(song["plays"] for song in songs_list)
    
    total_seconds = sum(song["duration"] * song["plays"] for song in songs_list)
    total_minutes = total_seconds // 60

    most_played = max(songs_list, key=lambda s: s["plays"])

    print("\n========== YOUR SPOTIFY WRAPPED ==========")
    print(f"\nTotal Songs: {total_songs}")
    print(f"Total Plays: {total_plays}")
    print(f"Total Listening Time: {total_minutes} minutes")
    print(f"\nYour Most Played Song:")
    print(f"{most_played['title']} - {most_played['artist']} ({most_played['plays']} plays)")
    print("\n==========================================")