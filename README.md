# Microorganisms Colony Simulator
Turn ★ into ⭐ (top-right corner) if you like the project!

<a href="https://www.buymeacoffee.com/pazoff" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 190px !important;" ></a>

The **Microorganisms Colony Simulator** is an interactive web-based simulation built using **p5.js** and **Chart.js** to model the behavior of microorganisms in a dynamic environment. Users can explore microbial growth, reproduction, and interactions under customizable conditions, including nutrient availability, environmental factors, and hazards. The simulator supports multiple simulation modes, real-time visualization, and detailed logging with graphical analysis of biomass and energy dynamics.

This project is ideal for educational purposes, research simulations, or interactive demonstrations of ecological and biological systems.

## Features

- **Three Simulation Modes**:
  - **Player vs AI**: Control a microorganism to compete against an AI-controlled species.
  - **AI vs AI**: Observe competition between two AI-controlled species.
  - **Colony Simulation**: Simulate multiple species forming colonies with customizable parameters.
- **Dynamic Environment**: Adjust nutrient density, temperature, pH, and hazard presence to influence microbial behavior.
- **Customizable Species**: Define growth rates, reproduction thresholds, initial biomass, and energy for multiple species, with the ability to add new species dynamically.
- **Interactive Controls**: Real-time manipulation of simulation parameters via a responsive UI with tabs, sliders, and toggles.
- **Real-Time Logging**: Detailed simulation log capturing events like growth, reproduction, and death, with copy-to-clipboard functionality.
- **Graphical Analysis**: Visualize average biomass and energy over time using Chart.js plots, with optional auto-update every 5 seconds.
- **Environmental Interactions**: Includes nutrients (basic, rich, decay enzymes, mutagens), enhancers (metabolism, resistance, biomass multipliers), waste production, and hazards.
- **Responsive Design**: Mobile-friendly interface with touch controls for player mode and adaptive layout for different screen sizes.
- **Sound Effects**: Optional audio feedback for events like nutrient absorption and damage (currently using placeholder sounds).
- **Colony Formation**: Simulate cooperative microbial behavior with customizable reproduction and biomass costs.
- **Biomass Popups**: Visual notifications for significant events, displayed in the simulation log.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Microorganisms-Colony-Simulator.git
   cd Microorganisms-Colony-Simulator
   ```

2. **Serve the Application**:
   Since this is a web-based application, you need a local server to run it. You can use Python's built-in HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Alternatively, use any web server (e.g., Node.js with `http-server`, Apache, or Nginx).

3. **Access the Simulator**:
   Open your browser and navigate to `http://localhost:8000/microorganisms.html`.

4. **Dependencies**:
   The simulator uses CDN-hosted libraries:
   - **p5.js** (v1.4.2) for rendering the simulation canvas.
   - **p5.sound** for audio effects.
   - **Chart.js** for plotting biomass and energy graphs.
   No additional installation is required as these are loaded via CDN.

## Usage

1. **Start the Simulation**:
   - Select a mode from the "General" tab (Player vs AI, AI vs AI, or Colony Simulation).
   - Adjust environmental settings (nutrient density, temperature, pH, hazards) and species parameters.
   - Click "New Simulation" to begin.

2. **Interact with the Simulation**:
   - In **Player vs AI** mode, use arrow keys (desktop) or on-screen buttons (mobile) to control your microorganism.
   - Modify parameters in real-time using the "General", "Species", and "Advanced" tabs.
   - Pause or restart the simulation using the control buttons.
   - Toggle sound effects and other features in the "Advanced" tab.

3. **Monitor and Analyze**:
   - View real-time stats (species counts, nutrients, waste) in the stats bar.
   - Check the simulation log for detailed event history.
   - Use the "Update Plots" button or enable auto-update to visualize biomass and energy trends.

4. **Customize**:
   - Add new species in the "Species" tab with custom names, colors, and parameters.
   - Fine-tune advanced settings like nutrient spawn rates, hazard movement, and environmental effects in the "Advanced" tab.

## File Structure

