# Pong Game

Pong Game is a simple implementation of the classic Pong game using Python and the Turtle graphics library. This README provides an overview of the project structure and how the game works.

## Table of Contents
- [Project Structure](#project-structure)
- [How the Game Works](#how-the-game-works)

## Project Structure

The project consists of the following Python files:

- `main.py`: This is the main script that sets up the game, creates the screen, paddles, ball, and game loop.
- `ball.py`: Contains the `Ball` class responsible for the ball's behavior, movement, and collisions.
- `paddle.py`: Defines the `Paddle` class, used for both the right and left paddles.
- `ai_paddle.py`: Extends the `Paddle` class to create an AI-controlled paddle on the left side.
- `center_line.py`: Handles the center line in the game.
- `scoreboard.py`: Manages the game's scorekeeping.

## How the Game Works

The Pong game works as follows:

1. Create a screen with a black background, set to a size of 800x600 pixels.
2. Create two paddles, one on the right and one on the left, each with a width of 20 and a height of 100.
3. Create a ball in the center of the screen.
4. The ball can bounce off the walls, and it bounces differently if it hits a paddle.
5. The right paddle is controlled by the "Up" and "Down" arrow keys.
6. The left paddle is AI-controlled and moves toward the ball's position.
7. The game keeps track of the score with a scoreboard.
8. The game continues until one of the paddles misses the ball, at which point the ball is reset and the score is updated.
9. You can exit the game by clicking on the screen.

Feel free to modify and enhance this Pong game as you see fit. Have fun playing and coding!

Enjoy the game!
