---
title: Prototype
authors: Alessandro Dorigo
tags:
  -
---

## Model Classes
These classes manage game data and rules, ensuring that only valid moves affect the game state.

### `GameBoard`
- **Purpose**: Represents the 10x20 grid and handles line completion.
- **Attributes**:
  - `grid: std::vector<std::vector<int>>`
- **Methods**:
  - `std::vector<int> clear_lines()`: Checks for and clears completed lines, returning the count of cleared lines.
  - `void add_penalty_line(const std::vector<int>& line)`: Adds a penalty line to the bottom. *(phase 2)*
  - `bool is_game_over() const`: Checks if any blocks reach the top of the grid.

### `Tetromino`
- **Purpose**: Represents an active tetromino.
- **Attributes**:
  - `shape: std::vector<std::vector<int>>`
  - `position: std::pair<int, int>`
- **Methods**:
  - `std::vector<std::vector<int>> rotate() const`: Returns the rotated shape without modifying the position.
  - `std::pair<int, int> move(const std::string& direction) const`: Calculates a new position based on the direction ("left", "right", "down").

### `GameLogic`
- **Purpose**: Checks the legality of moves and interacts with `GameBoard` for updates.
- **Attributes**:
  - `board: GameBoard&`
  - `active_tetromino: Tetromino`
- **Methods**:
  - `bool can_place_tetromino() const`: Checks if the active tetromino’s position is valid on the grid.
  - `void place_tetromino()`: Commits the tetromino to the grid if its position is valid.
  - `std::vector<int> clear_and_send_penalties(int lines_cleared)`: Clears lines and returns penalty lines to be sent to opponents based on `lines_cleared`. *(phase 2)*
  - `void spawn_new_tetromino()`: Replaces the active tetromino with a new one.

## View Classes
Handles rendering of the game for either GUI or terminal.

### `GameView` (Abstract Class)
- **Purpose**: Abstract class for rendering the game state.
- **Methods**:
  - `void draw_board(const GameBoard& board)`: Renders the game board grid.
  - `void draw_tetromino(const Tetromino& tetromino)`: Renders the active tetromino.

### `TerminalGameView` (inherits `GameView`)
- **Purpose**: Uses FTXUI to render the game on the terminal.
- **Methods**:
  - `void draw_board(const GameBoard& board)`: Uses FTXUI components to display the grid.
  - `void draw_tetromino(const Tetromino& tetromino)`: Overlays the active tetromino onto the grid in the display.
  - `void update_display()`: Refreshes the terminal to show the latest game state.

## Controller Classes
Handles user inputs and delegates actions to the `GameLogic` and `GameBoard` while ensuring actions are valid before updating.

### `InputHandler`
- **Purpose**: Receives and interprets user inputs.
- **Methods**:
  - `std::string process_input(const std::string& input)`: Maps inputs (e.g., "left", "rotate", "down") to actions.

### `GameController`
- **Purpose**: Mediates between `InputHandler`, `GameLogic`, and `GameView`.
- **Attributes**:
  - `game_logic: GameLogic&`
  - `game_view: GameView&`
  - `input_handler: InputHandler&`
- **Methods**:
  - `void handle_input(const std::string& input)`: Checks if the input action is legal. If valid, updates the game state.
  - `void update()`: Main update loop that handles the game progress (e.g., checking for line clears, advancing tetromino, checking game-over conditions).
