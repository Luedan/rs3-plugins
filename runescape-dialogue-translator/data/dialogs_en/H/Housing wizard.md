# Housing wizard

- **Original Wiki Page**: [Transcript:Housing wizard](https://runescape.wiki/w/Transcript%3AHousing%20wizard)
- **Letter**: `H`

---

## Dialogue Transcript


### Talk to


#### Before completing There's No Place Like Home...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px You need to complete the Construction tutorial before you can use this.
  - Speak to Alfred Stonemason, northwest of Rimmington, to learn more.
    - [Choice]: OK
      - ((The interface closes and dialogue continues below.))

#### After completing There's No Place Like Home...

- [Menu]: What would you like to do?
  - [Choice]: Move my plot.
    - **Housing wizard:** I'll teleport you to the homestead and from there you'll have the pick of the lot.
    - {{Qact|Screen fades to black. The player is now inside the homestead next to the homestead portal.}}
    - **Housing wizard:** Have a look around at your options. When you're ready, just touch the plot's numbered sign near  entrance.
  - [Choice]: Start a homestead.
    - [Menu]: Homestead setup
      - [Choice]: What is a homestead?
        - **Housing wizard:** A homestead is a shared space where you and up to four others can build together and explore each other's plots.
        - **Housing wizard:** If you choose to leave a homestead in the future, you will never lose any progress on your personal plot.
        - (initial)
      - [Choice]: Create homestead.
        - **Housing wizard:** Great! Invite some players to your group, then come see me again and we can get your homestead finalised!
        - [Right-click on nearby players to invite them to your homestead.]
      - [Choice]: Nothing for now.
        - (end)

#### The creator creating a homestead

- [Menu]: What would you like to do?
  - [Choice]: Set homestead name.
    - [Menu]: Enter your desired homestead name:
      - [0/20<br>[input field]<br>Names may only contain A-Z, a-z, 0-9 and space. No special characters e.g. å, ä]
        - [Menu]: Please confirm your chosen homestead name:
          - [Choice]: [name]
            - Checking if homestead name is available.
            - {{Pop-up|Checking if homestead name is available.|colour=#00FF00}}
            - [Menu]: Create homestead?
              - [Choice]: Create homestead: '[name]'.
                - Your homestead is now being created, this may take a few moments.
                - Player has joined your homestead.
                - Your homestead '[name]' has been created successfully.
                - {{Pop-up|Your homestead '[name]' has been created successfully.|colour=#00FF00}}
              - [Choice]: Cancel.
                - (end)
          - [Choice]: Choose a different name.
            - (previous)
  - [Choice]: Finalise homestead.
    - (above|enter-name)
  - [Choice]: Abort homestead creation.
    - [Menu]: Are you sure you want to abandon the homestead creation process?
      - [Choice]: Yes.
        - You have left the homestead creation process.
        - {{Pop-up|You have left the homestead creation process.|warning=yes}}
      - [Choice]: No.
        - (end)
  - [Choice]: Nothing for now.
    - (end)

#### Founding members creating a homestead

- **Housing wizard:** Your homestead is still being formed... What would you like to do?
- [Menu]: What would you like to do?
  - [Choice]: Leave homestead creation.
    - [Menu]: Are you sure you want to leave this group?
      - [Choice]: Yes.
        - You have left the homestead creation process.
        - {{Pop-up|You have left the homestead creation process.|warning=yes}}
      - [Choice]: No.
        - (end)
  - [Choice]: Nothing for now.
    - (end)

#### Created a homestead

- **Housing wizard:** Excellent! I see you're all setup in a homestead.
- (Condition: Swapping is in progress:)
  - **Housing wizard:** You're in the process of swapping a plot. Do you want to continue?
  - [Menu]: Stop plot swapping.
    - [Choice]: Cancel plot swapping.
      - **Housing wizard:** Sorted. If you want to start swapping plots with anyone in your homestead, just chat to me again.
      - (continue)
    - [Choice]: Continue plot swapping.
      - (end)
- [Menu]: What can I help you with?
  - [Choice]: Swap homestead plot.
    - Right-click on nearby players to propose swapping plots with them.
    - Inviting Player to swap plots.
    - {{Pop-up|Inviting Player to swap plots.|colour=#00ff00}}
    - (Condition: Player accepted swapping:)
      - You have successfully swapped plots with Player. Your plot will move the next time your homestead is generated.
      - {{Pop-up|You have successfully swapped plots with Player. Your plot will move the next time your homestead is generated.}}
    - (Condition: Player declined swapping:)
      - Player has declined your invitation.
      - {{Pop-up|Player has declined your invitation.|warning=yes}}
  - [Choice]: Leave homestead.
    - [Warning:]<br>You may not be able to rejoin this homestead if you leave.}}
    - [Menu]: Are you sure you want to leave?
      - [Choice]: Leave.
        - Your request to leave your homestead is now in progress.
        - You have left your homestead.
        - {{Pop-up|You have left your homestead.|colour=#00ff00}}
      - [Choice]: Stay.
        - (end)
  - [Choice]: Invite a player.
  - [Choice]: Homestead administration.
    - [Menu]: What homestead changes would you like to make?
      - [Choice]: Kick a member.
        - (Condition: If there is only one member:)
          - [can not] kick yourself.}}
          - [Choice]: Player 1
            - Player 1 has been removed from your homestead.
          - [Choice]: Player 2
            - (above)
          - [Choice]: Player 3
            - (above)
          - [Choice]: Player 4
            - (above)
          - [Choice]: Nobody
      - [Choice]: Change owner.
        - (Condition: If there is only one member:)
          - [can not] assign another owner.}}
        - [Menu]: Who would you like to assign as the new owner?
          - [Choice]: Player 1
            - You have successfully changed owner to Player 1
            - {{Pop-up|You have successfully changed owner to Player 1}}
          - [Choice]: Player 2
            - (above)
          - [Choice]: Player 3
            - (above)
          - [Choice]: Player 4
            - (above)
          - [Choice]: Nobody
            - (end)
      - [Choice]: Previous options.
        - (previous)
      - [Choice]: Nothing for now.
        - (end)
  - [Choice]: Nothing for now.
    - (end)

### Inviting player to join a homestead

- Inviting Player to join your homestead.
- {{Pop-up|Inviting Player to join your homestead.|colour=#00FF00}}
- (Condition: Player accepted the invitation:)
  - Player has accepted your invitation.
  - {{Pop-up|Player has accepted your invitation.|colour=#00FF00}}
- (Condition: Player declined the invitation:)
  - Player has declined your invitation.
  - {{Pop-up|Player has declined your invitation.|warning=yes}}

#### Being invited to join a homestead

- [Player] is inviting you to become a founding member of their homestead.}}}}
  - [Choice]: Accept
    - You have joined the creation a homestead!
    - {{Pop-up|Player has declined your invitation.|colour=#00FF00}}
  - [Choice]: Decline
    - (end)

### Being invited to swap plot

- [swap plots].}}}}
  - [Choice]: Accept
    - You have successfully swapped plots with Player. Your plot will move the next time your homestead is generated.
    - {{Pop-up|You have successfully swapped plots with Player. Your plot will move the next time your homestead is generated.}}
  - [Choice]: Decline
    - (end)

### Aborted the creation of a homestead

- The homestead creation has ended because the creator has left the group.
- {{Pop-up|The homestead creation has ended because the creator has left the group.|warning=yes}}

### When the owner finalising the creation

- You need between 2-5 players to create a homestead.
- You have joined the homestead: '[name]'.
- Your homestead '[name]' has been created successfully.
- {{Pop-up|Your homestead '[name]' has been created successfully.|colour=#00FF00}}

### Entering house portal when swapping is in progress

- You should finish swapping your homestead plot before trying to access a player-owned house!

### Being kicked from a homestead

- Player has been removed your from the homestead.
