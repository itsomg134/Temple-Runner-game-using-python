#  Temple Runner

An exciting side-scrolling endless runner game built with Python and Pygame, where you navigate through ancient temples, avoid obstacles, and collect treasures!

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pygame Version](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)

##  Game Overview

Temple Runner is a fast-paced endless runner game set in an ancient temple. Control your character as they dash through the temple grounds, jumping over rocks, sliding under logs, and collecting golden coins. The game gets progressively harder as your score increases, testing your reflexes and timing!

##  Features

- **Smooth Controls**: Jump over obstacles and slide under logs with responsive keyboard controls
- **Dynamic Difficulty**: Game speed increases as your score grows
- **Score System**: Earn points for survival and bonus points for collecting coins
- **Multiple Obstacles**: Different obstacles require different strategies (jump over rocks, slide under logs)
- **Visual Effects**: Gradient sky background, animated character, and temple pillars
- **Progressive Gameplay**: Never-ending action with increasing challenge
- **Score Tracking**: Track your high score and coins collected

##  How to Play

### Controls
| Action | Key |
|--------|-----|
| Jump | `SPACE` |
| Slide | `DOWN ARROW` |

### Game Rules
- **Jump** over rocks to avoid collision
- **Slide** under logs to pass safely
- **Collect** golden coins for bonus points
- Survive as long as possible to increase your score
- Game speed increases every 500 points

### Scoring
- **+1 point** for every frame survived
- **+10 points** for each coin collected
- Game speed increases at score milestones

##  Screenshots

<img width="1920" height="1080" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/8a529b0c-a2bb-45be-b01e-a7c72e975070" />
<img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/a0cc0b1a-b9e7-469e-af22-4e075daa11ee" />


##  Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/temple-runner.git
cd temple-runner
```

2. **Install required dependencies**
```bash
pip install pygame
```

3. **Run the game**
```bash
python temple_runner.py
```

##  Game Architecture

### Project Structure
```
temple-runner/
├── temple_runner.py    # Main game file
├── README.md          # Documentation
├── requirements.txt   # Dependencies
└── assets/           # Game assets (optional)
```

### Code Structure
- **TempleRunner Class**: Main game controller handling game loop, states, and rendering
- **Player Class**: Manages player movement, jumping, sliding, and animation
- **Obstacle Class**: Handles obstacle creation, movement, and collision detection
- **Coin Class**: Manages collectible coins and their behavior
- **GameState Enum**: Manages game states (MENU, RUNNING, GAME_OVER)

##  Customization

### Easy Modifications

**Change Game Speed**
```python
# In TempleRunner.__init__()
self.speed = 5  # Default speed - increase for harder start
```

**Adjust Score Multipliers**
```python
# In update() method
self.score += 1  # Change to increase/decrease score rate
```

**Modify Spawn Rates**
```python
# In update() method
if random.randint(1, 100) < 30:  # 30% chance - adjust this value
    self.create_obstacle()
```

##  Troubleshooting

### Common Issues

**Pygame not found**
```bash
pip install pygame
# or
pip3 install pygame
```

**Game runs too fast/slow**
- Check FPS constant (default is 60)
- Adjust game speed variable

**Collision detection issues**
- Verify collision boxes in player and obstacle classes
- Adjust player dimensions

##  Future Enhancements

Planned features for future releases:
- [ ] Power-ups (speed boost, invincibility, magnet for coins)
- [ ] Multiple character skins
- [ ] High score system with persistent storage
- [ ] Sound effects and background music
- [ ] Day/night cycle
- [ ] Different temple environments
- [ ] Mobile touch controls
- [ ] Online leaderboards

##  Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation as needed

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/) - the amazing game development library
- Inspired by classic endless runner games like Temple Run and Subway Surfers
- Thanks to all contributors and testers

##  Contact

Om Gedam

GitHub: [https://github.com/itsomg134](https://github.com/itsomg134)

Email: [omgedam123098@gmail.com](mailto:omgedam123098@gmail.com)

Twitter (X): [https://twitter.com/omgedam](https://twitter.com/omgedam)

LinkedIn: [https://linkedin.com/in/omgedam](https://linkedin.com/in/omgedam)

Portfolio: [https://ogworks.lovable.app](https://ogworks.lovable.app)


## Additional Files to Include

### requirements.txt
```txt
pygame>=2.0.0
```
