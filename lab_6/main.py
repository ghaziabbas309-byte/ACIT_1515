from spotify import songs, add_song, record_listen, generate_wrapped

def main():
    while True:
        print("\n====== SPOTIFY WRAPPED ======")
        print("1. Add a song")
        print("2. Record a listen")
        print("3. Generate Spotify Wrapped")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_song(songs)
        elif choice == "2":
            record_listen(songs)
        elif choice == "3":
            generate_wrapped(songs)
        elif choice == "4":
            print("\nThanks for using Spotify Wrapped! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()