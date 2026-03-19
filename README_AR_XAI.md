# AR-XAI OpenWorld Framework

This repository contains the framework for an AR-XAI-OpenWorld game, focusing on Riemannian geometry exploration and physical resource recycling for 3D printing.

## Components

- **Dashboard (Flask)**: A web-based UI for monitoring game progress, player stats, and 3D printer status.
- **Database (SQLAlchemy)**: Manages players, collected plastic resources, and mathematical discoveries.
- **BLE Manager (Bleak)**: Handles communication with AR-XAI hardware modules and 3D printers.
- **Game Logic**: Abstracted Riemannian geometry calculations and plastic-to-resource conversion.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install sqlalchemy bleak flask
    ```

2.  **Initialize Database**:
    ```bash
    python models.py
    ```

3.  **Run the Server**:
    ```bash
    python app.py
    ```
    Access the dashboard at `http://localhost:8080`.

## Key Files

- `app.py`: Main Flask application and API endpoints.
- `models.py`: SQLAlchemy database models.
- `game_logic.py`: Core game and mathematical logic.
- `ble_manager.py`: Bluetooth Low Energy integration.
- `templates/index.html`: Dashboard UI.
