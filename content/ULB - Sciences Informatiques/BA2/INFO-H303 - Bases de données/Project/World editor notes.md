---
title: World editor notes
authors: Alessandro Dorigo
tags:
  - Databases
---


- Zones editor needs to have all data about zones and connectivity
	- Connectivity represented not necessarily via coordinates but a certain direction or potentially a travel method
	- So you'd travel outside the zone once you reach the border, which would be a place that is used as a connector
		- Other types of connector places can be forests, paths, etc

- Place editor needs to be properly done so that when a place is in a zone, it can see all other places and connect to them if needed
	- Locations are used here to specify coordinates for the game engine

- Entity editor to regroup all entities
	- NPCs are made with empty equipment slots, which have to be filled up with items
	- HP/MP etc
	- Monsters too
	- Characters too but we add the other stuff tied to them
		- Ability view
		- Inventory view
		- Attribute view (see all attributes and add their values, base ones)