- **microorganisms.html**: The main HTML file containing the simulation logic, UI, and JavaScript code.
- **sounds/**: Directory for sound files (currently uses placeholder `eat.mp3` for all effects).

## Function Descriptions

Below is a comprehensive list of key JavaScript functions and classes in the simulator, organized by their purpose.

### Core Simulation Functions

- **`preload()`**:
  - Loads sound files for simulation events (e.g., nutrient absorption, damage).
  - Uses `soundFormats('mp3', 'wav')` and `loadSound()` from p5.js.

- **`setup()`**:
  - Initializes the p5.js canvas based on `simulationConfig.maxCanvasSize` and `gridSize`.
  - Sets the frame rate and calls `initializeSimulation()` to reset the simulation state.
  - Places the canvas in the `simulationContainer` div.

- **`initializeSimulation()`**:
  - Resets simulation state (microbes, nutrients, waste, popups).
  - Spawns microbes based on the selected mode:
    - **Player vs AI**: One player-controlled and one AI microbe.
    - **AI vs AI**: Two AI-controlled microbes.
    - **Colony Simulation**: Multiple microbes per species.
  - Generates nutrients and hazards based on configuration.

- **`draw()`**:
  - Main animation loop, executed every frame.
  - Renders the simulation state (background, nutrients, hazards, microbes, etc.) if started and not over.
  - Updates entities, checks interactions, and spawns new nutrients/enhancers.
  - Displays a start message or "Simulation Over" text when applicable.

- **`startSimulation()`**:
  - Begins a new simulation by updating configurations and calling `initializeSimulation()`.
  - Logs initial configuration to the simulation log.

- **`restartSimulation()`**:
  - Restarts the simulation with current parameters, resetting the state.

- **`pauseSimulation()`**:
  - Toggles the simulation's paused state by setting the frame rate to 0 (paused) or restoring it (resumed).
  - Updates UI button text and auto-update checkbox state.

- **`updateSimulationMode()`**:
  - Updates the `simulationMode` variable based on the mode selection dropdown.

- **`updateSimulationParams()`**:
  - Updates `simulationConfig` (grid size, canvas size, frame rate) from UI inputs.
  - Resizes the canvas and adjusts `tileSize` accordingly.

- **`updateEnvironment()`**:
  - Updates environmental parameters (`nutrientDensity`, `temperature`, `pH`, hazard count) from UI inputs.
  - Regenerates nutrients and hazards.

- **`updateMicrobeParams()`**:
  - Updates `speciesParams` for each species based on UI inputs (growth rate, reproduction threshold, initial biomass/energy).

- **`addNewSpecies()`**:
  - Adds a new species to `speciesParams` with user-defined parameters (name, color, growth rate, etc.).
  - Appends new control sliders to the "Species" tab UI.
  - Validates unique species names.

- **`updateFeatureToggles()`**:
  - Updates `featureToggles` based on checkbox states (e.g., waste, hazards, sound).
  - Syncs the mute button state.

- **`updateNutrientParams()`**:
  - Updates `nutrientConfig` for nutrient spawn rates, biomass/size gains, and lifetimes from UI inputs.

- **`updateHazardParams()`**:
  - Updates `hazardConfig.moveInterval` from UI input.

- **`updateWasteParams()`**:
  - Updates `wasteConfig` (spawn chance, lifetime, energy penalty) from UI inputs.

- **`updateColonyParams()`**:
  - Updates `colonyConfig` (reproduction chance, biomass cost factor) from UI inputs.

- **`updatePopupParams()`**:
  - Updates `popupConfig` (lifetime, opacity decay, y-speed) from UI inputs.

- **`updateMicrobeMoveParams()`**:
  - Updates `microbeMoveConfig.energyCost` from UI input.

- **`updateEnvEffectParams()`**:
  - Updates `envEffectConfig` (optimal temperature/pH, effect strengths) from UI inputs.

- **`toggleSound()`**:
  - Toggles `featureToggles.soundEnabled` and updates the mute button's text and state.

- **`displayStats()`**:
  - Updates the stats bar with species counts, nutrient count, and waste count, styled with species colors.

- **`keyPressed()`**:
  - Handles arrow key inputs in **Player vs AI** mode to set the player's microbe direction.

- **`setDirection(dx, dy)`**:
  - Sets the player's microbe direction in **Player vs AI** mode for touch controls, ensuring valid moves.

- **`checkInteractions()`**:
  - Checks microbe interactions:
    - Removes microbes with zero biomass/energy.
    - Applies hazard damage if not resistant.
    - Handles inter-species competition (stronger microbe consumes weaker).
    - Ends simulation if no microbes remain or only one species survives.

- **`checkColonyFormation()`**:
  - Manages microbe reproduction if biomass exceeds the threshold and random chance succeeds.
  - Spawns new microbes with biomass cost, avoiding hazards and overlaps.

- **`updateWaste()`**:
  - Filters expired waste products.
  - Applies energy penalties to microbes on waste tiles.

### Classes

- **`Microbe`**:
  - Represents a microorganism with properties like position, direction, biomass, energy, size, and species.
  - Methods:
    - `constructor(x, y, dir, color, species, name)`: Initializes a microbe.
    - `update()`: Updates position, consumes nutrients, applies environmental effects, and produces waste.
    - `updateAI()`: Updates AI-controlled microbes by choosing a direction and calling `update()`.
    - `move()`: Moves the microbe, applying metabolism boost and energy cost.
    - `consumeNutrients()`: Consumes nearby nutrients/enhancers, updating biomass and size.
    - `applyEnvironmentalEffects()`: Adjusts biomass/energy based on temperature and pH.
    - `produceWaste()`: Spawns waste products randomly.
    - `chooseDirection()`: AI logic to move toward nutrients/enhancers or randomly.
    - `isValidMove(dir)`: Checks if a move avoids hazards (if not resistant).
    - `show()`: Renders the microbe as an ellipse with optional resistance aura.

- **`Nutrient`**:
  - Represents a basic nutrient.
  - Methods:
    - `constructor()`: Spawns at a random grid position.
    - `show()`: Renders as a green ellipse.

- **`RichNutrient`**:
  - Represents a high-value nutrient with a limited duration.
  - Methods:
    - `constructor()`: Initializes with inactive state.
    - `maybeSpawn()`: Spawns randomly based on `nutrientConfig.richNutrientSpawn`.
    - `update()`: Manages spawn timer and state.
    - `show()`: Renders as a pulsing gold ellipse.

- **`DecayEnzyme`**:
  - Represents a nutrient that alters size and biomass.
  - Methods:
    - `constructor()`: Spawns randomly with a timer.
    - `spawn()`: Sets random position.
    - `update()`: Deactivates after `decayEnzymeLifetime`.
    - `show()`: Renders as a pink ellipse with a stroke.

- **`Mutagen`**:
  - Represents a nutrient with random positive/negative effects.
  - Methods:
    - `constructor()`: Spawns randomly with a timer.
    - `update()`: Deactivates after `mutagenLifetime`.
    - `show()`: Renders as a purple-bordered square with a "?".

- **`Enhancer`**:
  - Represents a power-up (metabolism boost, resistance, or biomass multiplier).
  - Methods:
    - `constructor()`: Spawns randomly with a random type and timer.
    - `update()`: Deactivates after `enhancerLifetime`.
    - `show()`: Renders based on type (triangle, ellipse, or star).
    - `applyEffect(microbe)`: Applies the enhancer's effect to a microbe.

- **`Hazards`**:
  - Represents acidic zones that damage microbes.
  - Methods:
    - `constructor()`: Initializes an empty hazard list.
    - `generate(numHazards)`: Spawns hazards at non-overlapping positions.
    - `move()`: Relocates hazards periodically based on `hazardConfig.moveInterval`.
    - `show()`: Renders hazards as black rectangles.

- **`Waste`**:
  - Represents waste that penalizes microbe energy.
  - Methods:
    - `constructor(x, y)`: Spawns at a given position with a lifetime.
    - `show()`: Renders as a semi-transparent brown ellipse.

- **`BiomassPopup`**:
  - Represents a notification for simulation events, logged to the UI.
  - Methods:
    - `constructor(x, y, message, color)`: Initializes with a message and color, logging to the UI.
    - `logToBox()`: Appends the message to the simulation log with a timestamp.
    - `show()`: No-op (UI-based popups).
    - `isDone()`: Returns true (instant popups).

### UI and Plotting Functions

- **`copyLogBoxContentOnClick()`**:
  - Adds a click event to the log box to copy its content to the clipboard, showing a confirmation message.

- **`logInitialSimulationConfig()`**:
  - Logs the initial simulation configuration (mode, grid size, environment, toggles, species) to the log box.

- **`toggleRules()`**:
  - Toggles the visibility of the help/rules section.

- **`isMobileDevice()`**:
  - Detects if the user is on a mobile device using `navigator.userAgent`.

- **`windowResized()`**:
  - Resizes the canvas responsively when the window size changes.

- **`plotSimulationLog()`**:
  - Parses the simulation log to extract biomass and energy data for each microbe instance.
  - Generates two line charts (biomass and energy over time) using Chart.js, with species-specific colors.
  - Destroys previous chart instances to prevent memory leaks.

- **`setCheckboxState(checkboxId, action)`**:
  - Checks or unchecks a checkbox programmatically.

- **Auto-Update Logic**:
  - Listens for changes to the `autoUpdateCheckbox` to start/stop a 5-second interval for calling `plotSimulationLog()`.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description of your changes.

Please ensure your code follows the existing style and includes appropriate documentation.

## Future Improvements

- **Enhanced AI**: Improve AI decision-making for more realistic microbial behavior.
- **Sound Effects**: Replace placeholder sounds with event-specific audio.
- **Performance Optimization**: Optimize rendering for large numbers of microbes/nutrients.
- **Data Export**: Allow exporting simulation logs and charts as CSV or images.
- **Multiplayer Mode**: Enable multiple players to control different species.
- **Advanced Interactions**: Add symbiosis, predation, or quorum sensing mechanics.
- **Accessibility**: Improve keyboard navigation and screen reader support.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Acknowledgments

- **p5.js**: For the rendering and animation framework.
- **Chart.js**: For data visualization.
- **xAI**: Inspiration for interactive scientific simulations.

---

Feel free to explore the simulator and experiment with microbial ecosystems! For questions or feedback, open an issue or contact the repository owner.
