---
title: Main notes
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ This document explains the relationships between key entities in our game database design
## Player
> [!info]+ Core User Entity
> - Represents a real-world user of the game
> - Has `user_id` (UUID) as primary key
> - Stores `username`, `email`, `password`
> - Player-specific progression: `level`, `xp`, `player_currency`
> - One `Player` can own many `Characters`

> [!important] Relationship
> - One-to-many relationship with `Character`
> - Foreign key goes in the `Character` table (not in `Player`)
## Entity
> [!info]+ Base Game Object
> - Represents any spawnable object in the game
> - Has `entity_id` as primary key
> - Has `entity_type` to distinguish between `Characters`, `NPCs`, `Monsters`
> - The parent table for all interactive game objects
> - Contains common properties shared across all entity types
## Character
> [!info]+ Player-Controlled Entity
> - A specific type of `Entity` with additional attributes
> - Has `char_id` as primary key
> - Connected to `Player` via `user_id` (FK)
> - Connected to `CharacterClass` via `class_id` (FK)
> - Connected to `Stats` via `stats_id` (FK)
> - Connected to `EntityAttribute` via `entity_attribute_id` (FK)

> [!important] Benefit
> - `CharacterClass` system allows adding new classes without redesigning database

```sql
SELECT * FROM Characters WHERE player_id = 'logged_in_player_id'
```
## Stats (Core Stats)
> [!info]+ Fundamental Gameplay Metrics
> - These are the concrete, measurable properties
> - Examples: `vitality`, `attunement`, `endurance`, `strength`, `dexterity`, `resistance`, `intelligence`, `faith`
> 	- These would be defined by default, or could be edited to remove or add new ones.
> - Each `Entity` has exactly one row in this table
> - Primary key is `stats_id`
> - Foreign key relation: `entity_id` references Entity table
## AttributeDefinitions Table
> [!info]+ Base Character Qualities
> - Primary key: `attribute_id`
> - Defines all possible attributes in the game
> - Examples: `hp`, `mp`, `stamina`, `equip_load`, `right_hand_1_dmg`, `right_hand_2_dmg`, `left_hand_1_dmg`, `left_hand_2_dmg`, `phys_def`, `strike_def`, `slash_def`, `thrust_def`, `magic_def`, `fire_def`, `lightning_def`, `poise`, `bleed_res`, `poison_res`, `curse_res`, `item_discovery`
> - Contains: `name`, `description`, `attribute_type`

> [!warning]+ Important Distinction
> - This table defines WHAT attributes exist
> - It doesn't store HOW MUCH of each attribute entities have
## EntityAttributes Table
> [!info]+ Junction Table
> - Links entities to specific attribute values
> - Contains: `entity_id`, `attribute_id`, `base_value`
> - Composite key: (`entity_id`, `attribute_id`)
> - Shows which entities have which attributes and their base values
## ModifierSources Table
> [!info]+ Source of Modifications
> - Primary key: `source_id`
> - Tracks where modifiers come from (items, buffs, etc.)
> - Contains: `source_type`, `reference_id`, `duration`
> - Example: Item #123 is a modifier source
## AttributeModifiers Table
> [!info]+ Actual Modifiers
> - Primary key: `modifier_id`
> - Contains: `source_id`, `entity_id`, `attribute_id`, `modifier_type`, `value`
> - Tracks which modifiers affect which attributes on which entities
> - Example: +5 STR buff from Ring of Might on Character #456

> [!success]+ Calculation Flow
> 1. Get base attribute values from `EntityAttributes`
> 2. Apply all relevant modifiers from `AttributeModifiers`
> 3. Calculate derived `Stats` based on modified attribute values
> 4. Use final `Stats` values for gameplay mechanics
## Key Concepts
### Core Stats
> [!info]+ Game Mechanics Properties
> - **What they are**: Concrete gameplay values used directly in mechanics
> - **Examples**: HP, MP, damage, defense ratings
> - **Characteristics**:
>     - Have current and maximum values
>     - Used directly in combat and skill calculations
>     - Derived from attributes and modified by equipment
### Attributes
> [!info]+ Character Potential
> - **What they are**: Fundamental character qualities
> - **Examples**: Strength, Dexterity, Intelligence, Faith
> - **Characteristics**:
>     - More basic than stats
>     - Level up through character progression
>     - Influence multiple stats (STR affects damage AND equip load)
### Modifiers
> [!info]+ Temporary or Permanent Adjustments
> - **What they are**: Changes to attributes or stats from external sources
> - **Examples**: +2 STR from armor, +10% fire resistance from potion
> - **Characteristics**:
>     - Come from equipment, buffs, debuffs
>     - Can be flat (+5) or percentage (+10%)
>     - May have duration or conditions
>     - Applied after base values are established

> [!tip]+ Database Implementation
> This system allows for high flexibility while maintaining data integrity:
> - Add new attributes without changing structure
> - Add new modifiers without changing structure
> - Add new stats without affecting existing calculations
