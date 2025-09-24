# Movie Explorer Platform

## Usage

### Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/jeetendra29gupta/Movie-Explorer-Platform.git
    cd Movie-Explorer-Platform
    ```

2. Build and Run the Container for backend
    ```bash
    docker build -t movie-explorer-backend ./backend
    docker run -d -p 8181:8181 --name movie-explorer-backend movie-explorer-backend
    ```

3. Build and Run the Container for frontend
    ```bash
    docker build -t movie-explorer-frontend ./frontend
    docker run -d -p 9191:9191 --name movie-explorer-frontend movie-explorer-frontend
    ```
   
4. **Access the API**
   > - Visit [http://localhost:8181/](http://localhost:8181/) for a welcome message.
   > - API docs available at [http://localhost:8181/docs](http://localhost:8181/docs)
   > - UI available at [http://localhost:9191/](http://localhost:9191/)